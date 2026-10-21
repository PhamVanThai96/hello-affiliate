import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { detect } from './cli.js';

const APP_DIR = path.dirname(fileURLToPath(import.meta.url));
const FILE = path.join(APP_DIR, 'config.json');

let raw = {};
try {
  raw = JSON.parse(fs.readFileSync(FILE, 'utf8'));
} catch (e) {
  if (e.code !== 'ENOENT') console.warn(`[config] Không đọc được config.json (${e.message}), dùng mặc định.`);
}

// Giá trị trong config.json được ưu tiên; để trống thì lấy từ biến môi trường.
const str = (v, env) => (typeof v === 'string' && v.trim() ? v.trim() : env || '');
const notes = [];

const PROVIDERS = {
  claude: { keyName: 'ANTHROPIC_API_KEY', envKeys: ['ANTHROPIC_API_KEY'], model: 'claude-sonnet-4-5' },
  gpt: { keyName: 'OPENAI_API_KEY', envKeys: ['OPENAI_API_KEY'], model: 'gpt-4o' },
  gemini: { keyName: 'GEMINI_API_KEY', envKeys: ['GEMINI_API_KEY', 'GOOGLE_API_KEY'], model: 'gemini-2.0-flash' },
};
const ALIAS = { anthropic: 'claude', openai: 'gpt', google: 'gemini' };

let provider = (str(raw.AI_PROVIDER, process.env.AI_PROVIDER) || 'claude').toLowerCase();
provider = ALIAS[provider] || provider;
if (!PROVIDERS[provider]) {
  notes.push(`AI_PROVIDER "${provider}" không hợp lệ (chọn claude, gpt hoặc gemini), dùng claude.`);
  provider = 'claude';
}
const P = PROVIDERS[provider];
const apiKey = str(raw[P.keyName], P.envKeys.map((k) => process.env[k]).find(Boolean));

// API: gọi trực tiếp bằng khoá. CLI: dùng claude/codex/gemini đã đăng nhập sẵn trên máy.
let connection = (str(raw.CONNECTION, process.env.CONNECTION) || 'API').toUpperCase();
if (connection !== 'API' && connection !== 'CLI') {
  notes.push(`CONNECTION "${connection}" không hợp lệ (chọn API hoặc CLI), dùng API.`);
  connection = 'API';
}
const CLI_DEFAULT = { claude: 'claude', gpt: 'codex', gemini: 'gemini' };
const cliCmd = {}, cliModels = {}, cliOk = {};
for (const name of Object.keys(PROVIDERS)) {
  cliCmd[name] = str(raw.CLI?.[name], '') || CLI_DEFAULT[name];
  cliModels[name] = str(raw.CLI_MODELS?.[name], '');
  cliOk[name] = connection === 'CLI' && detect(cliCmd[name]);
}
const model = connection === 'CLI' ? cliModels[provider] : (str(raw.MODELS?.[provider], '') || P.model);

let mode = (str(raw.MODE, process.env.MODE) || 'MOCK').toUpperCase();
if (mode !== 'MOCK' && mode !== 'REAL') {
  notes.push(`MODE "${mode}" không hợp lệ, dùng MOCK.`);
  mode = 'MOCK';
}
if (mode === 'REAL' && connection === 'API' && !apiKey) {
  notes.push(`MODE=REAL nhưng chưa có ${P.keyName} (provider ${provider}), dùng MOCK.`);
  mode = 'MOCK';
}
if (mode === 'REAL' && connection === 'CLI' && !cliOk[provider]) {
  notes.push(`MODE=REAL, CONNECTION=CLI nhưng không chạy được lệnh "${cliCmd[provider]}" (chưa cài hoặc chưa đăng nhập), dùng MOCK.`);
  mode = 'MOCK';
}

// Thư mục mã nguồn mà các agent làm việc; đường dẫn tương đối của agent được tính từ đây.
let sourceDir = str(raw.SOURCE_DIR, process.env.SOURCE_DIR);
if (sourceDir.startsWith('~')) sourceDir = path.join(os.homedir(), sourceDir.slice(1));
sourceDir = sourceDir ? path.resolve(sourceDir) : APP_DIR;
try {
  if (!fs.statSync(sourceDir).isDirectory()) throw new Error('không phải thư mục');
} catch {
  notes.push(`SOURCE_DIR "${sourceDir}" không tồn tại hoặc không phải thư mục, dùng thư mục của ứng dụng.`);
  sourceDir = APP_DIR;
}

const note = notes.join(' ');
if (note) console.warn(`[config] ${note}`);

// Khoá và model của từng provider, để agent có thể dùng AI khác mặc định.
const keys = {}, models = {};
for (const [name, p] of Object.entries(PROVIDERS)) {
  keys[name] = str(raw[p.keyName], p.envKeys.map((k) => process.env[k]).find(Boolean));
  models[name] = str(raw.MODELS?.[name], '') || p.model;
}

export const CONFIG = {
  connection, cliCmd, cliModels, cliOk, keys, models, providers: Object.keys(PROVIDERS), aliases: ALIAS,
  mode, note, provider, apiKey, model, sourceDir, appDir: APP_DIR,
  port: Number(raw.PORT || process.env.PORT) || 3000,
};
export const LIVE = mode === 'REAL';
