import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { AGENTS, ROOMS, aiLabel, rawAgents, setAgents } from './agents.js';
import { CONFIG } from './config.js';
import { createOrchestrator } from './orchestrator.js';
import { listPending, decide, listAllowed, revoke } from './access.js';

const dir = path.dirname(fileURLToPath(import.meta.url));
const PORT = CONFIG.port;
const history = [];
const state = Object.fromEntries(AGENTS.map((a) => [a.id, { status: 'idle', report: '' }]));
let busy = false;
let agentsVer = 1;

function emit(event) {
  if (event.type === 'status') state[event.id] = { status: event.status, report: event.report ?? state[event.id].report };
  history.push(event);
}

const run = createOrchestrator({ emit, state });

const readJson = (req) => new Promise((resolve) => {
  let body = '';
  req.on('data', (d) => (body += d));
  req.on('end', () => { try { resolve(JSON.parse(body)); } catch { resolve({}); } });
});

const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' };

http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');

  if (req.method === 'GET' && url.pathname === '/poll') {
    const since = Number(url.searchParams.get('since')) || 0;
    const full = Number(url.searchParams.get('ver')) !== agentsVer;
    res.writeHead(200, { 'content-type': 'application/json', 'cache-control': 'no-store' });
    res.end(JSON.stringify({
      next: history.length, mode: CONFIG.mode, connection: CONFIG.connection, provider: CONFIG.provider, model: CONFIG.model, sourceDir: CONFIG.sourceDir, modeNote: CONFIG.note, pending: listPending(), allowed: listAllowed(),
      agentsVer,
      agents: full ? AGENTS.map(({ prompt, basePrompt, ...a }) => ({ ...a, prompt: basePrompt, ai: aiLabel(a) })) : undefined,
      state: full ? state : undefined,
      rooms: full ? ROOMS : undefined,
      keys: full ? Object.fromEntries(Object.entries(CONFIG.connection === 'CLI' ? CONFIG.cliOk : CONFIG.keys).map(([k, v]) => [k, Boolean(v)])) : undefined,
      events: history.slice(since),
    }));
    return;
  }

  if (req.method === 'POST') {
    const b = await readJson(req);
    if (url.pathname === '/task') {
      const task = typeof b.task === 'string' ? b.task.trim() : '';
      if (!task) { res.writeHead(400).end('missing task'); return; }
      if (busy) { res.writeHead(409).end('office is busy'); return; }
      busy = true;
      run(task)
        .catch((e) => emit({ type: 'log', from: 'Hệ thống', text: `Lỗi: ${e.message}` }))
        .finally(() => { busy = false; emit({ type: 'done' }); });
      res.writeHead(202).end('ok');
      return;
    }
    if (url.pathname === '/agent/save' || url.pathname === '/agent/delete') {
      if (busy) { res.writeHead(409).end('Văn phòng đang xử lý yêu cầu, hãy chỉnh sửa sau khi xong.'); return; }
      const list = rawAgents();
      const id = String(b.agent?.id ?? b.id ?? '');
      const i = list.findIndex((a) => a.id === id);
      try {
        if (url.pathname === '/agent/delete') {
          if (i < 0) throw new Error('Không có agent này.');
          if (id === 'manager') throw new Error('Không thể xoá agent điều phối (manager).');
          list.splice(i, 1);
        } else if (b.isNew) {
          if (i >= 0) throw new Error(`id "${id}" đã tồn tại.`);
          list.push(b.agent);
        } else {
          if (i < 0) throw new Error('Không có agent này.');
          list[i] = { ...b.agent, id };
        }
        setAgents(list);
      } catch (e) { res.writeHead(400).end(e.message); return; }
      for (const a of AGENTS) state[a.id] ??= { status: 'idle', report: '' };
      for (const k of Object.keys(state)) if (!AGENTS.some((a) => a.id === k)) delete state[k];
      agentsVer++;
      res.writeHead(200).end('ok');
      return;
    }
    if (url.pathname === '/permission') { res.writeHead(decide(b.id, b.allow === true) ? 200 : 404).end(); return; }
    if (url.pathname === '/revoke') { revoke(String(b.path)); res.writeHead(200).end('ok'); return; }
    if (url.pathname === '/online') {
      const cur = state[b.id]?.status;
      if (!cur || cur === 'working' || cur === 'waiting') { res.writeHead(409).end('agent unavailable or busy'); return; }
      emit({ type: 'status', id: b.id, status: b.online ? 'idle' : 'offline' });
      res.writeHead(200).end('ok');
      return;
    }
    res.writeHead(404).end('not found');
    return;
  }

  const pub = path.join(dir, 'public');
  const file = path.join(pub, url.pathname === '/' ? 'index.html' : path.normalize(url.pathname));
  if (!file.startsWith(pub + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    res.writeHead(404).end('not found');
    return;
  }
  res.writeHead(200, { 'content-type': mime[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
}).listen(PORT, () => console.log(`Agent Office: http://localhost:${PORT}  (MODE=${CONFIG.mode}, ${CONFIG.connection} ${CONFIG.provider}/${CONFIG.model || 'mặc định'}, SOURCE_DIR=${CONFIG.sourceDir})`));
