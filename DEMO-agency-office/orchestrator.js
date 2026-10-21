import { AGENTS, work, makePlan, summarize, answer } from './agents.js';
import { toolsFor } from './access.js';

const byId = new Proxy({}, { get: (_, id) => AGENTS.find((a) => a.id === id) });
const CEO = 'manager';
const short = (s, n = 90) => (s.length > n ? s.slice(0, n - 1) + '…' : s);

// Vòng lặp xã hội: CEO(user) → Quản Lí → (assign) → agent ⇄ agent (handoff/hỏi đáp) → (report) → Quản Lí → (final) → user
export function createOrchestrator({ emit, state }) {
  const locks = {};
  // Mỗi agent chỉ làm một task một lúc; các task khác của agent đó xếp hàng.
  const withAgent = (id, fn) => {
    const p = (locks[id] || Promise.resolve()).then(fn);
    locks[id] = p.catch(() => {});
    return p;
  };
  const msg = (from, to, kind, text) => emit({ type: 'msg', from, to, kind, text });
  const setStatus = (id, status, report) => emit({ type: 'status', id, status, report });

  async function consult(from, toId, question, command) {
    if (!byId[toId] || toId === from.id) return 'Không có đồng nghiệp này.';
    if (state[toId].status === 'offline') return `${byId[toId].name} đang offline.`;
    msg(from.id, toId, 'question', question);
    const a = await answer(byId[toId], question, command);
    msg(toId, from.id, 'answer', a);
    return a;
  }

  async function run(raw) {
    let command = raw;
    let direct = null;
    const m = raw.match(/^\/(\w+)\s+([\s\S]+)/);
    if (m && byId[m[1]]) {
      command = m[2];
      if (m[1] !== CEO) direct = m[1];
    }
    if (state[CEO].status === 'offline') {
      emit({ type: 'log', from: 'Hệ thống', text: 'Quản Lí đang offline, không có ai nhận lệnh. Hãy bật Quản Lí online.' });
      return;
    }

    msg('user', CEO, 'command', command);
    setStatus(CEO, 'working', 'Đang lập kế hoạch…');
    const tasks = direct
      ? [{ id: 't1', title: command, assignee: direct, dependsOn: [] }]
      : await makePlan(command);
    emit({ type: 'plan', tasks: tasks.map((t) => ({ ...t, status: 'pending' })) });
    for (const t of tasks) msg(CEO, t.assignee, 'assign', t.title);
    setStatus(CEO, 'working', `Đã tạo ${tasks.length} task, đang theo dõi tiến độ.`);

    const results = {};
    const started = {};
    const byTask = Object.fromEntries(tasks.map((t) => [t.id, t]));

    const exec = async (t) => {
      const deps = await Promise.all(t.dependsOn.map((d) => start(byTask[d])));
      const a = byId[t.assignee];
      if (state[a.id].status === 'offline') {
        emit({ type: 'task', id: t.id, status: 'skipped' });
        msg(a.id, CEO, 'report', `${a.name} đang offline, task bị bỏ qua.`);
        return { status: 'skipped', text: `${a.name} offline` };
      }
      const inputs = [];
      deps.forEach((d, i) => {
        if (d.status !== 'done') return;
        const from = byTask[t.dependsOn[i]].assignee;
        inputs.push({ from: byId[from].name, text: d.text });
        if (from !== a.id) msg(from, a.id, 'handoff', short(d.text));
      });
      return withAgent(a.id, async () => {
        emit({ type: 'task', id: t.id, status: 'running' });
        setStatus(a.id, 'working');
        try {
          const text = await work(a, {
            command, task: t, inputs,
            tools: toolsFor(a, emit),
            ask: (to, q) => consult(a, to, q, command),
          });
          setStatus(a.id, 'idle', text);
          msg(a.id, CEO, 'report', short(text, 140));
          emit({ type: 'task', id: t.id, status: 'done' });
          return { status: 'done', text };
        } catch (e) {
          const text = `Lỗi: ${e.message}`;
          setStatus(a.id, 'error', text);
          msg(a.id, CEO, 'report', short(text, 140));
          emit({ type: 'task', id: t.id, status: 'failed' });
          return { status: 'failed', text };
        }
      });
    };
    const start = (t) => (started[t.id] ||= exec(t).then((r) => (results[t.id] = r)));

    await Promise.all(tasks.map(start));

    setStatus(CEO, 'working', 'Đang tổng hợp báo cáo…');
    const items = tasks.map((t) => ({ agent: byId[t.assignee].name, title: t.title, ...results[t.id] }));
    let text;
    try {
      text = direct ? items[0].text : await summarize(command, items);
    } catch (e) {
      text = `Không tổng hợp được báo cáo: ${e.message}`;
    }
    msg(CEO, 'user', 'final', short(text, 140));
    emit({ type: 'final', text, tasks: items.map((i) => ({ agent: i.agent, title: i.title, status: i.status })) });
    setStatus(CEO, 'idle', text);
  }

  return run;
}
