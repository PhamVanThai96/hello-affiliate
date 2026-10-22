import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { CONFIG, LIVE } from './config.js';
import { complete, resolveAI } from './llm.js';
import { classify, planFor, routeGuide } from './routing.js';
import { stripData } from './report.js';
import { webSearch, webFetch } from './web.js';

// Danh sách agent đọc từ agents.json. Quản Lí (#manager) là agent điều phối; người dùng là CEO.
export const ROOMS = ['Ban điều hành', 'Phòng nghiên cứu', 'Phòng sáng tạo', 'Phòng kỹ thuật'];
const ROOM_CAPACITY = 3;
const FILE = path.join(path.dirname(fileURLToPath(import.meta.url)), 'agents.json');

const SKILL_EXT = /\.(md|markdown|txt)$/i;
const SKILL_MAX = 12000;
const skillPath = (f) => path.resolve(path.dirname(FILE), f.replace(/^~(?=$|[\\/])/, os.homedir()));
const skillCache = new Map();

// Nội dung "skill file" của agent ("file-skill" trong agents.json): bỏ phần YAML đầu file, cắt tối đa SKILL_MAX ký tự, đọc lại khi file đổi.
export function skillDoc(agent) {
  if (!agent.fileSkill) return '';
  const f = skillPath(agent.fileSkill);
  try {
    const mt = fs.statSync(f).mtimeMs, c = skillCache.get(f);
    if (c && c.mt === mt) return c.text;
    let t = fs.readFileSync(f, 'utf8').replace(/^\uFEFF/, '').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '').trim();
    if (t.length > SKILL_MAX) t = t.slice(0, SKILL_MAX) + '\n…(đã cắt bớt)';
    const text = `\n\n--- Skill file (${path.basename(f)}) ---\n${t}\n--- Hết skill file ---\n`;
    skillCache.set(f, { mt, text });
    return text;
  } catch (e) {
    if (!skillCache.has('!' + f)) { skillCache.set('!' + f, 1); console.warn(`[skill] #${agent.id}: không đọc được ${f}: ${e.code || e.message}`); }
    return '';
  }
}

function normalize(list, strict = false) {
  const fail = (m) => { throw new Error(m); };
  if (!Array.isArray(list) || !list.length) fail('"agents" phải là mảng có ít nhất 1 agent.');
  const ids = new Set(), perRoom = {};
  const agents = list.map((a, i) => {
    const id = String(a?.id ?? '');
    if (!/^[a-z][a-z0-9_]{0,19}$/.test(id)) fail(`agent #${i + 1}: id "${id}" không hợp lệ (chữ thường/số/_, bắt đầu bằng chữ, tối đa 20 ký tự).`);
    if (ids.has(id)) fail(`id "${id}" bị trùng.`);
    ids.add(id);
    const name = String(a.name ?? '').trim(), basePrompt = String(a.prompt ?? '').trim();
    if (!name || !basePrompt) fail(`agent "${id}" thiếu name hoặc prompt.`);
    const room = a.room || ROOMS[0];
    if (!ROOMS.includes(room)) fail(`agent "${id}": room "${room}" không có (chọn: ${ROOMS.join(', ')}).`);
    perRoom[room] = (perRoom[room] || 0) + 1;
    if (perRoom[room] > ROOM_CAPACITY) fail(`"${room}" tối đa ${ROOM_CAPACITY} agent.`);
    // canAsk: danh sách id đồng nghiệp được phép hỏi; [] = không được hỏi ai; bỏ trống = không giới hạn.
    const canAsk = Array.isArray(a.canAsk) ? [...new Set(a.canAsk.map(String).filter((x) => x && x !== id))] : undefined;
    const fileSkill = String(a['file-skill'] ?? a.fileSkill ?? '').trim();
    if (fileSkill) {
      if (!SKILL_EXT.test(fileSkill)) fail(`agent "${id}": file-skill phải là file .md, .markdown hoặc .txt.`);
      if (strict) {
        let st; try { st = fs.statSync(skillPath(fileSkill)); } catch { fail(`agent "${id}": không tìm thấy file-skill "${fileSkill}".`); }
        if (!st.isFile()) fail(`agent "${id}": file-skill "${fileSkill}" không phải là file.`);
      }
    }
    const skills = Array.isArray(a.skills) ? a.skills.map((x) => String(x).trim()).filter(Boolean) : [];
    return {
      id, name, role: String(a.role ?? '').trim(), room, skills, basePrompt, canAsk, fileSkill: fileSkill || undefined,
      color: /^#[0-9a-f]{6}$/i.test(a.color) ? a.color : '#8a8f98',
      prompt: basePrompt + (skills.length ? ` Kỹ năng của bạn: ${skills.join(', ')}.` : ''),
      provider: a.provider ? String(a.provider) : undefined, model: a.model ? String(a.model) : undefined,
    };
  });
  if (agents[0].id !== 'manager') fail('agent đầu tiên phải có id "manager" (agent điều phối).');
  return agents;
}

function readFileAgents() {
  try {
    return normalize(JSON.parse(fs.readFileSync(FILE, 'utf8')).agents);
  } catch (e) {
    throw new Error(`agents.json: ${e.message}`);
  }
}

// AGENTS và IDS được cập nhật tại chỗ để mọi module thấy thay đổi ngay, không cần khởi động lại.
export const AGENTS = readFileAgents();
export const IDS = AGENTS.map((a) => a.id);

export const rawAgents = () => AGENTS.map(({ id, name, role, room, color, skills, basePrompt, canAsk, fileSkill, provider, model }) =>
  ({ id, name, role, room, color, skills, canAsk, 'file-skill': fileSkill, prompt: basePrompt, provider, model }));

// Kiểm tra danh sách mới, ghi agents.json rồi áp dụng ngay. Sai thì ném lỗi và giữ nguyên danh sách cũ.
export function setAgents(list) {
  const next = normalize(list, true);
  const tmp = FILE + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify({ agents: next.map(({ id, name, role, room, color, skills, basePrompt, canAsk, fileSkill, provider, model }) =>
    ({ id, name, role, room, color, skills, canAsk, 'file-skill': fileSkill, prompt: basePrompt, provider, model })) }, null, 2) + '\n');
  fs.renameSync(tmp, FILE);
  AGENTS.splice(0, AGENTS.length, ...next);
  IDS.splice(0, IDS.length, ...next.map((a) => a.id));
}

// Hiển thị AI thực tế của từng agent (không chứa khoá API).
export const aiLabel = (agent) => { const r = resolveAI(agent); return `${r.provider}${r.via === 'cli' ? ' (CLI)' : ''}/${r.model || 'mặc định'}`; };

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const short = (s, n = 60) => (s.length > n ? s.slice(0, n - 1) + '…' : s);

// Kế hoạch theo quy trình trong workflows.json (không tốn token). Không khớp quy trình nào thì dùng chuỗi tra cứu tối thiểu rag → reviewer.
const FALLBACK = { id: 'general', name: 'Tổng quát', steps: ['rag', 'reviewer'] };
export function templatePlan(command) {
  const w = classify(command) || FALLBACK;
  const tasks = planFor(w, command, IDS);
  tasks.route = w.name;
  return tasks;
}

const MOCK = {
  secretary: (c) => `Đã ghi nhận yêu cầu "${short(c, 50)}", yêu cầu rõ ràng.`,
  rag: () => 'Top 3 nguồn liên quan đã được xếp hạng; nguồn #1 độ tin cậy 0.92.',
  analyst: () => 'Nhận định: doanh thu tăng đều, tháng 3 cao nhất; nên tập trung nguồn lực vào quý 2.\n\n| Tháng | Doanh thu (triệu) | Tăng trưởng |\n|---|---|---|\n| T1 | 120 | - |\n| T2 | 150 | 25% |\n| T3 | 180 | 20% |\n\n```chart\n{"type":"bar","title":"Doanh thu theo tháng (dữ liệu mẫu)","labels":["T1","T2","T3"],"series":[{"name":"Doanh thu","data":[120,150,180]}],"unit":"triệu"}\n```',
  designer: () => 'Đề xuất bố cục 2 cột, tông màu dịu, ưu tiên đọc nhanh.',
  content: () => 'Kịch bản TikTok 30s: hook 3s đầu, 4 cảnh, CTA cuối + caption Facebook 100 từ, 5 hashtag.',
  writer: () => 'Đã viết xong nội dung chính và tiêu đề.',
  dev: () => 'Đã triển khai chức năng chính, 3 module, sẵn sàng kiểm thử.',
  tester: () => 'Chạy 12 test: 12 đạt, 0 lỗi.',
  ops: () => 'Dịch vụ đã khởi động đủ, cleanup xác nhận. Sẵn sàng bàn giao.',
  reviewer: () => 'Đã duyệt. Kết quả đạt yêu cầu.',
  manager: () => 'Đã xử lý xong yêu cầu.',
};

// Ở chế độ mock, một số agent giả lập việc cần truy cập file hoặc hỏi đồng nghiệp.
const MOCK_ACCESS = {
  dev: { fn: 'listDir', path: '.', ok: (r) => `Thư mục nguồn có ${r.entries.length} file: ${r.entries.join(', ')}` },
};
const MOCK_CONSULT = {
  tester: { to: 'dev', q: 'Có chức năng nào chưa ổn định không?', a: 'Chưa có, nhưng nên test kỹ phần phân quyền.' },
};
const MOCK_ANSWER = (agent, q) => {
  for (const c of Object.values(MOCK_CONSULT)) if (c.to === agent.id && c.q === q) return c.a;
  return 'Đã nhận câu hỏi, tôi sẽ phản hồi chi tiết sau.';
};

const toolDefs = (agent) => TOOL_DEFS.filter((t) => t.name !== 'ask_colleague' || agent.canAsk?.length !== 0)
  .map((t) => (t.name === 'ask_colleague' && agent.canAsk
    ? { ...t, description: `Hỏi nhanh một đồng nghiệp (chỉ khi thật cần). Được hỏi: ${agent.canAsk.join(', ')}.`, parameters: { ...t.parameters, properties: { ...t.parameters.properties, to: { type: 'string', enum: agent.canAsk } } } }
    : t));

const TOOL_DEFS = [
  { name: 'read_file', description: 'Đọc một file văn bản. Có thể cần người dùng cho phép.',
    parameters: { type: 'object', properties: { path: { type: 'string' } }, required: ['path'] } },
  { name: 'list_dir', description: 'Liệt kê một thư mục. Có thể cần người dùng cho phép.',
    parameters: { type: 'object', properties: { path: { type: 'string' } }, required: ['path'] } },
  { name: 'write_file', description: 'Tạo file mới hoặc ghi đè file văn bản (cần người dùng cho phép từng file; file cũ được sao lưu .bak). Chỉ dùng khi task yêu cầu tạo/sửa file; để sửa file, đọc nội dung bằng read_file rồi ghi lại toàn bộ nội dung mới.',
    parameters: { type: 'object', properties: { path: { type: 'string', description: 'Đường dẫn file (tuyệt đối hoặc tương đối SOURCE_DIR)' }, content: { type: 'string', description: 'Toàn bộ nội dung mới của file' } }, required: ['path', 'content'] } },
  { name: 'make_image', description: 'Tạo ảnh PNG/JPG/WEBP (banner, poster...) bằng cách ghép ảnh gốc + các lớp chữ/hình/ảnh phụ. Ảnh gốc được cắt vừa khung (cover). Cần người dùng cho phép đọc từng ảnh nguồn và ghi file đầu ra. Bạn không nhìn thấy nội dung ảnh, nên hãy bố cục theo kích thước khung và dùng lớp rect/gradient làm nền cho chữ dễ đọc. Toạ độ tính bằng pixel, gốc ở góc trên trái.',
    parameters: { type: 'object', properties: {
      output: { type: 'string', description: 'File đầu ra, đuôi .png/.jpg/.webp (tuyệt đối hoặc tương đối SOURCE_DIR)' },
      base: { type: 'string', description: 'Ảnh gốc làm nền (tuỳ chọn)' },
      width: { type: 'integer', description: 'Chiều rộng px (64-4096). Bỏ trống = theo ảnh gốc, hoặc 1080 nếu không có ảnh gốc' },
      height: { type: 'integer', description: 'Chiều cao px (64-4096)' },
      background: { type: 'string', description: 'Màu nền khi không có ảnh gốc, vd #1a1033' },
      layers: { type: 'array', description: 'Các lớp vẽ lần lượt từ dưới lên trên (tối đa 30)', items: { type: 'object', properties: {
        type: { type: 'string', enum: ['text', 'rect', 'circle', 'image'] },
        text: { type: 'string', description: 'text: nội dung, xuống dòng bằng \n' },
        x: { type: 'number' }, y: { type: 'number', description: 'text: y là đường chân chữ dòng đầu; circle: x,y là tâm' },
        size: { type: 'number', description: 'text: cỡ chữ px' }, fill: { type: 'string', description: 'màu, vd #ff7a00' },
        weight: { type: 'string', description: 'text: normal|bold' }, anchor: { type: 'string', enum: ['start', 'middle', 'end'], description: 'text: căn lề quanh x' },
        stroke: { type: 'string' }, strokeWidth: { type: 'number' }, opacity: { type: 'number', description: '0-1' }, rotate: { type: 'number' },
        w: { type: 'number' }, h: { type: 'number' }, r: { type: 'number', description: 'circle: bán kính' }, radius: { type: 'number', description: 'rect: bo góc' },
        fillTo: { type: 'string', description: 'rect: màu cuối của gradient dọc (từ fill xuống fillTo)' }, opacityTo: { type: 'number', description: 'rect: độ mờ cuối gradient' },
        path: { type: 'string', description: 'image: đường dẫn ảnh chèn (logo, sản phẩm)' },
      }, required: ['type'] } },
    }, required: ['output'] } },
  { name: 'make_docx', description: 'Tạo file Word .docx từ nội dung markdown: tiêu đề (#, ##, ###), đoạn văn, **đậm**/*nghiêng*, danh sách, bảng markdown (| a | b |), biểu đồ bằng khối ```chart {...}``` (tự vẽ thành hình) và ảnh bằng dòng ![chú thích](đường dẫn ảnh). Dùng khi người dùng yêu cầu file Word/.docx; nội dung phải là bản đầy đủ, không để trống. Cần người dùng cho phép ghi file (và đọc từng ảnh chèn vào).',
    parameters: { type: 'object', properties: {
      output: { type: 'string', description: 'File đầu ra, đuôi .docx (không chỉ định nơi lưu thì dùng reports/ten-file.docx)' },
      title: { type: 'string', description: 'Tiêu đề lớn đầu tài liệu (tuỳ chọn)' },
      content: { type: 'string', description: 'Toàn bộ nội dung tài liệu dạng markdown' },
    }, required: ['output', 'content'] } },
  { name: 'web_search', description: 'Tìm trên Internet để lấy thông tin/số liệu MỚI NHẤT (giá, tỷ giá, tin tức, sự kiện, thống kê...). Bắt buộc dùng cho mọi số liệu thay đổi theo thời gian; trả về tiêu đề, URL, đoạn trích.',
    parameters: { type: 'object', properties: { query: { type: 'string', description: 'Từ khoá, nên kèm năm/tháng hiện tại' } }, required: ['query'] } },
  { name: 'web_fetch', description: 'Tải nội dung văn bản của một trang web (URL từ web_search) để đọc số liệu chi tiết, kèm thời điểm lấy.',
    parameters: { type: 'object', properties: { url: { type: 'string' } }, required: ['url'] } },
  { name: 'ask_colleague', description: 'Hỏi nhanh một đồng nghiệp và nhận câu trả lời.',
    parameters: { type: 'object', properties: { to: { type: 'string', enum: IDS }, question: { type: 'string' } }, required: ['to', 'question'] } },
];

// Báo cáo tự nhúng bảng/biểu đồ/ảnh từ câu trả lời của agent (xem report.js).
const words = (t) => Math.round((t * 0.45) / 10) * 10;
const style = () => CONFIG.detail === 'brief'
  ? { work: 'phần văn bản tối đa 3 câu, không lặp lại đề bài.', sum: 'tối đa 5 câu.' }
  : {
      work: 'trình bày chi tiết, có cấu trúc bằng markdown (### tiêu đề, danh sách), không lặp lại đề bài. Gồm: (1) kết quả/kết luận chính trước; (2) giải thích cách làm, căn cứ, công thức hoặc số liệu dùng và vì sao chọn như vậy; (3) các giả định, hạn chế, rủi ro; (4) đề xuất bước tiếp theo nếu có. Việc đơn giản (hỏi nhanh một thông tin) thì gọn lại, chỉ đủ ý, không độn chữ.',
      sum: 'mở đầu bằng "### Kết luận" (2-3 câu trả lời thẳng vào yêu cầu), sau đó "### Diễn giải" giải thích đầy đủ lý do, căn cứ và cách các agent đi đến kết quả (có thể dùng danh sách), rồi "### Lưu ý & bước tiếp theo". Với yêu cầu đơn giản thì viết ngắn hơn.',
    };
const DATA_RULES = 'Báo cáo được dựng tự động từ câu trả lời của bạn nên hãy tự quyết định cần bảng/biểu đồ/ảnh nào: (1) số liệu từ 2 mục trở lên thì trình bày bằng bảng markdown (| Cột | Cột | rồi dòng |---|---|); (2) từ 3 giá trị cần so sánh/xu hướng/tỷ trọng thì thêm biểu đồ bằng khối ```chart {"type":"bar|line|pie","title":"…","labels":["…"],"series":[{"name":"…","data":[số thuần]}],"unit":"…"} ```; (3) ảnh tạo bằng make_image tự được chèn vào báo cáo. Bảng/biểu đồ không tính vào giới hạn số câu. Chỉ dùng số liệu thật từ yêu cầu, đồng nghiệp hoặc công cụ; không có số liệu thì không bịa để vẽ.';

const claude = ({ agent, system, user, handlers = {}, max = 400 }) => complete({ agent, system, user, tools: toolDefs(agent), handlers, max });

// Quản Lí tạo kế hoạch. Yêu cầu khớp quy trình thì dùng luôn (không gọi AI); không khớp mới nhờ AI chia task theo hướng dẫn quy trình.
export async function makePlan(command) {
  const w = classify(command);
  if (w) { await sleep(LIVE ? 0 : 600); return templatePlan(command); }
  if (!LIVE) { await sleep(1200); return templatePlan(command); }
  try {
    const text = await claude({
      agent: AGENTS[0],
      system: `${AGENTS[0].prompt}\nChia yêu cầu thành 1-5 task, mỗi agent tối đa 1 task, chỉ dùng agent thật sự cần, ưu tiên chuỗi ngắn nhất. ` +
        `Quy trình mẫu:\n${routeGuide()}\n` +
        `Chỉ trả về JSON dạng {"tasks":[{"id":"t1","title":"...","assignee":"<id>","dependsOn":[]}]}. ` +
        `Agent: ${AGENTS.slice(1).map((a) => `${a.id} (${a.role})`).join('; ')}. dependsOn chỉ trỏ tới task đứng trước.`,
      user: command, max: 600,
    });
    const tasks = JSON.parse(text.match(/\{[\s\S]*\}/)[0]).tasks;
    const seen = new Set(), who = new Set();
    const ok = Array.isArray(tasks) && tasks.length > 0 && tasks.length <= 6 && tasks.every((t) => {
      const valid = t.id && t.title && IDS.includes(t.assignee) && t.assignee !== 'manager' && !who.has(t.assignee)
        && Array.isArray(t.dependsOn) && t.dependsOn.every((d) => seen.has(d));
      seen.add(t.id); who.add(t.assignee);
      return valid;
    });
    if (ok) {
      const out = tasks.map(({ id, title, assignee, dependsOn }) => ({ id, title, assignee, dependsOn }));
      out.route = 'Quản Lí tự lập kế hoạch';
      return out;
    }
  } catch { /* dùng kế hoạch mặc định */ }
  return templatePlan(command);
}

// ctx: { command, task, inputs: [{from, text}], tools, ask }
const WORD_RE = /\b(docx|word)\b/i;
// Yêu cầu xuất Word: chỉ agent cuối chuỗi tạo file (đã có đủ kết quả của đồng nghiệp) để không tạo trùng.
const wantsWord = (ctx) => (!WORD_RE.test(ctx.command.normalize('NFD').replace(/[\u0300-\u036f]/g, '')) ? ''
  : ctx.isLast === false
    ? ' Yêu cầu có xuất file Word (.docx): đó là việc của agent cuối chuỗi, bạn chỉ cần hoàn thành phần nội dung của mình thật đầy đủ (bảng/biểu đồ dạng markdown) để agent sau đưa vào file.'
    : ' Yêu cầu có xuất file Word (.docx): bạn là agent cuối chuỗi nên hãy gọi make_docx với TOÀN BỘ nội dung báo cáo cuối (gộp kết quả đồng nghiệp, giữ nguyên bảng và khối ```chart, chèn ảnh đã tạo bằng ![chú thích](đường dẫn)), lưu vào reports/. Chỉ báo hoàn thành khi make_docx trả ok.');

// Mốc thời gian thật để AI không dùng số liệu cũ trong dữ liệu huấn luyện.
const nowText = () => {
  const d = new Date();
  return `Hôm nay là ${d.toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'numeric', year: 'numeric' })} (năm ${d.getFullYear()}). Dữ liệu huấn luyện của bạn đã cũ: với số liệu thay đổi theo thời gian (giá vàng, tỷ giá, chứng khoán, tin tức, thống kê...) PHẢI dùng web_search/web_fetch để lấy số liệu mới nhất, chỉ dùng số liệu của năm ${d.getFullYear()} làm mốc hiện tại, ghi rõ nguồn và ngày của từng số liệu; nếu không tìm được số liệu mới thì nói rõ, tuyệt đối không dùng số cũ rồi coi là hiện tại.`;
};

export async function work(agent, ctx) {
  if (LIVE) {
    const inputs = ctx.inputs.map((i) => `[${i.from}] ${i.text}`).join('\n') || '(chưa có)';
    return claude({
      agent,
      system: `${agent.prompt}${skillDoc(agent)} ${nowText()} Chỉ làm đúng phần việc thuộc vai trò của bạn; việc ngoài vai trò thì nói ngắn gọn cần agent nào, đừng tự làm. Trả lời tiếng Việt, ${style().work} Giữ phần văn bản trong khoảng ${words(CONFIG.workMax)} từ. ${DATA_RULES}${wantsWord(ctx)} Cần file/thư mục thì dùng công cụ (nếu bị từ chối thì báo lại, đừng thử lại). Chỉ ghi file (write_file), tạo ảnh (make_image) hoặc tạo file Word .docx (make_docx, viết toàn bộ nội dung markdown đầy đủ kèm bảng/biểu đồ cần thiết; không tự ghi .docx bằng write_file) khi task yêu cầu, báo rõ đường dẫn đã tạo/sửa. Báo cáo/tài liệu/ảnh đầu ra (.md, .csv, .html, .png...) mà người dùng không chỉ định nơi lưu thì lưu vào thư mục reports/ (vd reports/ten-bao-cao.md) để xem được trên trang báo cáo; không ghi file tài liệu vào thư mục gốc mã nguồn. Nếu công cụ báo lỗi hoặc bị từ chối thì nói rõ chưa làm được, tuyệt đối không báo đã hoàn thành. Không bịa đã làm điều gì mà bạn chưa thực sự làm. Chỉ dùng ask_colleague khi thiếu thông tin mà không thể tự xử lý.`,
      user: `Yêu cầu gốc của CEO: ${ctx.command}\nTask của bạn: ${ctx.task.title}\n\nKết quả từ đồng nghiệp:\n${inputs}${ctx.memory || ''}`,
      max: CONFIG.workMax,
      handlers: {
        read_file: (i) => ctx.tools.readFile(String(i.path)),
        list_dir: (i) => ctx.tools.listDir(String(i.path)),
        write_file: (i) => ctx.tools.writeFile(String(i.path ?? ''), i.content),
        make_image: (i) => ctx.tools.makeImage(i),
        make_docx: (i) => ctx.tools.makeDocx(i),
        web_search: async (i) => { ctx.think?.(`Tìm web: ${i.query}`); return webSearch(i.query); },
        web_fetch: async (i) => { ctx.think?.(`Đọc trang: ${i.url}`); return webFetch(i.url); },
        ask_colleague: async (i) => ({ answer: await ctx.ask(String(i.to), String(i.question)) }),
      },
    });
  }
  await sleep(1500 + Math.random() * 1500);
  let out = (MOCK[agent.id] || ((c, t) => `Đã hoàn thành: ${short(t, 60)}`))(ctx.command, ctx.task.title);
  const consult = IDS.includes(MOCK_CONSULT[agent.id]?.to) ? MOCK_CONSULT[agent.id] : null;
  if (consult) out = `Theo ${consult.to}: ${await ctx.ask(consult.to, consult.q)} ${out}`;
  // Giả lập: lệnh có dạng "tạo file <đường dẫn>" thì agent nhận việc ghi file đó (mọi agent đều có write_file).
  const wm = ctx.command.match(/(?:tạo|ghi|sửa)\s+file\s+(\S+)/i);
  if (wm) {
    const r = await ctx.tools.writeFile(wm[1], `Tạo bởi #${agent.id} (${agent.name})\nYêu cầu: ${ctx.command}\n`);
    out = r.error ? `${out} (Không ghi được ${wm[1]}: ${r.error})` : `Đã ${r.created ? 'tạo' : 'ghi đè'} ${r.path}. ${out}`;
  }
  const dm = ctx.command.match(/(?:tạo|xuất)\s+(?:file\s+)?(?:word|docx)\s+(\S+)/i);
  if (dm) {
    const r = await ctx.tools.makeDocx({ output: dm[1], title: 'Báo cáo mẫu', content: `### Kết luận\nĐây là tài liệu mẫu do #${agent.id} tạo.\n\n| Hạng mục | Giá trị |\n|---|---|\n| A | 10 |\n| B | 20 |\n\n\`\`\`chart\n{"type":"bar","title":"Mẫu","labels":["A","B"],"series":[{"name":"Giá trị","data":[10,20]}]}\n\`\`\`\n` });
    out = r.error ? `${out} (Không tạo được .docx: ${r.error})` : `Đã ${r.created ? 'tạo' : 'ghi đè'} tài liệu Word ${r.path}. ${out}`;
  }
  const im = ctx.command.match(/(?:tạo|vẽ)\s+ảnh\s+(\S+)/i);
  if (im) {
    const r = await ctx.tools.makeImage({ output: im[1], width: 1200, height: 628, background: '#241038', layers: [
      { type: 'rect', x: 0, y: 380, w: 1200, h: 248, fill: '#000000', fillTo: '#000000', opacity: 0, opacityTo: 0.7 },
      { type: 'circle', x: 1000, y: 180, r: 90, fill: '#ff7a00' },
      { type: 'text', text: 'Mùa Halloween\nƯu đãi ma mị', x: 60, y: 440, size: 72, fill: '#ffb347', stroke: '#2a0a3d', strokeWidth: 6 },
    ] });
    out = r.error ? `${out} (Không tạo được ảnh: ${r.error})` : `Đã ${r.created ? 'tạo' : 'ghi đè'} ảnh ${r.path} (${r.width}x${r.height}). ${out}`;
  }
  const acc = MOCK_ACCESS[agent.id];
  if (acc) {
    const r = await ctx.tools[acc.fn](acc.path);
    out = r.error ? `${out} (Không truy cập được ${acc.path}: ${r.error})` : `${acc.ok(r)}. ${out}`;
  }
  return out;
}

export async function answer(agent, question, command) {
  if (!LIVE) { await sleep(800); return MOCK_ANSWER(agent, question); }
  return claude({
    agent,
    system: `${agent.prompt}${skillDoc(agent)} Hôm nay là ${new Date().toLocaleDateString('vi-VN')}; không khẳng định số liệu thời sự từ trí nhớ. Trả lời tiếng Việt, tối đa 2 câu.`,
    user: `Bối cảnh: ${command}\nĐồng nghiệp hỏi: ${question}`, max: 250,
  });
}

// items: [{ agent, title, status, text }]
export async function summarize(command, items) {
  const lines = items.map((i) => `- [${i.status}] ${i.agent}: ${i.title} → ${stripData(i.text)}`).join('\n');
  if (!LIVE) {
    await sleep(800);
    const done = items.filter((i) => i.status === 'done').length;
    return `Yêu cầu "${short(command, 50)}": hoàn thành ${done}/${items.length} task.\n${lines}`;
  }
  return claude({
    agent: AGENTS[0],
    system: `${AGENTS[0].prompt} Hôm nay là ${new Date().toLocaleDateString('vi-VN')}. Viết báo cáo cuối cho CEO bằng tiếng Việt: ${style().sum} Giữ trong khoảng ${words(CONFIG.sumMax)} từ. Nêu rõ task nào chưa xong. Kết quả chi tiết (bảng, biểu đồ, ảnh của từng agent) được hệ thống tự đính kèm vào file báo cáo, nên chỉ tóm tắt và không chép lại dữ liệu; chỗ có [bảng dữ liệu]/[biểu đồ] nghĩa là đã có trong báo cáo.`,
    user: `Yêu cầu: ${command}\nKết quả các task:\n${lines}`, max: CONFIG.sumMax,
  });
}
