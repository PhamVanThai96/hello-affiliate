#!/usr/bin/env python3
"""
Chuyển bộ skill "finance-agent-skill" (mba-quan-tri-doanh-nghiep/3-financial-management/finance-agent-skill)
sang định dạng skill của office (skills/*.yaml, xem skills.js) cho agent `financial_expert`.

Vì sao phải chuyển đổi: bộ gốc ~1 MB YAML (11 module, 286 công thức, 85 thuật ngữ…) — không thể nhét vào prompt.
Office nạp skill theo 2 cách, nên file đầu ra chia như sau:
  - finance-00-core.yaml      LUÔN nạp vào prompt (≤ ~6000 ký tự): vai trò, nguyên tắc, quy trình trả lời, bảng định tuyến câu hỏi → module.
  - finance-mNN-*.yaml        nạp THEO NGỮ CẢNH (khoá `when` lấy từ bộ định tuyến): phần tổng quan module liên quan.
  - finance-playbooks / report-templates / glossary / formulas-index / readme
                              chỉ tra cứu (khoá `when` không bao giờ khớp): agent gọi công cụ `skill_search`.
Mọi khoá/mục của bộ gốc đều thành một "section" tra cứu được (không bỏ sót). Bộ gốc vẫn là nguồn chính: sửa ở đó rồi chạy lại script này.

Chạy:  python3 scripts/import_finance_skill.py [thư_mục_bộ_skill]   (cần pyyaml)
"""
import json, os, re, sys, unicodedata, glob
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'skills')
DEFAULT_SRC = os.path.join(HERE, '..', '..', 'mba-quan-tri-doanh-nghiep', '3-financial-management', 'finance-agent-skill')
SRC = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC)
AGENT = 'financial_expert'
SEARCH_ONLY = ['__chi_tra_cuu_bang_skill_search__']   # từ khoá không bao giờ khớp → skill chỉ tra cứu, không nạp vào prompt
CORE_BODY_MAX = 5800                                   # skills.js cắt phần nạp prompt ở 6000 ký tự/file


def plain(s):
    s = unicodedata.normalize('NFD', str(s).lower().replace('đ', 'd'))
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def clip(s, n):
    s = re.sub(r'\b\d\d-[\w-]+\.yaml\b', 'chỉ mục công thức (skill_search)', re.sub(r'\s+', ' ', str(s))).strip()
    return s if len(s) <= n else s[: n - 1] + '…'


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(str, lambda d, v: d.represent_scalar('tag:yaml.org,2002:str', v, style='|') if '\n' in v else d.represent_scalar('tag:yaml.org,2002:str', v))


def render(v):
    """Dữ liệu → văn bản YAML dễ đọc (giữ nguyên mọi trường)."""
    if isinstance(v, str):
        return v.strip()
    return yaml.dump(v, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False).strip()


NAME_KEYS = ('name_vi', 'term_vi', 'title', 'name', 'question', 'term', 'symbol', 'label', 'id')


def title_of(item, fallback):
    if isinstance(item, dict):
        for k in NAME_KEYS:
            if item.get(k) and isinstance(item[k], (str, int, float)):
                t = str(item[k]).strip()
                if k != 'id' and item.get('id') and str(item['id']) not in t:
                    t = f"{item['id']} — {t}"
                return clip(t, 140)
        for v in item.values():
            if isinstance(v, str) and v.strip():
                return clip(v, 100)
    elif isinstance(item, str) and item.strip():
        return clip(item, 100)
    return fallback


def tags_of(*parts, extra=()):
    words = []
    for p in list(parts) + list(extra):
        for w in re.split(r'[^\wÀ-ỹ]+', str(p or '')):
            w = w.strip('_')
            if len(w) >= 2 and w.lower() not in words:
                words.append(w.lower())
    return words[:12]


def slug(s, i):
    s = re.sub(r'[^a-z0-9]+', '-', plain(s)).strip('-')[:48]
    return f'{s or "muc"}-{i}'


def section(sid, title, text, tags=()):
    return {'id': sid, 'title': title, 'tags': list(tags), 'text': render(text).strip() if not isinstance(text, str) else text.strip()}


# ---------------------------------------------------------------- ghi file skill (định dạng skills.js / yamlmini.js)
def q(s):
    return json.dumps(str(s), ensure_ascii=False)


def flow(items):
    return '[' + ', '.join(q(x) for x in items) + ']'


def write_skill(name, sid, title, summary, sections, when=None, order=50, extra_agents=(), body_max=None):
    lines = [f'id: {sid}', f'title: {q(title)}', f'summary: {q(clip(summary, 300))}', f'agents: {flow([AGENT, *extra_agents])}', f'order: {order}']
    if when:
        lines.append(f'when: {flow(when)}')
    if body_max:
        lines.append(f'body_max: {int(body_max)}')
    lines.append('sections:')
    n = 0
    for s in sections:
        text = s['text'].replace('\r', '').rstrip()
        if not text:
            continue
        n += 1
        lines += [f'  - id: {q(s["id"])}', f'    title: {q(s["title"])}', f'    tags: {flow(s["tags"])}', '    text: |-']
        lines += [('      ' + ln.rstrip()) if ln.strip() else '' for ln in text.split('\n')]
    path = os.path.join(OUT, name)
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return n, os.path.getsize(path)


def load(rel):
    return yaml.safe_load(open(os.path.join(SRC, rel), encoding='utf-8'))


# ---------------------------------------------------------------- đọc bộ gốc
readme, profile, router = load('00-README.yaml'), load('01-agent-profile.yaml'), load('02-decision-router.yaml')
playbooks, templates, glossary, findex = load('03-playbooks.yaml'), load('04-report-templates.yaml'), load('05-glossary.yaml'), load('06-formulas-index.yaml')
modules = [load(os.path.relpath(f, SRC)) for f in sorted(glob.glob(os.path.join(SRC, 'modules', 'm*.yaml')))]
version = (readme.get('skill') or {}).get('version', '')
stats, total_sections = [], 0

# ---------------------------------------------------------------- 1) CORE (luôn nạp)
routes = router.get('routes', [])
mod_name = {m['id']: m.get('name_vi', m['id']) for m in modules}
principles = '\n'.join(f'- {clip(p if isinstance(p, str) else render(p), 115)}' for p in profile.get('principles', []))
calc = '\n'.join(f'- {clip(p if isinstance(p, str) else render(p), 100)}' for p in profile.get('calculation_discipline', []))
wf = '\n'.join(f'{i + 1}. {clip(p if isinstance(p, str) else render(p), 95)}' for i, p in enumerate(profile.get('workflow', [])))
labels = profile.get('confidence_labels', {})
label_txt = '; '.join(f'{k}: {clip(v, 55)}' for k, v in (labels.items() if isinstance(labels, dict) else []))
route_txt = '\n'.join(f"- {r.get('id')}: {', '.join(str(t) for t in (r.get('triggers') or [])[:4])} → module {', '.join(r.get('modules', []))}"
                      f"{' | playbook ' + r['playbook'] if r.get('playbook') else ''}" for r in routes)
mods_txt = '; '.join(f'{m["id"]} {m.get("name_vi", "")}' for m in modules)
how = (
    'Bộ kiến thức tài chính doanh nghiệp (11 module, '
    f'{findex.get("total", len(findex.get("formulas", [])))} công thức, thuật ngữ, playbook, mẫu báo cáo) KHÔNG nằm hết trong prompt: tra bằng công cụ skill_search.\n'
    '- Công thức: skill_search("m03_wacc") hoặc tên/biến ("WACC", "chi phí vốn chủ"). Playbook: skill_search("pb_wacc"). Mẫu báo cáo: skill_search("mẫu báo cáo ...").\n'
    '- Thuật ngữ: skill_search("<thuật ngữ>"). Ví dụ có lời giải/checklist/lỗi thường gặp của module cũng tra được bằng từ khoá của chủ đề.\n'
    '- Trước khi tính, tra công thức và điều kiện áp dụng; sau khi tính, kiểm tra lại bằng run_command (python) với số quan trọng.'
)
core_sections = [
    section('vai-tro-nguyen-tac', 'Vai trò, nguyên tắc và quy trình trả lời',
            f"Vai trò: {clip((profile.get('agent') or {}).get('mission', ''), 300)}\n\nNguyên tắc:\n{principles}\n\nKỷ luật tính toán:\n{calc}\n\nQuy trình trả lời:\n{wf}\n\nNhãn độ tin cậy: {label_txt}", ['vai', 'trò', 'nguyên', 'tắc']),
    section('dinh-tuyen', 'Định tuyến: câu hỏi → module → playbook', route_txt + '\n\nModule:\n' + mods_txt, ['định', 'tuyến', 'module']),
    section('cach-tra-cuu', 'Cách tra kiến thức (skill_search)', how, ['skill_search', 'tra', 'cứu']),
    section('pham-vi', 'Phạm vi và giới hạn', 'Trong phạm vi: ' + clip(render((profile.get('scope') or {}).get('in_scope', '')).replace('\n', ' '), 330) + '\nNgoài phạm vi: ' + clip(render((profile.get('scope') or {}).get('out_of_scope', '')).replace('\n', ' '), 330), ['phạm', 'vi', 'giới', 'hạn']),
]
# phần còn lại của hồ sơ (tra cứu được, không nạp prompt vì nằm sau mốc cắt)
for key, label in (('scope', 'Phạm vi'), ('response_style', 'Phong cách trả lời'), ('disclaimers', 'Tuyên bố miễn trừ'), ('known_data_caveats', 'Lưu ý dữ liệu'), ('principles', 'Nguyên tắc (đầy đủ)'),
                   ('calculation_discipline', 'Kỷ luật tính toán (đầy đủ)'), ('workflow', 'Quy trình (đầy đủ)'), ('confidence_labels', 'Nhãn độ tin cậy (đầy đủ)')):
    if profile.get(key):
        core_sections.append(section(f'hs-{key}', f'Hồ sơ agent — {label}', profile[key], tags_of(label)))
for key, label in (('chaining_rules', 'Quy tắc nối module'), ('clarifying_questions_default', 'Câu hỏi làm rõ mặc định')):
    if router.get(key):
        core_sections.append(section(f'rt-{key}', f'Định tuyến — {label}', router[key], tags_of(label)))
core_sections.append(section('rt-routes-day-du', 'Định tuyến — toàn bộ từ khoá từng nhóm câu hỏi', routes, ['định', 'tuyến', 'từ', 'khoá']))
for key in ('conventions_for_calculation', 'maintenance', 'how_to_bootstrap', 'load_order', 'file_index', 'skill'):
    if readme.get(key):
        core_sections.append(section(f'readme-{key}', f'README bộ skill — {key}', readme[key], tags_of(key)))
n, size = write_skill('finance-00-core.yaml', 'finance-00-core', 'Chuyên gia tài chính doanh nghiệp — vai trò, quy tắc, định tuyến',
                      f'Bộ skill finance-agent-skill v{version} cho agent {AGENT}: vai trò, nguyên tắc, định tuyến câu hỏi → module.', core_sections, order=5, body_max=6000)
body = '\n\n'.join(s['text'] for s in core_sections)[:6000]
stats.append(('finance-00-core.yaml', n, size, f'phần nạp prompt {len(body)} ký tự'))
total_sections += n
if len('\n\n'.join(s['text'] for s in core_sections[:4])) > 5900:
    print('CẢNH BÁO: 4 mục đầu của core vượt 5900 ký tự → bị cắt ở prompt', file=sys.stderr)

# ---------------------------------------------------------------- 2) MODULES (nạp theo ngữ cảnh)
primary = {}
for r in routes:
    if r.get('modules'):
        primary.setdefault(r['modules'][0], []).extend(str(t) for t in (r.get('triggers') or []))
LABEL = {'concepts': 'Khái niệm', 'formulas': 'Công thức', 'procedures': 'Quy trình', 'decision_rules': 'Quy tắc quyết định', 'benchmarks': 'Chuẩn so sánh', 'pitfalls': 'Lỗi thường gặp',
         'sme_vn_guidance': 'Lưu ý SME Việt Nam', 'case_lessons': 'Bài học case', 'worked_examples': 'Ví dụ có lời giải', 'practice_questions': 'Câu hỏi luyện tập', 'checklist': 'Checklist',
         'excel_google_sheets_templates': 'Mẫu Excel/Sheets'}
SCALARS = ('id', 'name_vi', 'name_en', 'source_file', 'purpose')
for m in modules:
    mid = m['id']
    fl = m.get('formulas', [])
    overview = [f"{m.get('name_vi', '')} ({m.get('name_en', '')}) — module {mid}", f"Mục đích: {clip(m.get('purpose', ''), 500)}"]
    if m.get('when_to_use'):
        overview.append('Dùng khi:\n' + '\n'.join(f'- {clip(x, 160)}' for x in m['when_to_use'][:8]))
    if m.get('prerequisites'):
        overview.append('Nên nắm trước: ' + render(m['prerequisites']).replace('\n', '; ')[:300])
    if m.get('related_modules'):
        overview.append('Module liên quan: ' + clip(render(m['related_modules']).replace('\n', ' '), 400))
    if fl:
        overview.append('Công thức (tra chi tiết bằng skill_search("<id>")):\n' + '\n'.join(f"- {f.get('id')}: {clip(f.get('name_vi', ''), 60)}" for f in fl))
    counts = ', '.join(f'{LABEL.get(k, k)} {len(v)}' for k, v in m.items() if isinstance(v, list) and k not in ('when_to_use', 'prerequisites', 'related_modules'))
    overview.append('Kho tra cứu của module: ' + counts + '. Tra bằng skill_search với từ khoá chủ đề (vd "ví dụ NPV", "lỗi thường gặp WACC").')
    secs = [section(f'{mid}-tong-quan', f'Tổng quan {mid}', '\n\n'.join(overview), tags_of(mid, m.get('name_vi'), m.get('name_en')))]
    for k, v in m.items():
        if k in SCALARS or k in ('when_to_use', 'prerequisites', 'related_modules'):
            continue
        label = LABEL.get(k, k.replace('_', ' ').capitalize())
        if isinstance(v, list):
            for i, it in enumerate(v):
                t = title_of(it, f'{label} {i + 1}')
                secs.append(section(f'{mid}-{k}-{i + 1}', f'{label}: {t}', it, tags_of(label, t, extra=[it.get('id', '')] if isinstance(it, dict) else [])))
        elif v:
            secs.append(section(f'{mid}-{k}', f'{label}', v, tags_of(label)))
    secs.append(section(f'{mid}-nguon', 'Nguồn', f"source_file: {m.get('source_file', '')}", ['nguồn']))
    when = []
    for t in primary.get(mid, []) + [m.get('name_vi', ''), m.get('name_en', '')]:
        raw_t = str(t).strip()
        p = plain(raw_t).strip()
        # bỏ từ khoá ngắn/chung ("vay", "lỗ"…); giữ viết tắt IN HOA 3 ký tự (NPV, IRR, EPS…)
        if (len(p) >= 4 or (len(p) == 3 and raw_t.isupper())) and p not in when:
            when.append(p)
    en = re.sub(r'[^a-z0-9]+', '-', plain(m.get('name_en') or m.get('name_vi') or mid)).strip('-').split('-')
    fname = f"finance-{mid}-{'-'.join(en[:4])}.yaml"
    ov_len = len(secs[0]['text'])
    n, size = write_skill(fname, f'finance-{mid}', f"Tài chính {mid}: {m.get('name_vi', '')}", clip(m.get('purpose', ''), 280), secs, when=when, order=20 + int(mid[1:]),
                          body_max=min(max(ov_len + 60, 1500), 3600))   # chỉ phần tổng quan vào prompt; chi tiết tra bằng skill_search
    stats.append((fname, n, size, f'{len(when)} từ khoá nạp theo ngữ cảnh'))
    total_sections += n

# ---------------------------------------------------------------- 3) TRA CỨU (playbook, mẫu báo cáo, thuật ngữ, chỉ mục công thức)
pb = playbooks.get('playbooks', {})
secs = [section(f'pb-{k}', f'Playbook {k} — {title_of(v, k)}'.replace(f'{k} — {k}', k), v, tags_of(k, title_of(v, ''), 'playbook')) for k, v in pb.items()]
n, size = write_skill('finance-playbooks.yaml', 'finance-playbooks', 'Tài chính — playbook (quy trình giải quyết từng loại vấn đề)', 'Các playbook pb_* theo bộ định tuyến.', secs, when=SEARCH_ONLY, order=60)
stats.append(('finance-playbooks.yaml', n, size, 'chỉ tra cứu')); total_sections += n

secs = [section('tpl-cau-truc-chung', 'Mẫu báo cáo — cấu trúc chung', templates.get('common_structure', []), ['mẫu', 'báo', 'cáo', 'cấu', 'trúc'])]
for k, v in (templates.get('templates') or {}).items():
    secs.append(section(f'tpl-{k}', f'Mẫu báo cáo {k} — {title_of(v, k)}', v, tags_of(k, title_of(v, ''), 'mẫu báo cáo')))
n, size = write_skill('finance-report-templates.yaml', 'finance-report-templates', 'Tài chính — mẫu báo cáo/bảng biểu', 'Cấu trúc chung và các mẫu báo cáo tài chính.', secs, when=SEARCH_ONLY, order=61)
stats.append(('finance-report-templates.yaml', n, size, 'chỉ tra cứu')); total_sections += n

secs = [section(slug(title_of(t, f'thuat-ngu'), i + 1), f"Thuật ngữ: {title_of(t, f'#{i + 1}')}", t, tags_of(title_of(t, ''), t.get('term_en', '') if isinstance(t, dict) else '', 'thuật ngữ')) for i, t in enumerate(glossary.get('terms', []))]
n, size = write_skill('finance-glossary.yaml', 'finance-glossary', 'Tài chính — thuật ngữ (Việt/Anh)', f'{len(secs)} thuật ngữ tài chính doanh nghiệp.', secs, when=SEARCH_ONLY, order=62)
stats.append(('finance-glossary.yaml', n, size, 'chỉ tra cứu')); total_sections += n

by_mod = {}
for f in findex.get('formulas', []):
    by_mod.setdefault(str(f.get('module') or f.get('id', 'm00')[:3]), []).append(f)
secs = []
for mid, lst in sorted(by_mod.items()):
    secs.append(section(f'idx-{mid}', f'Chỉ mục công thức {mid} — {mod_name.get(mid, "")}', '\n'.join('- ' + clip(render(f).replace('\n', ' | '), 230) for f in lst), tags_of('chỉ mục công thức', mid, mod_name.get(mid, ''))))
n, size = write_skill('finance-formulas-index.yaml', 'finance-formulas-index', 'Tài chính — chỉ mục công thức', f"{findex.get('total', len(findex.get('formulas', [])))} công thức (chi tiết ở từng module).", secs, when=SEARCH_ONLY, order=63)
stats.append(('finance-formulas-index.yaml', n, size, 'chỉ tra cứu')); total_sections += n

print(f'Nguồn: {SRC}\nĐích : {os.path.abspath(OUT)}')
for name, n, size, note in stats:
    print(f'  {name:46} {n:4} mục  {size / 1024:7.1f} KB  ({note})')
print(f'Tổng: {len(stats)} file, {total_sections} mục tra cứu.')
