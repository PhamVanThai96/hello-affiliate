#!/usr/bin/env node
// Bỏ mục "Diễn giải" (h5 "Diễn giải" cho tới tiêu đề kế tiếp) khỏi báo cáo .html đã tạo. Bản gốc lưu ở reports/.commentary-backup/.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const R = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'reports'), B = path.join(R, '.commentary-backup');
let n = 0;
for (const f of fs.readdirSync(R).filter((x) => x.endsWith('.html'))) {
  const p = path.join(R, f), s = fs.readFileSync(p, 'utf8');
  const out = s.replace(/<h[3-6]>Diễn giải<\/h[3-6]>[\s\S]*?(?=<h[3-6]>|<hr>|<\/section>|<\/main>)/g, '');
  if (out === s) continue;
  fs.mkdirSync(B, { recursive: true }); fs.copyFileSync(p, path.join(B, f)); fs.writeFileSync(p, out); console.log('✔', f, `(-${s.length - out.length} ký tự)`); n++;
}
console.log(n ? `Xong ${n} file.` : 'Không có mục Diễn giải nào.');
