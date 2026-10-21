import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { LIVE } from './config.js';
import { complete, resolveAI } from './llm.js';

// Danh sách agent đọc từ agents.json. Quản Lí (#manager) là agent điều phối; người dùng là CEO.
export const ROOMS = ['Ban điều hành', 'Phòng nghiên cứu', 'Phòng sáng tạo', 'Phòng kỹ thuật'];
const ROOM_CAPACITY = 3;
const FILE = path.join(path.dirname(fileURLToPath(import.meta.url)), 'agents.json');

function normalize(list) {
  const fail = (m) => { throw new Error(m); };
  if (!Array.isArray(list) || !list.length) fail('"agents" phải là mảng có ít nhất 1 agent.');
  const ids = new Set(), perRoom = {};
  const agents = list.map((a, i) => {
    const id = String(a?.id ?? '');
    if (!/^[a-z][a-z0-9_]{0,19}$/.test(id)) fail(`agent #${i + 1}: id "${id}" không hợp lệ (chữ thường/số/_, bắt đầu bằng chữ, tối đa 20 ký tự).`);
    if (ids.has(id)) fail(`id "${id}" bị trùng.`);
    ids.add(id);
    const name = String(a.name ?? '').trim(), basePrompt = String(a.prompt ?? '').trim();
    if (!name || !basePrompt) fail(`agent "${id}" thiếu name hoặc prompt.`);
    const room = a.room || ROOMS[0];
    if (!ROOMS.includes(room)) fail(`agent "${id}": room "${room}" không có (chọn: ${ROOMS.join(', ')}).`);
    perRoom[room] = (perRoom[room] || 0) + 1;
    if (perRoom[room] > ROOM_CAPACITY) fail(`"${room}" tối đa ${ROOM_CAPACITY} agent.`);
    const skills = Array.isArray(a.skills) ? a.skills.map((x) => String(x).trim()).filter(Boolean) : [];
    return {
      id, name, role: String(a.role ?? '').trim(), room, skills, basePrompt,
      color: /^#[0-9a-f]{6}$/i.test(a.color) ? a.color : '#8a8f98',
      prompt: basePrompt + (skills.length ? ` Kỹ năng của bạn: ${skills.join(', ')}.` : ''),
      provider: a.provider ? String(a.provider) : undefined, model: a.model ? String(a.model) : undefined,
    };
  });
  if (agents[0].id !== 'manager') fail('agent đầu tiên phải có id "manager" (agent điều phối).');
  return agents;
}

function readFileAgents() {
  try {
    return normalize(JSON.parse(fs.readFileSync(FILE, 'utf8')).agents);
  } catch (e) {
    throw new Error(`agents.json: ${e.message}`);
  }
}

// AGENTS và IDS được cập nhật tại chỗ để mọi module thấy thay đổi ngay, không cần khởi động lại.
export const AGENTS = readFileAgents();
export const IDS = AGENTS.map((a) => a.id);

export const rawAgents = () => AGENTS.map(({ id, name, role, room, color, skills, basePrompt, provider, model }) =>
  ({ id, name, role, room, color, skills, prompt: basePrompt, provider, model }));

// Kiểm tra danh sách mới, ghi agents.json rồi áp dụng ngay. Sai thì ném lỗi và giữ nguyên danh sách cũ.
export function setAgents(list) {
  const next = normalize(list);
  const tmp = FILE + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify({ agents: next.map(({ id, name, role, room, color, skills, basePrompt, provider, model }) =>
    ({ id, name, role, room, color, skills, prompt: basePrompt, provider, model })) }, null, 2) + '\n');
  fs.renameSync(tmp, FILE);
  AGENTS.splice(0, AGENTS.length, ...next);
  IDS.splice(0, IDS.length, ...next.map((a) => a.id));
}

// Hiển thị AI thực tế của từng agent (không chứa khoá API).
export const aiLabel = (agent) => { const r = resolveAI(agent); return `${r.provider}${r.via === 'cli' ? ' (CLI)' : ''}/${r.model || 'mặc định'}`; };

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const short = (s, n = 60) => (s.length > n ? s.slice(0, n - 1) + '…' : s);

// Kế hoạch mặc định (mock, và khi AI trả kế hoạch không hợp lệ), dựng theo agent đang có.
// Mỗi nhóm chạy song song; nhóm sau phụ thuộc toàn bộ nhóm trước. Agent tuỳ biến chạy ở nhóm "hỗ trợ" trước khâu rà soát.
const STAGES = [
  [['secretary', (c) => `Ghi nhận & làm rõ yêu cầu: ${c}`]],
  [['rag', () => 'Tìm và xếp hạng tài liệu liên quan']],
  [['analyst', () => 'Phân tích kết quả tìm kiếm']],
  [['designer', () => 'Thiết kế giải pháp'], ['writer', () => 'Viết nội dung']],
  [['dev', () => 'Triển khai']],
  [['tester', () => 'Kiểm thử']],
  [['ops', () => 'Kiểm tra cuối & cleanup']],
];
const KNOWN = new Set([...STAGES.flat().map(([id]) => id), 'reviewer', 'manager']);

export function templatePlan(command) {
  const c = short(command, 40);
  const stages = STAGES.map((s) => s.filter(([id]) => IDS.includes(id)).map(([id, t]) => [id, t(c)]));
  const extras = AGENTS.filter((a) => !KNOWN.has(a.id)).map((a) => [a.id, `Hỗ trợ (${a.role || a.name}): ${c}`]);
  if (extras.length) stages.push(extras);
  if (IDS.includes('reviewer')) stages.push([['reviewer', 'Rà soát & duyệt']]);
  const tasks = [];
  let prev = [];
  for (const stage of stages.filter((s) => s.length)) {
    const cur = stage.map(([assignee, title], i) => ({ id: `t${tasks.length + i + 1}`, title, assignee, dependsOn: prev }));
    tasks.push(...cur);
    prev = cur.map((t) => t.id);
  }
  return tasks;
}

const MOCK = {
  secretary: (c) => `Đã ghi nhận yêu cầu "${short(c, 50)}", yêu cầu rõ ràng.`,
  rag: () => 'Top 3 nguồn liên quan đã được xếp hạng; nguồn #1 độ tin cậy 0.92.',
  analyst: () => 'Nhận định: nhu cầu rõ, rủi ro thấp, nên làm bản tối giản trước.',
  designer: () => 'Đề xuất bố cục 2 cột, tông màu dịu, ưu tiên đọc nhanh.',
  writer: () => 'Đã viết xong nội dung chính và tiêu đề.',
  dev: () => 'Đã triển khai chức năng chính, 3 module, sẵn sàng kiểm thử.',
  tester: () => 'Chạy 12 test: 12 đạt, 0 lỗi.',
  ops: () => 'Dịch vụ đã khởi động đủ, cleanup xác nhận. Sẵn sàng bàn giao.',
  reviewer: () => 'Đã duyệt. Kết quả đạt yêu cầu.',
  manager: () => 'Đã xử lý xong yêu cầu.',
};

// Ở chế độ mock, một số agent giả lập việc cần truy cập file hoặc hỏi đồng nghiệp.
const MOCK_ACCESS = {
  rag: { fn: 'readFile', path: 'workspace/notes.txt', ok: (r) => `Đã đọc notes.txt: "${r.content.split('\n')[1]}"` },
  dev: { fn: 'listDir', path: '.', ok: (r) => `Thư mục nguồn có ${r.entries.length} file: ${r.entries.join(', ')}` },
};
const MOCK_CONSULT = {
  dev: { to: 'designer', q: 'Màn hình nào cần làm trước?', a: 'Ưu tiên màn hình giao việc và bảng trạng thái.' },
  tester: { to: 'dev', q: 'Có chức năng nào chưa ổn định không?', a: 'Chưa có, nhưng nên test kỹ phần phân quyền.' },
};
const MOCK_ANSWER = (agent, q) => {
  for (const c of Object.values(MOCK_CONSULT)) if (c.to === agent.id && c.q === q) return c.a;
  return 'Đã nhận câu hỏi, tôi sẽ phản hồi chi tiết sau.';
};

const TOOL_DEFS = [
  { name: 'read_file', description: 'Đọc một file văn bản. Có thể cần người dùng cho phép.',
    parameters: { type: 'object', properties: { path: { type: 'string' } }, required: ['path'] } },
  { name: 'list_dir', description: 'Liệt kê một thư mục. Có thể cần người dùng cho phép.',
    parameters: { type: 'object', properties: { path: { type: 'string' } }, required: ['path'] } },
  { name: 'ask_colleague', description: 'Hỏi nhanh một đồng nghiệp và nhận câu trả lời.',
    parameters: { type: 'object', properties: { to: { type: 'string', enum: IDS }, question: { type: 'string' } }, required: ['to', 'question'] } },
];

const claude = ({ agent, system, user, handlers = {}, max = 400 }) => complete({ agent, system, user, tools: TOOL_DEFS, handlers, max });

// Quản Lí tạo kế hoạch: danh sách task có người nhận và phụ thuộc. Sai định dạng thì dùng kế hoạch mặc định.
export async function makePlan(command) {
  if (!LIVE) { await sleep(1200); return templatePlan(command); }
  try {
    const text = await claude({
      agent: AGENTS[0],
      system: `${AGENTS[0].prompt} Chia yêu cầu thành 3-9 task. Chỉ trả về JSON dạng {"tasks":[{"id":"t1","title":"...","assignee":"<id>","dependsOn":[]}]}. ` +
        `Agent: ${AGENTS.slice(1).map((a) => `${a.id} (${a.role})`).join('; ')}. dependsOn chỉ trỏ tới task đứng trước.`,
      user: command, max: 800,
    });
    const tasks = JSON.parse(text.match(/\{[\s\S]*\}/)[0]).tasks;
    const seen = new Set();
    const ok = Array.isArray(tasks) && tasks.length > 0 && tasks.every((t) => {
      const valid = t.id && t.title && IDS.includes(t.assignee) && t.assignee !== 'manager'
        && Array.isArray(t.dependsOn) && t.dependsOn.every((d) => seen.has(d));
      seen.add(t.id);
      return valid;
    });
    if (ok) return tasks.map(({ id, title, assignee, dependsOn }) => ({ id, title, assignee, dependsOn }));
  } catch { /* dùng kế hoạch mặc định */ }
  return templatePlan(command);
}

// ctx: { command, task, inputs: [{from, text}], tools, ask }
export async function work(agent, ctx) {
  if (LIVE) {
    const inputs = ctx.inputs.map((i) => `[${i.from}] ${i.text}`).join('\n') || '(chưa có)';
    return claude({
      agent,
      system: `${agent.prompt} Trả lời tiếng Việt, tối đa 3 câu. Cần file/thư mục thì dùng công cụ (nếu bị từ chối thì báo lại, đừng thử lại). Cần hỏi đồng nghiệp thì dùng ask_colleague.`,
      user: `Yêu cầu gốc của CEO: ${ctx.command}\nTask của bạn: ${ctx.task.title}\n\nKết quả từ đồng nghiệp:\n${inputs}`,
      handlers: {
        read_file: (i) => ctx.tools.readFile(String(i.path)),
        list_dir: (i) => ctx.tools.listDir(String(i.path)),
        ask_colleague: async (i) => ({ answer: await ctx.ask(String(i.to), String(i.question)) }),
      },
    });
  }
  await sleep(1500 + Math.random() * 1500);
  let out = (MOCK[agent.id] || ((c, t) => `Đã hoàn thành: ${short(t, 60)}`))(ctx.command, ctx.task.title);
  const consult = IDS.includes(MOCK_CONSULT[agent.id]?.to) ? MOCK_CONSULT[agent.id] : null;
  if (consult) out = `Theo ${consult.to}: ${await ctx.ask(consult.to, consult.q)} ${out}`;
  const acc = MOCK_ACCESS[agent.id];
  if (acc) {
    const r = await ctx.tools[acc.fn](acc.path);
    out = r.error ? `${out} (Không truy cập được ${acc.path}: ${r.error})` : `${acc.ok(r)}. ${out}`;
  }
  return out;
}

export async function answer(agent, question, command) {
  if (!LIVE) { await sleep(800); return MOCK_ANSWER(agent, question); }
  return claude({
    agent,
    system: `${agent.prompt} Trả lời tiếng Việt, tối đa 2 câu.`,
    user: `Bối cảnh: ${command}\nĐồng nghiệp hỏi: ${question}`, max: 250,
  });
}

// items: [{ agent, title, status, text }]
export async function summarize(command, items) {
  const lines = items.map((i) => `- [${i.status}] ${i.agent}: ${i.title} → ${i.text}`).join('\n');
  if (!LIVE) {
    await sleep(800);
    const done = items.filter((i) => i.status === 'done').length;
    return `Yêu cầu "${short(command, 50)}": hoàn thành ${done}/${items.length} task.\n${lines}`;
  }
  return claude({
    agent: AGENTS[0],
    system: `${AGENTS[0].prompt} Viết báo cáo cuối cho CEO bằng tiếng Việt, tối đa 5 câu, nêu rõ task nào chưa xong.`,
    user: `Yêu cầu: ${command}\nKết quả các task:\n${lines}`, max: 500,
  });
}
