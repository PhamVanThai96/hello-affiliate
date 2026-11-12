// Gửi báo cáo hoàn tất sang bot Telegram: một tin tóm tắt + file báo cáo .html (mở bằng trình duyệt; công thức, bảng, biểu đồ nằm trong file).
// Thông tin bot lấy theo thứ tự: biến môi trường TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID → telegram.json cạnh server.js
// ({"bot_token":"...","chat_id":"...","enabled":true}) → file khóa của stock-analysist (dev/key/tele-bot-token.json, cùng định dạng, dùng chung bot).
// Tắt gửi: TELEGRAM_REPORTS=off hoặc "enabled": false trong telegram.json. Không bao giờ ghi token ra log.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { stripData } from './report.js';

const DIR = path.dirname(fileURLToPath(import.meta.url));
const FILES = [path.join(DIR, 'telegram.json'), path.join(DIR, '..', 'stock-analysist', 'dev', 'key', 'tele-bot-token.json')];
const API = 'https://api.telegram.org';

export function telegramConfig() {
  if (/^(off|0|false)$/i.test(process.env.TELEGRAM_REPORTS || '')) return null;
  let token = process.env.TELEGRAM_BOT_TOKEN, chat = process.env.TELEGRAM_CHAT_ID, enabled = true;
  for (const f of FILES) {
    if (token && chat) break;
    try {
      const c = JSON.parse(fs.readFileSync(f, 'utf8'));
      if (c.enabled === false) enabled = false;
      token ||= c.bot_token; chat ||= c.chat_id;
    } catch { /* không có file này */ }
  }
  return enabled && token && chat ? { token, chat: String(chat) } : null;
}

const plain = (s) => stripData(s).replace(/```[\s\S]*?```/g, '').replace(/^#{1,6}\s*/gm, '').replace(/\*\*|__|`/g, '').replace(/\$\$?|\\\(|\\\)|\\\[|\\\]/g, '').replace(/\n{3,}/g, '\n\n').trim();

async function call(cfg, method, body) {
  const r = await fetch(`${API}/bot${cfg.token}/${method}`, { method: 'POST', body });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.ok) throw new Error(`Telegram ${method}: ${j.description || r.status}`);
  return j;
}

// ev: sự kiện 'final' (text = tóm tắt của Quản Lí, title); file: đường dẫn tuyệt đối tới báo cáo .html đã lưu.
export async function sendReport({ title, text, file, link }) {
  const cfg = telegramConfig();
  if (!cfg) return false;
  const head = `📊 ${title || 'Báo cáo mới'}`;
  const body = plain(text).slice(0, 3000);
  const msg = new URLSearchParams({ chat_id: cfg.chat, text: `${head}\n\n${body}${link ? `\n\n${link}` : ''}`.slice(0, 4096), disable_web_page_preview: 'true' });
  await call(cfg, 'sendMessage', msg);
  if (file && fs.existsSync(file) && fs.statSync(file).size <= 49 * 1024 * 1024) {
    const form = new FormData();
    form.append('chat_id', cfg.chat);
    form.append('caption', head.slice(0, 1000));
    form.append('document', new Blob([fs.readFileSync(file)], { type: 'text/html' }), path.basename(file));
    await call(cfg, 'sendDocument', form);
  }
  return true;
}
