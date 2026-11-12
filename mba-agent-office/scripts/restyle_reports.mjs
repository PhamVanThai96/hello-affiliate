#!/usr/bin/env node
// Đưa các báo cáo .html ĐÃ tạo sang mẫu mới (tiêu đề dạng banner, bảng/khung kết luận đẹp hơn, dòng --- thành đường kẻ...).
//   node scripts/restyle_reports.mjs [file.html ...]   # không tham số: mọi .html trong reports/
// Idempotent (file đã có <main class="paper"> bị bỏ qua). Bản gốc lưu ở reports/.restyle-backup/.
// Ảnh biểu đồ tham chiếu bằng đường dẫn reports/stock-charts/*.png (kiểu cũ) được nhúng thẳng vào file rồi xoá ảnh/json rời.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { pageShell } from '../report.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const REPORTS = path.join(ROOT, 'reports'), BACKUP = path.join(REPORTS, '.restyle-backup');
const unesc = (s) => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
const files = process.argv.length > 2 ? process.argv.slice(2).map((f) => path.resolve(f)) : fs.readdirSync(REPORTS).filter((f) => f.endsWith('.html')).map((f) => path.join(REPORTS, f));
const protect = (html, fn) => { const keep = []; const h = html.replace(/<(math|pre|svg|style)\b[\s\S]*?<\/\1>/g, (m) => { keep.push(m); return `@@K${keep.length - 1}@@`; }); return fn(h).replace(/@@K(\d+)@@/g, (_, i) => keep[+i]); };
let n = 0;
for (const f of files) {
  const src = fs.readFileSync(f, 'utf8');
  if (src.includes('<main class="paper">')) continue;
  const title = (src.match(/<title>([\s\S]*?)<\/title>/) || [])[1] || 'Báo cáo';
  const head = src.match(/<h2>([\s\S]*?)<\/h2><p class="meta"><b>Lệnh:<\/b>\s*([\s\S]*?)<br>([\s\S]*?)<\/p>(?:<p class="meta">([\s\S]*?)<\/p>)?/);
  if (!head) { console.log('bỏ qua (không nhận ra cấu trúc):', path.basename(f)); continue; }
  let body = src.slice(src.indexOf(head[0]) + head[0].length);
  // Báo cáo tổng hợp lỗi (Quản Lí không tổng hợp được) mà đã có phần chi tiết: bỏ khung lỗi, bỏ tiêu đề agent khi chỉ có 1 agent.
  const dets = body.match(/<h3>[^<]*<span class="st done">done<\/span><\/h3><div class="meta">[\s\S]*?<\/div>/g) || [];
  if (/<div class="sum"><p>Không tổng hợp được/.test(body) && dets.length) body = body.replace(/<div class="sum"><p>Không tổng hợp được[\s\S]*?<\/p><\/div>\s*/, '');
  const allH3 = (body.match(/<h3>[^<]*<span class="st /g) || []).length;
  body = body.replace(/<h3>Danh sách công việc<\/h3><div class="tw">([\s\S]*?)<\/div>\s*$/, (_, t) => (allH3 === 1 ? '' : `<details class="tasks"><summary>Danh sách công việc</summary><div class="tw">${t}</div></details>`));
  if (allH3 === 1 && dets.length === 1) body = body.replace(dets[0], '');
  // Ảnh biểu đồ kiểu cũ: dòng "File biểu đồ ... <code>reports/stock-charts/x.png</code>" -> ảnh nhúng.
  const m = body.match(/<code>(?:\.\/)?(?:reports\/)?(stock-charts\/[^<]+?\.png)<\/code>/);
  if (m && fs.existsSync(path.join(REPORTS, m[1]))) {
    const sharp = (await import('sharp')).default;
    const buf = await sharp(path.join(REPORTS, m[1])).resize({ width: 1500, withoutEnlargement: true }).png().toBuffer();
    const fig = `<figure><img src="data:image/png;base64,${buf.toString('base64')}" alt="Biểu đồ kỹ thuật"></figure>`;
    body = body.replace(/<p>[^<]*lưu tại[^<]*<br><code>[^<]+<\/code><\/p>\s*(<p>Dưới đây[^<]*<\/p>\s*)?/, `${fig}\n`);
    if (!body.includes('data:image/png')) body = `<h3>Biểu đồ kỹ thuật</h3>${fig}${body}`;
  }
  body = protect(body, (h) => h.replace(/(?<![\w*>])\*([^*\s<][^*<]*?)\*(?![\w*])/g, '<i>$1</i>'));
  fs.mkdirSync(BACKUP, { recursive: true });
  fs.copyFileSync(f, path.join(BACKUP, path.basename(f)));
  fs.writeFileSync(f, pageShell({ title: unesc(head[1]), command: unesc(head[2]), when: unesc(head[3]), links: head[4] || '', body }).replace(/<title>[\s\S]*?<\/title>/, `<title>${title}</title>`));
  console.log('✔', path.basename(f)); n++;
}
const sc = path.join(REPORTS, 'stock-charts');
if (fs.existsSync(sc)) { fs.rmSync(sc, { recursive: true }); console.log('Đã xoá reports/stock-charts (ảnh đã nhúng vào báo cáo)'); }
console.log(n ? `Xong ${n} file.` : 'Không có file nào cần đổi.');
