import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { CONFIG } from './config.js';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const STORE = path.join(ROOT, 'permissions.json');

let allowed = [];
try { allowed = JSON.parse(fs.readFileSync(STORE, 'utf8')).allowed || []; } catch { /* chưa có quyền nào được lưu */ }

const pending = new Map();
let seq = 0;

// Đường dẫn thật (xử lý .. và symlink) để không né được kiểm tra quyền.
function canon(p) {
  const abs = path.resolve(CONFIG.sourceDir, p);
  try { return fs.realpathSync(abs); } catch { return abs; }
}

const covered = (c) => allowed.some((a) => c === a || c.startsWith(a + path.sep));

export const listAllowed = () => [...allowed];
export const listPending = () => [...pending.values()].map(({ resolve, ...p }) => p);

export function revoke(p) {
  allowed = allowed.filter((a) => a !== p);
  fs.writeFileSync(STORE, JSON.stringify({ allowed }, null, 2));
}

export function decide(id, allow) {
  const req = pending.get(id);
  if (!req) return false;
  pending.delete(id);
  if (allow && !covered(req.path)) {
    allowed.push(req.path);
    fs.writeFileSync(STORE, JSON.stringify({ allowed }, null, 2));
  }
  req.resolve(allow);
  return true;
}

// Trả về true nếu đã có quyền (đã nhớ) hoặc người dùng vừa cho phép.
async function ensureAccess(agent, p, action, onEvent) {
  const c = canon(p);
  if (covered(c)) return c;
  const id = `req${++seq}`;
  onEvent?.({ type: 'status', id: agent.id, status: 'waiting' });
  const granted = await new Promise((resolve) => {
    pending.set(id, { id, agent: agent.name, path: c, action, resolve });
    onEvent?.({ type: 'log', from: agent.name, text: `Xin quyền ${action}: ${c}` });
  });
  onEvent?.({ type: 'status', id: agent.id, status: 'working' });
  onEvent?.({ type: 'log', from: 'Hệ thống', text: `${granted ? 'Đã cho phép (ghi nhớ)' : 'Đã từ chối'}: ${c}` });
  return granted ? c : null;
}

export function toolsFor(agent, onEvent) {
  const denied = { error: 'Người dùng đã từ chối quyền truy cập.' };
  return {
    async readFile(p) {
      const c = await ensureAccess(agent, p, 'đọc file', onEvent);
      if (!c) return denied;
      try { return { content: fs.readFileSync(c, 'utf8').slice(0, 4000) }; } catch (e) { return { error: e.message }; }
    },
    async listDir(p) {
      const c = await ensureAccess(agent, p, 'xem thư mục', onEvent);
      if (!c) return denied;
      try { return { entries: fs.readdirSync(c).slice(0, 100) }; } catch (e) { return { error: e.message }; }
    },
  };
}
