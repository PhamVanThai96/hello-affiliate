// Quản lý vòng đời: theo dõi tiến trình con và dừng gọn khi nhận Ctrl+C (SIGINT) / SIGTERM / SIGHUP.
const children = new Set();

export function trackChild(child) {
  if (!child) return child;
  children.add(child);
  const drop = () => children.delete(child);
  child.once('close', drop);
  child.once('error', drop);
  return child;
}

export function killChildren(signal = 'SIGTERM') {
  for (const c of children) {
    try { c.pid && c.spawnargs && c.spawnfile && process.kill(-c.pid, signal); } catch { try { c.kill(signal); } catch { /* đã thoát */ } }
    try { c.kill(signal); } catch { /* đã thoát */ }
  }
}

export function installShutdown({ server, onStop, graceMs = 800 } = {}) {
  let stopping = false;
  const shutdown = (sig) => {
    if (stopping) { console.log('\nThoát ngay.'); process.exit(1); }
    stopping = true;
    console.log(`\nĐang dừng MBA Office (${sig})… nhấn Ctrl+C lần nữa để thoát ngay.`);
    try { onStop?.(); } catch { /* bỏ qua */ }
    killChildren('SIGTERM');
    try { server?.close(); server?.closeAllConnections?.(); } catch { /* bỏ qua */ }
    setTimeout(() => { killChildren('SIGKILL'); process.exit(0); }, graceMs);
  };
  for (const s of ['SIGINT', 'SIGTERM', 'SIGHUP']) process.on(s, () => shutdown(s));
}
