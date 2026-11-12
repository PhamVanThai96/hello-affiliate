#!/usr/bin/env node
// Dựng lại công thức LaTeX ($...$, $$...$$, \(..\), \[..\]) trong các báo cáo .html ĐÃ tạo trước đây (báo cáo mới tự dựng sẵn khi tạo).
//   node scripts/render_math_reports.mjs [file.html ...]     # không tham số: mọi .html trong reports/ có công thức chưa dựng
// Idempotent: file đã dựng (có <math>) hoặc không có công thức thì bỏ qua. Bản gốc lưu ở BACKUP_DIR (mặc định reports/.math-backup/, không hiện trong danh sách báo cáo).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { texHtml } from '../report.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const REPORTS = path.join(ROOT, 'reports');
const BACKUP = process.env.BACKUP_DIR || path.join(REPORTS, '.math-backup');
const ENT = { '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&nbsp;': ' ' };
const decode = (s) => s.replace(/&(amp|lt|gt|quot|#39|nbsp);/g, (m) => ENT[m]).replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)));
const clean = (s) => decode(s.replace(/<br\s*\/?>/gi, '\n').replace(/<\/?(p|li|ol|ul|b|i|strong|em)\b[^>]*>/gi, ''));
const MATH = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<![\\$])\$(?![\s$])([^$\n<>]+?)(?<![\s\\])\$(?![\d$])/g;

export function renderHtml(html) {
  const keep = [];
  const protectedHtml = html.replace(/<(pre|code|style|script)\b[\s\S]*?<\/\1>/gi, (m) => { keep.push(m); return `@@K${keep.length - 1}@@`; });
  let n = 0;
  const out = protectedHtml.replace(MATH, (m, d1, d2, i1, i2) => {
    const display = d1 != null || d2 != null;
    const tex = clean(d1 ?? d2 ?? i1 ?? i2);
    if (!tex.trim()) return m;
    n++;
    return texHtml(tex, display);
  });
  return { html: out.replace(/@@K(\d+)@@/g, (_, i) => keep[Number(i)]), count: n };
}

const CSS_ADD = 'math{font-size:1.12em}math[display="block"]{display:block math;margin:.7em 0;overflow-x:auto}';
const files = process.argv.length > 2 ? process.argv.slice(2).map((f) => path.resolve(f))
  : fs.existsSync(REPORTS) ? fs.readdirSync(REPORTS).filter((f) => f.endsWith('.html')).map((f) => path.join(REPORTS, f)) : [];
let changed = 0;
for (const f of files) {
  const src = fs.readFileSync(f, 'utf8');
  if (!/[$]|\\[(\[]/.test(src)) continue;
  const { html, count } = renderHtml(src);
  if (!count) continue;
  fs.mkdirSync(BACKUP, { recursive: true });
  fs.copyFileSync(f, path.join(BACKUP, path.basename(f)));
  fs.writeFileSync(f, html.includes('math{font-size') ? html : html.replace('</style>', `${CSS_ADD}</style>`));
  console.log(`✔ ${path.basename(f)}: dựng ${count} công thức`);
  changed++;
}
console.log(changed ? `Xong ${changed} file.` : 'Không có file nào cần dựng lại công thức.');
