import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildReport, mdPage } from './report.js';
import { clearMemory, memorySize } from './memory.js';
import { exportFile, formatsFor } from './export.js';
import { AGENTS, ROOMS, aiLabel, rawAgents, setAgents } from './agents.js';
import { CONFIG, settings, saveSettings } from './config.js';
import { createOrchestrator } from './orchestrator.js';
import { listPending, decide, listAllowed, revoke } from './access.js';

const dir = path.dirname(fileURLToPath(import.meta.url));
const PORT = CONFIG.port;
const history = [];
const state = Object.fromEntries(AGENTS.map((a) => [a.id, { status: 'idle', report: '' }]));
let busy = false;
let agentsVer = 1;
const REPORTS = path.join(dir, 'reports');
fs.mkdirSync(REPORTS, { recursive: true });
let lastCommand = '';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

async function saveReport(ev) {
  const t = new Date(), p2 = (n) => String(n).padStart(2, '0');
  const name = `bao-cao-${t.getFullYear()}${p2(t.getMonth() + 1)}${p2(t.getDate())}-${p2(t.getHours())}${p2(t.getMinutes())}${p2(t.getSeconds())}.html`;
  fs.writeFileSync(path.join(REPORTS, name), await buildReport(ev, lastCommand, t.toLocaleString('vi-VN')));
  return name;
}

function listReports(base = '') {
  const out = [];
  for (const e of fs.readdirSync(path.join(REPORTS, base), { withFileTypes: true })) {
    const rel = base ? `${base}/${e.name}` : e.name;
    if (e.name.startsWith('.')) continue;
    if (e.isDirectory()) out.push(...listReports(rel));
    else { const st = fs.statSync(path.join(REPORTS, rel)); out.push({ name: rel, size: st.size, mtime: st.mtimeMs, formats: formatsFor(rel) }); }
  }
  return out;
}

function emit(event) {
  if (event.type === 'msg' && event.kind === 'command') lastCommand = event.text;
  if (event.type === 'final') {
    // Dựng báo cáo (có ảnh/bảng/biểu đồ) rồi mới gửi sự kiện, bỏ phần chi tiết nặng khỏi luồng gửi trình duyệt.
    return saveReport(event).catch((e) => console.warn(`[report] ${e.message}`)).then((file) => {
      if (file) event.file = file;
      delete event.details; delete event.artifacts;
      history.push(event);
    });
  }
  if (event.type === 'status') state[event.id] = { status: event.status, report: event.report ?? state[event.id].report };
  history.push(event);
}

const run = createOrchestrator({ emit, state });

const readJson = (req) => new Promise((resolve) => {
  let body = '';
  req.on('data', (d) => (body += d));
  req.on('end', () => { try { resolve(JSON.parse(body)); } catch { resolve({}); } });
});

const mime = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css' };
const rmime = {
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.html': 'text/html; charset=utf-8', '.htm': 'text/html; charset=utf-8', '.csv': 'text/csv; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8', '.md': 'text/plain; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml',
};

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
      settings: full ? settings() : undefined,
      keys: full ? Object.fromEntries(Object.entries(CONFIG.connection === 'CLI' ? CONFIG.cliOk : CONFIG.keys).map(([k, v]) => [k, Boolean(v)])) : undefined,
      events: history.slice(since),
    }));
    return;
  }

  if (req.method === 'GET' && (url.pathname === '/reports' || url.pathname === '/reports/')) {
    if (url.searchParams.has('list')) {
      res.writeHead(200, { 'content-type': 'application/json', 'cache-control': 'no-store' });
      res.end(JSON.stringify(listReports().sort((a, b) => b.mtime - a.mtime)));
    } else {
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' });
      fs.createReadStream(path.join(dir, 'public', 'reports.html')).pipe(res);
    }
    return;
  }
  if (req.method === 'GET' && url.pathname.startsWith('/reports/')) {
    let rel;
    try { rel = decodeURIComponent(url.pathname.slice(9)); } catch { rel = ''; }
    const f = path.join(REPORTS, path.normalize(rel));
    if (!rel || !f.startsWith(REPORTS + path.sep) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404).end('not found'); return; }
    const fmt = url.searchParams.get('export');
    if (fmt) {
      let r;
      try { r = await exportFile(f, fmt); } catch (e) { r = { error: e.message }; }
      if (r.error) { res.writeHead(400, { 'content-type': 'text/plain; charset=utf-8' }).end(r.error); return; }
      res.writeHead(200, { 'content-type': r.mime, 'content-disposition': `attachment; filename*=UTF-8''${encodeURIComponent(r.name)}`, 'x-content-type-options': 'nosniff', 'cache-control': 'no-store', 'content-length': r.data.length });
      res.end(r.data);
      return;
    }
    // sandbox: HTML/SVG trong reports không chạy script với quyền của trang chính
    if (/\.(md|markdown)$/i.test(f) && !url.searchParams.has('download')) {
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8', 'content-security-policy': 'sandbox allow-popups', 'x-content-type-options': 'nosniff', 'cache-control': 'no-store' });
      res.end(mdPage(path.basename(f), fs.readFileSync(f, 'utf8')));
      return;
    }
    const dl = url.searchParams.has('download') ? { 'content-disposition': `attachment; filename*=UTF-8''${encodeURIComponent(path.basename(f))}` } : {};
    res.writeHead(200, {
      ...dl,
      'content-type': rmime[path.extname(f).toLowerCase()] || 'application/octet-stream',
      'content-security-policy': 'sandbox allow-popups', 'x-content-type-options': 'nosniff', 'cache-control': 'no-store',
    });
    // Excel chỉ nhận đúng UTF-8 khi CSV có BOM; thêm khi tải về nếu file chưa có.
    if (dl['content-disposition'] && path.extname(f).toLowerCase() === '.csv') {
      const head = Buffer.alloc(3); const fd = fs.openSync(f, 'r'); fs.readSync(fd, head, 0, 3, 0); fs.closeSync(fd);
      if (!head.equals(Buffer.from([0xef, 0xbb, 0xbf]))) res.write(Buffer.from([0xef, 0xbb, 0xbf]));
    }
    fs.createReadStream(f).pipe(res);
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
          list[i] = { ...list[i], ...b.agent, id };
        }
        setAgents(list);
      } catch (e) { res.writeHead(400).end(e.message); return; }
      for (const a of AGENTS) state[a.id] ??= { status: 'idle', report: '' };
      for (const k of Object.keys(state)) if (!AGENTS.some((a) => a.id === k)) delete state[k];
      agentsVer++;
      res.writeHead(200).end('ok');
      return;
    }
    if (url.pathname === '/memory/clear') { clearMemory(); res.writeHead(200).end('ok'); return; }
    if (url.pathname === '/config/save') {
      const origin = req.headers.origin;
      if (origin && new URL(origin).host !== req.headers.host && !req.headers['x-forwarded-host']) { res.writeHead(403).end('forbidden'); return; }
      if (busy) { res.writeHead(409).end('Văn phòng đang xử lý yêu cầu, hãy đổi cấu hình sau khi xong.'); return; }
      try { saveSettings(b); } catch (e) { res.writeHead(400).end(e.message); return; }
      agentsVer++;
      res.writeHead(200).end('ok');
      return;
    }
    if (url.pathname === '/permission') { res.writeHead(decide(b.id, b.allow === true) ? 200 : 404).end(); return; }
    if (url.pathname === '/revoke') { revoke(String(b.path), b.mode === 'write' ? 'write' : 'read'); res.writeHead(200).end('ok'); return; }
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
