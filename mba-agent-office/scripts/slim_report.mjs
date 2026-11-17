#!/usr/bin/env node
// Rút gọn báo cáo .html đã tạo: giữ khung Kết luận, ma trận định giá (bảng có cột "Giá cơ sở") và biểu đồ; bỏ phần suy luận của từng agent + danh sách công việc.
//   node scripts/slim_report.mjs reports/<file>.html [...]   (bản gốc lưu ở reports/.slim-backup/)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const R = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'reports'), B = path.join(R, '.slim-backup');
for (const arg of process.argv.slice(2)) {
  const f = path.resolve(arg); let t = fs.readFileSync(f, 'utf8');
  const sum = t.indexOf('<div class="sum">'), firstH3 = t.indexOf('<h3>', sum);
  if (sum < 0 || firstH3 < 0) { console.log('bỏ qua (không nhận ra cấu trúc):', path.basename(f)); continue; }
  const tail = t.indexOf('</main>');
  const mx = (t.slice(firstH3, tail).match(/<div class="tw matrix">[\s\S]*?<\/div>/) || [''])[0];
  const imgs = [...t.slice(firstH3, tail).matchAll(/<figure><img [\s\S]*?<\/figure>/g)].slice(0, 1).map((m) => m[0]).join('');
  fs.mkdirSync(B, { recursive: true }); fs.copyFileSync(f, path.join(B, path.basename(f)));
  const body = `${mx ? `<h3>Ma trận định giá</h3>${mx}\n` : ''}${imgs ? `<h3>Biểu đồ</h3>${imgs}\n` : ''}`;
  t = t.slice(0, firstH3) + body + t.slice(tail);
  fs.writeFileSync(f, t); console.log('✔', path.basename(f), `${(t.length / 1024).toFixed(0)} KB`, mx ? '(có ma trận)' : '(không có ma trận)');
}
