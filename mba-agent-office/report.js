// Dựng báo cáo HTML tự chứa (không cần file ngoài): chữ, bảng markdown, biểu đồ ```chart (SVG) và ảnh agent đã tạo.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import katex from 'katex';

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
const PALETTE = ['#4f7cff', '#ff8a3d', '#2fb67c', '#c35bd6', '#e5484d', '#e0b300', '#18a0c8', '#8a8f98'];
const fmt = (n) => (Number.isFinite(n) ? n.toLocaleString('vi-VN', { maximumFractionDigits: 2 }) : '');
const IMG_MIME = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif', '.svg': 'image/svg+xml' };

// ---------- Biểu đồ ----------
// Cú pháp trong câu trả lời của agent: ```chart {"type":"bar|line|pie","title":"..","labels":[..],"series":[{"name":"..","data":[..]}],"unit":".."} ```
function niceMax(v) {
  if (v <= 0) return 1;
  const p = 10 ** Math.floor(Math.log10(v)), f = v / p;
  return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * p;
}

export function chartSvg(spec) {
  const type = ['bar', 'line', 'pie'].includes(spec?.type) ? spec.type : 'bar';
  const labels = (Array.isArray(spec?.labels) ? spec.labels : []).slice(0, 30).map(String);
  const series = (Array.isArray(spec?.series) ? spec.series : []).slice(0, 6)
    .map((s, i) => ({ name: String(s?.name ?? `Chuỗi ${i + 1}`), data: (Array.isArray(s?.data) ? s.data : []).slice(0, labels.length).map(Number) }))
    .filter((s) => s.data.length && s.data.every(Number.isFinite));
  if (!labels.length || !series.length) return null;
  const W = 680, H = 340, unit = spec.unit ? ` ${esc(spec.unit)}` : '';
  const title = spec.title ? `<text x="${W / 2}" y="24" text-anchor="middle" font-size="16" font-weight="700" fill="#232834">${esc(spec.title)}</text>` : '';
  let body = '';
  if (type === 'pie') {
    const data = series[0].data.map((v) => Math.max(0, v)), total = data.reduce((a, b) => a + b, 0);
    if (!total) return null;
    const cx = 190, cy = 190, r = 120;
    let a0 = -Math.PI / 2;
    data.forEach((v, i) => {
      const a1 = a0 + (v / total) * 2 * Math.PI, large = a1 - a0 > Math.PI ? 1 : 0;
      const c = PALETTE[i % PALETTE.length];
      body += data.length === 1 || v === total
        ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${c}"/>`
        : `<path d="M${cx} ${cy} L${cx + r * Math.cos(a0)} ${cy + r * Math.sin(a0)} A${r} ${r} 0 ${large} 1 ${cx + r * Math.cos(a1)} ${cy + r * Math.sin(a1)}Z" fill="${c}" stroke="#fff" stroke-width="2"/>`;
      body += `<rect x="370" y="${70 + i * 24}" width="14" height="14" rx="3" fill="${c}"/><text x="392" y="${82 + i * 24}" font-size="13" fill="#3a4150">${esc(labels[i])}: ${fmt(v)}${unit} (${Math.round((v / total) * 100)}%)</text>`;
      a0 = a1;
    });
  } else {
    const L = 64, R = 20, T = 44, B = 56 + (series.length > 1 ? 18 : 0), pw = W - L - R, ph = H - T - B;
    const all = series.flatMap((s) => s.data), lo = Math.min(0, ...all), hi = niceMax(Math.max(...all, 0)), span = hi - lo || 1;
    const y = (v) => T + ph - ((v - lo) / span) * ph;
    for (let k = 0; k <= 5; k++) {
      const v = lo + (span * k) / 5, yy = y(v);
      body += `<line x1="${L}" y1="${yy}" x2="${W - R}" y2="${yy}" stroke="#e6e3da"/><text x="${L - 8}" y="${yy + 4}" text-anchor="end" font-size="11" fill="#6b7280">${fmt(v)}</text>`;
    }
    const step = pw / labels.length;
    labels.forEach((lb, i) => {
      const x = L + step * i + step / 2, t = lb.length > 12 ? lb.slice(0, 11) + '…' : lb;
      body += `<text x="${x}" y="${T + ph + 18}" text-anchor="middle" font-size="11" fill="#6b7280"${labels.length > 10 ? ` transform="rotate(-35 ${x} ${T + ph + 18})" text-anchor="end"` : ''}>${esc(t)}</text>`;
    });
    if (type === 'bar') {
      const gw = Math.min(step * 0.8, 70 * series.length), bw = gw / series.length;
      series.forEach((s, si) => s.data.forEach((v, i) => {
        const x = L + step * i + (step - gw) / 2 + bw * si, y0 = y(Math.max(v, 0)), h = Math.abs(y(v) - y(0));
        body += `<rect x="${x}" y="${y0}" width="${bw - 2}" height="${Math.max(h, 1)}" rx="3" fill="${PALETTE[si % PALETTE.length]}"/>`;
        if (labels.length <= 12 && series.length <= 2) body += `<text x="${x + (bw - 2) / 2}" y="${y0 - 5}" text-anchor="middle" font-size="11" fill="#3a4150">${fmt(v)}</text>`;
      }));
    } else {
      series.forEach((s, si) => {
        const c = PALETTE[si % PALETTE.length], pts = s.data.map((v, i) => [L + step * i + step / 2, y(v)]);
        body += `<polyline points="${pts.map((p) => p.join(',')).join(' ')}" fill="none" stroke="${c}" stroke-width="2.5" stroke-linejoin="round"/>`;
        pts.forEach(([px, py], i) => {
          body += `<circle cx="${px}" cy="${py}" r="3.5" fill="${c}"/>`;
          if (labels.length <= 12 && series.length === 1) body += `<text x="${px}" y="${py - 8}" text-anchor="middle" font-size="11" fill="#3a4150">${fmt(s.data[i])}</text>`;
        });
      });
    }
    if (series.length > 1) {
      let x = L;
      series.forEach((s, si) => { body += `<rect x="${x}" y="${H - 18}" width="12" height="12" rx="3" fill="${PALETTE[si % PALETTE.length]}"/><text x="${x + 17}" y="${H - 8}" font-size="12" fill="#3a4150">${esc(s.name)}</text>`; x += 40 + s.name.length * 7; });
    }
    if (spec.unit) body += `<text x="${L}" y="${T - 10}" font-size="11" fill="#6b7280">Đơn vị: ${esc(spec.unit)}</text>`;
  }
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="100%" style="max-width:${W}px;background:#fff;border:1px solid #e6e3da;border-radius:10px" font-family="system-ui,Segoe UI,Arial,sans-serif">${title}${body}</svg>`;
}

// ---------- Markdown rút gọn ----------
const inline = (s) => esc(s)
  .replace(/`([^`]+)`/g, '<code>$1</code>')
  .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
  .replace(/(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])/g, '<i>$1</i>')
  .replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+|[\w./-]+\.html)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');

const cells = (line) => line.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
const isSep = (line) => /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(line) && line.includes('-');

function tableHtml(head, rows) {
  const num = (v) => /^[-+]?[\d.,\s]+%?$/.test(v) && /\d/.test(v);
  return `<div class="tw"><table><thead><tr>${head.map((h) => `<th>${inline(h)}</th>`).join('')}</tr></thead><tbody>${rows.map((r) => `<tr>${head.map((_, i) => `<td${num(r[i] ?? '') ? ' class="n"' : ''}>${inline(r[i] ?? '')}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}

// images: Map<đường dẫn | tên file, dataURI>; dùng để thay ![alt](path). used: Set đánh dấu ảnh đã chèn trong thân báo cáo.
// ---------- Công thức toán (LaTeX -> MathML, dựng sẵn lúc tạo báo cáo) ----------
// Báo cáo mở trong khung sandbox (không chạy script) nên KaTeX phải chạy ở phía server. Dùng đầu ra MathML (không cần phông/CSS ngoài),
// trình duyệt hiện đại hiển thị trực tiếp. Hỗ trợ $$...$$, \[...\], $...$, \(...\). Chữ Việt trong \text{...} được giữ nguyên.
export function texHtml(tex, display = false) {
  const keep = [];
  const safe = String(tex).replace(/\\(text|mathrm|textbf|mbox)\{([^{}]*[^\x00-\x7F][^{}]*)\}/g, (_, cmd, body) => { keep.push(body); return `\\${cmd}{@@T${keep.length - 1}@@}`; });
  try {
    const out = katex.renderToString(safe.trim(), { output: 'mathml', displayMode: display, throwOnError: false, strict: 'ignore', trust: false });
    return out.replace(/@@T(\d+)@@/g, (_, n) => esc(keep[Number(n)] ?? ''));
  } catch {
    return `<code>${esc(tex)}</code>`;
  }
}

const MATH_RE = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<![\\$])\$(?![\s$])([^$\n]+?)(?<![\s\\])\$(?![\d$])/g;

// Thay công thức bằng ký hiệu giữ chỗ (tránh markdown làm hỏng _ * ...), dựng lại sau khi chuyển HTML. Bỏ qua khối mã ```...```.
function extractMath(text) {
  const store = [];
  const parts = String(text ?? '').split(/(```[\s\S]*?```)/g);
  const done = parts.map((p, i) => (i % 2 ? p : p.replace(MATH_RE, (m, d1, d2, i1, i2) => {
    const display = d1 != null || d2 != null;
    store.push(texHtml(d1 ?? d2 ?? i1 ?? i2, display));
    return `@@M${store.length - 1}@@`;
  })));
  return { text: done.join(''), store };
}

export function mdHtml(text, images = new Map(), used = new Set()) {
  const { text: t, store } = extractMath(text);
  const html = mdHtmlRaw(t, images, used);
  return store.length ? html.replace(/@@M(\d+)@@/g, (_, n) => store[Number(n)] ?? '') : html;
}

function mdHtmlRaw(text, images = new Map(), used = new Set()) {
  const lines = String(text ?? '').replace(/\r/g, '').split('\n');
  const out = [];
  let para = [], list = null;
  const flush = () => { if (para.length) out.push(`<p>${para.map(inline).join('<br>')}</p>`); para = []; };
  const endList = () => { if (list) out.push(`</${list}>`); list = null; };
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    const fence = ln.match(/^\s*```\s*(\w*)/);
    if (fence) {
      flush(); endList();
      const buf = [];
      for (i++; i < lines.length && !/^\s*```/.test(lines[i]); i++) buf.push(lines[i]);
      if (fence[1].toLowerCase() === 'chart') {
        let svg = null;
        try { svg = chartSvg(JSON.parse(buf.join('\n'))); } catch { /* JSON sai: hiện như mã */ }
        out.push(svg ? `<figure class="chart">${svg}</figure>` : `<pre>${esc(buf.join('\n'))}</pre>`);
      } else if (fence[1].toLowerCase() === 'panel') out.push(`<aside class="panel-hi">${mdHtmlRaw(buf.join('\n'), images, used)}</aside>`);
      else out.push(`<pre>${esc(buf.join('\n'))}</pre>`);
      continue;
    }
    if (ln.includes('|') && i + 1 < lines.length && isSep(lines[i + 1]) && !isSep(ln)) {
      flush(); endList();
      const head = cells(ln), rows = [];
      for (i += 2; i < lines.length && lines[i].includes('|') && lines[i].trim(); i++) rows.push(cells(lines[i]));
      i--;
      out.push(tableHtml(head, rows));
      continue;
    }
    const img = ln.match(/^\s*!\[([^\]]*)\]\(([^)]+)\)\s*$/);
    if (img) {
      flush(); endList();
      const key = img[2].trim(), uri = images.get(key) || images.get(path.basename(key));
      if (uri) { used.add(images.get(key) ? key : path.basename(key)); out.push(`<figure><img src="${uri}" alt="${esc(img[1])}"><figcaption>${esc(img[1])}</figcaption></figure>`); }
      else out.push(`<p><i>[Hình: ${esc(img[1] || key)}]</i></p>`);
      continue;
    }
    if (/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(ln)) { flush(); endList(); out.push('<hr>'); continue; }
    const h = ln.match(/^(#{1,6})\s+(.*)$/);
    if (h) { const lv = Math.min(h[1].length + 2, 6); flush(); endList(); out.push(`<h${lv}>${inline(h[2])}</h${lv}>`); continue; }
    const li = ln.match(/^\s*([-*•]|\d+[.)])\s+(.*)$/);
    if (li) {
      flush();
      const kind = /\d/.test(li[1]) ? 'ol' : 'ul';
      if (list !== kind) { endList(); out.push(`<${kind}>`); list = kind; }
      out.push(`<li>${inline(li[2])}</li>`);
      continue;
    }
    if (!ln.trim()) { flush(); endList(); continue; }
    endList(); para.push(ln);
  }
  flush(); endList();
  return out.join('\n');
}

// Rút gọn bảng/biểu đồ thành nhãn ngắn để Quản Lí tổng hợp mà không tốn token cho dữ liệu chi tiết.
export function stripData(text) {
  return String(text ?? '')
    .replace(/```chart\s*([\s\S]*?)```/gi, (_, j) => { try { return `[biểu đồ: ${JSON.parse(j).title || 'không tên'}]`; } catch { return '[biểu đồ]'; } })
    .replace(/```panel\s*([\s\S]*?)```/gi, '[bảng tiêu chí đánh giá content]')
    .replace(/(^\|.*\|\s*\n){2,}/gm, '[bảng dữ liệu]\n');
}

// ---------- Ảnh / tệp đính kèm ----------
async function imageUri(file) {
  const ext = path.extname(file).toLowerCase();
  if (!IMG_MIME[ext]) return null;
  let st; try { st = fs.statSync(file); } catch { return null; }
  if (!st.isFile() || st.size > 30 * 1024 * 1024) return null;
  if (ext === '.svg' || ext === '.gif') return st.size <= 1024 * 1024 ? `data:${IMG_MIME[ext]};base64,${fs.readFileSync(file).toString('base64')}` : null;
  try {
    const sharp = (await import('sharp')).default;
    const png = ext === '.png';
    const buf = await sharp(file).rotate().resize({ width: 1500, withoutEnlargement: true })[png ? 'png' : 'jpeg'](png ? {} : { quality: 85 }).toBuffer();
    return `data:${png ? 'image/png' : 'image/jpeg'};base64,${buf.toString('base64')}`;
  } catch {
    return st.size <= 3 * 1024 * 1024 ? `data:${IMG_MIME[ext]};base64,${fs.readFileSync(file).toString('base64')}` : null;
  }
}

export function csvRows(text) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true;
    else if (c === ',' || c === ';') { row.push(cur); cur = ''; }
    else if (c === '\n') { row.push(cur); rows.push(row); row = []; cur = ''; }
    else if (c !== '\r') cur += c;
  }
  if (cur || row.length) { row.push(cur); rows.push(row); }
  return rows.filter((r) => r.some((x) => x.trim()));
}

export const CSS = `:root{--ink:#1f2633;--mut:#6b7280;--line:#e4e1d8;--bg:#f4f3ee;--card:#fff;--acc:#2f5bea;--acc2:#eaf0ff;--ok:#1f9d6b;--bad:#d1373f}
*{box-sizing:border-box}body{font:15.5px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;max-width:960px;margin:0 auto;padding:24px 16px 56px;color:var(--ink);background:var(--bg)}
.rh{background:linear-gradient(135deg,#1c2b4a,#2f5bea);color:#fff;border-radius:16px;padding:22px 26px;margin-bottom:18px;box-shadow:0 8px 24px rgba(31,43,74,.18)}
.rh .kick{font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.75;margin-bottom:6px}
.rh h1{font-size:24px;line-height:1.3;margin:0 0 10px;font-weight:750}.rh .meta{color:rgba(255,255,255,.82);font-size:13px}.rh .meta b{color:#fff}
.rh .meta a{color:#cfe0ff}.paper{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:8px 28px 26px;box-shadow:0 2px 10px rgba(0,0,0,.04)}
h2{margin:0 0 4px}h3{font-size:19px;margin:30px 0 10px;padding:2px 0 2px 12px;border-left:4px solid var(--acc)}
h4{font-size:17px;margin:24px 0 8px;padding-left:10px;border-left:3px solid #9db4f5}h5{font-size:16px;margin:22px 0 8px;color:#243b7a}h6{font-size:14.5px;margin:16px 0 6px;color:#3a4a73}
p{margin:9px 0}ul,ol{margin:8px 0 8px;padding-left:24px}li{margin:4px 0}hr{border:0;border-top:1px dashed var(--line);margin:24px 0}
.meta{color:var(--mut);font-size:13px}.tw{overflow-x:auto;margin:12px 0;border:1px solid var(--line);border-radius:12px}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:14px}th,td{padding:8px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:#eef1fa;color:#243b7a;font-weight:650;white-space:nowrap}tbody tr:last-child td{border-bottom:0}td.n{text-align:right;font-variant-numeric:tabular-nums}
tbody tr:nth-child(even){background:#fafaf6}tbody tr:hover{background:#f1f5ff}
pre{white-space:pre-wrap;background:#f6f4ee;padding:12px;border-radius:10px;font-size:13px}code{background:#f0eee6;padding:1px 6px;border-radius:5px;font-size:.9em}
figure{margin:18px 0;text-align:center}figure img{max-width:100%;border-radius:12px;border:1px solid var(--line);box-shadow:0 2px 10px rgba(0,0,0,.06)}
figcaption{color:var(--mut);font-size:13px;margin-top:6px}figure.chart svg{max-width:100%;height:auto;box-shadow:0 2px 10px rgba(0,0,0,.05)}
.verdict,.sum{background:var(--acc2);border:1px solid #cddafc;border-left:5px solid var(--acc);border-radius:12px;padding:6px 18px 10px;margin:18px 0}
.verdict h3,.verdict h4,.verdict h5,.verdict h6{border:0;padding:0;margin:8px 0 4px;color:#1d3fb0}.verdict p{margin:6px 0}
.panel-hi{background:#0d2540;color:#fff;border:3px solid #ffc83d;border-radius:14px;padding:6px 20px 14px;margin:20px 0;box-shadow:0 6px 18px rgba(13,37,64,.3)}
.panel-hi h3,.panel-hi h4{color:#ffc83d;border:0;margin:12px 0 6px}.panel-hi p{margin:8px 0}.panel-hi strong,.panel-hi b{color:#ffd978}
.panel-hi table{background:#12345a;color:#fff}.panel-hi th{background:#1d4a7e;color:#fff;border-color:#3b6ba3}.panel-hi td{border-color:#3b6ba3}.panel-hi tbody tr:nth-child(even){background:#173f6a}
.st{font-size:11.5px;color:#fff;border-radius:99px;padding:1px 9px;vertical-align:middle}.st.done{background:var(--ok)}.st.failed{background:var(--bad)}.st.skipped{background:#8a8f98}.fail{color:#b42318}
details.tasks{margin-top:26px;font-size:13.5px}details.tasks summary{cursor:pointer;color:var(--mut)}
math{font-size:1.12em}math[display="block"]{display:block math;margin:.8em 0;padding:8px 12px;background:#f7f8fc;border-radius:8px;overflow-x:auto}
@media(max-width:600px){.paper{padding:4px 14px 18px}.rh{padding:16px}.rh h1{font-size:20px}}
@media print{body{background:#fff;padding:0}.paper,.rh{box-shadow:none}}`;

// Bọc phần "Kết luận…" thành khung nổi bật; <p>---</p> (markdown cũ) thành đường kẻ.
export function decorate(html) {
  return html.replace(/<p>\s*-{3,}\s*<\/p>/g, '<hr>')
    .replace(/(<h[3-6]>(?:<b>)?Kết luận[^<]*(?:<\/b>)?<\/h[3-6]>)([\s\S]*?)(?=<h[3-6]>|<hr>|<\/main>|$)/g, '<section class="verdict">$1$2</section>');
}

export function pageShell({ title, command, when, links = '', body }) {
  return `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title || 'Báo cáo')}</title>
<style>${CSS}</style>
<header class="rh"><div class="kick">Báo cáo</div><h1>${esc(title || 'Báo cáo gửi CEO')}</h1><div class="meta"><b>Lệnh:</b> ${esc(command)} &nbsp;·&nbsp; ${esc(when)}${links ? `<br>${links}` : ''}</div></header>
<main class="paper">
${decorate(body)}
</main>`;
}

// Trang HTML cho file markdown trong reports/ (bảng, biểu đồ ```chart, danh sách).
export function mdPage(title, text) {
  return pageShell({ title, command: 'Tài liệu markdown', when: '', body: mdHtml(text) });
}

// Ảnh biểu đồ do công cụ phân tích tạo (thư mục tạm, không nằm trong reports/): nhận ra từ đường dẫn xuất hiện trong lời agent rồi nhúng thẳng vào báo cáo.
export const CHART_DIR = path.join(os.tmpdir(), 'mba-stock-charts');
const chartPaths = (text) => [...String(text ?? '').matchAll(/[^\s`()"'<>\[\]]+\.(?:png|jpe?g|webp)/gi)].map((m) => m[0])
  .filter((f) => { try { return fs.realpathSync(f).startsWith(fs.realpathSync(CHART_DIR) + path.sep); } catch { return false; } });

// ev: { text, tasks, details:[{agent,title,status,text}], artifacts:[đường dẫn file agent đã tạo] }
export async function buildReport(ev, command, when, title = '') {
  const images = new Map(), used = new Set(), attach = [], tables = [];
  const mentioned = [ev.text, ...(ev.details || []).map((d) => d.text)].flatMap(chartPaths);
  for (const f of [...new Set([...(ev.artifacts || []), ...mentioned])]) {
    const ext = path.extname(f).toLowerCase();
    if (IMG_MIME[ext]) { const uri = await imageUri(f); if (uri) { images.set(f, uri); images.set(path.basename(f), uri); attach.push({ f, uri, hero: mentioned.includes(f) }); } }
    else if (ext === '.csv') { try { tables.push({ f, rows: csvRows(fs.readFileSync(f, 'utf8').replace(/^﻿/, '')).slice(0, 200) }); } catch { /* bỏ qua */ } }
  }
  // Dòng "file biểu đồ lưu tại <đường dẫn>" của agent chỉ là rác khi ảnh đã nhúng: bỏ đi (giữ dòng ![..](..) để chèn ảnh đúng chỗ).
  const clean = (t) => String(t ?? '').split('\n').filter((l) => !(chartPaths(l).length && !/^\s*!\[/.test(l))).join('\n');
  const failedSum = /^Không tổng hợp được/.test(ev.text || '') && (ev.details || []).some((d) => d.status === 'done');
  const single = (ev.details || []).length === 1 && ev.details[0].status === 'done';
  const detail = (ev.details || []).map((d) => `${single ? '' : `<h3>${esc(d.agent)} <span class="st ${esc(d.status)}">${esc(d.status)}</span></h3><div class="meta">${esc(d.title)}</div>`}${
    d.status === 'done' ? mdHtml(clean(d.text), images, used) : `<p class="fail">${esc(d.text)}</p>`}`).join('\n');
  const summary = failedSum ? '' : mdHtml(clean(ev.text), images, used);
  const unused = (a) => !used.has(a.f) && !used.has(path.basename(a.f));
  const hero = attach.filter((a) => a.hero && unused(a)), left = attach.filter((a) => !a.hero && unused(a));
  const figs = (arr) => arr.map((a) => `<figure><img src="${a.uri}" alt="${esc(path.basename(a.f))}"></figure>`).join('');
  const files = figs(left)
    + tables.filter((t) => t.rows.length > 1).map((t) => `<div class="meta">${esc(t.f)}</div>${tableHtml(t.rows[0], t.rows.slice(1))}`).join('');
  const rows = (ev.tasks || []).map((x) => `<tr><td>${esc(x.agent)}</td><td>${esc(x.title)}</td><td>${esc(x.status)}</td></tr>`).join('');
  // Liên kết kèm theo (vd Dashboard content): href tính từ gốc web ("reports/…") nên đổi sang đường dẫn tương đối trong thư mục reports.
  const links = (ev.links || []).filter((l) => l?.href).map((l) => `<a href="${esc(String(l.href).replace(/^reports\//, ''))}">${esc(l.label || l.href)}</a>`).join(' &nbsp;·&nbsp; ');
  const body = `${summary ? `<div class="sum">${summary}</div>` : ''}
${hero.length ? `<h3>Biểu đồ</h3>${figs(hero)}` : ''}
${detail}
${files ? `<h3>Hình ảnh &amp; dữ liệu đính kèm</h3>${files}` : ''}
${rows && !single ? `<details class="tasks"><summary>Danh sách công việc (${(ev.tasks || []).length})</summary><div class="tw"><table><tr><th>Agent</th><th>Task</th><th>Trạng thái</th></tr>${rows}</table></div></details>` : ''}`;
  return pageShell({ title, command, when, links, body });
}
