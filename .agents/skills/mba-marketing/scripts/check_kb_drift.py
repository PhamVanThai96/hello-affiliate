#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_kb_drift.py — Phát hiện tài liệu nguồn (raw source) đã thay đổi/mới thêm
so với lần chưng cất (distillation) gần nhất vào ai-distilled-kb/.

Cách hoạt động:
1. Quét mọi file .yaml/.json trong ai-distilled-kb/ có field "source_documents".
2. Tính SHA-256 hash của từng file nguồn được tham chiếu.
3. So sánh với manifest đã lưu (_kb_manifest.json). Báo cáo:
   - MODIFIED: file nguồn đã đổi nội dung kể từ lần distill gần nhất -> cần re-distill module tương ứng.
   - MISSING: file nguồn bị tham chiếu nhưng không còn tồn tại trên đĩa.
   - NEW_UNTRACKED: file .md mới trong thư mục raw-source nhưng CHƯA được domain nào tham chiếu
     (VD: thêm case study mới vào mba-quan-tri-doanh-nghiep/case-studies/ nhưng chưa distill).

Giới hạn quan trọng: Script này KHÔNG tự chạy nền/theo lịch (không có cron/daemon
trong môi trường này). Đây là công cụ ON-DEMAND — agent hoặc người dùng phải
chủ động chạy nó (đầu mỗi session, hoặc khi biết có tài liệu mới) rồi mới
tiến hành re-distill thủ công/bán tự động các module bị stale.

Usage:
    python3 check_kb_drift.py                  # In báo cáo drift
    python3 check_kb_drift.py --update-manifest # Sau khi đã re-distill xong, chốt baseline mới
"""

import hashlib
import json
import sys
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[4]  # .../hello-affiliate/
KB_DIR = REPO_ROOT / "ai-distilled-kb"
MANIFEST_PATH = KB_DIR / "_kb_manifest.json"

RAW_SOURCE_DIRS = [
    REPO_ROOT / "mba-quan-tri-doanh-nghiep",
    REPO_ROOT / "content-marketing",
    REPO_ROOT / "real-estate",
]
# Lưu ý: google-ads/ không quét .md vì raw source ở đây chủ yếu là .py/.json
# (đã tham chiếu trực tiếp trong affiliate_ads/01_campaign_and_landing_page_playbook.yaml).


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def load_module_files():
    """Trả về list các file distilled (.yaml/.json) trong ai-distilled-kb (trừ manifest/index)."""
    files = []
    for ext in ("*.yaml", "*.yml", "*.json"):
        files.extend(KB_DIR.rglob(ext))
    return [f for f in files if f.name not in ("_kb_manifest.json",)]


def extract_source_documents(module_path: Path):
    text = module_path.read_text(encoding="utf-8")
    if module_path.suffix == ".json":
        data = json.loads(text)
        return data.get("source_documents", [])
    else:
        if yaml is None:
            print("⚠️  PyYAML chưa cài (`pip install pyyaml`) — bỏ qua parse YAML chi tiết, dùng regex fallback.")
            import re
            block = re.search(r"source_documents:\s*\n((?:\s*-\s*.+\n?)+)", text)
            if not block:
                return []
            return [l.strip("- \n\"'") for l in block.group(1).splitlines() if l.strip()]
        data = yaml.safe_load(text)
        return data.get("source_documents", []) if isinstance(data, dict) else []


def build_current_state():
    """Trả về dict: {module_relpath: {source_relpath: hash}}"""
    state = {}
    for module_path in load_module_files():
        module_rel = str(module_path.relative_to(REPO_ROOT))
        try:
            sources = extract_source_documents(module_path)
        except Exception as e:
            print(f"⚠️  Không parse được {module_rel}: {e}")
            continue
        if not sources:
            continue
        # Path convention khác nhau giữa domain: mba_management yaml dùng path
        # đầy đủ từ repo root; content_marketing yaml dùng path tương đối so
        # với content-marketing/. Thử cả 2 cách resolve.
        source_hashes = {}
        for src_rel in sources:
            candidates = [REPO_ROOT / src_rel, REPO_ROOT / "content-marketing" / src_rel]
            resolved = next((c for c in candidates if c.exists()), None)
            if resolved:
                source_hashes[src_rel] = sha256_of(resolved)
            else:
                source_hashes[src_rel] = "MISSING"
        state[module_rel] = source_hashes
    return state


def find_untracked_raw_docs(all_tracked_sources):
    # Chuẩn hóa: content_marketing yaml dùng path tương đối so với content-marketing/,
    # mba_management yaml dùng path đầy đủ từ repo root. So khớp cả 2 dạng.
    normalized_tracked = set(all_tracked_sources)
    for src in all_tracked_sources:
        normalized_tracked.add(f"content-marketing/{src}")

    untracked = []
    for raw_dir in RAW_SOURCE_DIRS:
        if not raw_dir.exists():
            continue
        for md_file in raw_dir.rglob("*.md"):
            rel = str(md_file.relative_to(REPO_ROOT))
            if rel in normalized_tracked:
                continue
            if md_file.stat().st_size == 0:
                # File placeholder rỗng (VD READ.md stub cho domain chưa có nội dung)
                # -> không tính là drift, không có gì để distill.
                continue
            untracked.append(rel)
    return untracked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--update-manifest", action="store_true",
                        help="Chốt baseline mới sau khi đã re-distill xong")
    args = parser.parse_args()

    current_state = build_current_state()
    all_tracked = {src for hashes in current_state.values() for src in hashes}

    if args.update_manifest:
        MANIFEST_PATH.write_text(json.dumps(current_state, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"✅ Đã chốt baseline mới tại {MANIFEST_PATH}")
        return

    if not MANIFEST_PATH.exists():
        print("ℹ️  Chưa có manifest baseline. Chạy với --update-manifest để tạo lần đầu.")
        sys.exit(0)

    baseline = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    modified_modules = []
    missing_sources = []
    for module_rel, sources in current_state.items():
        old_sources = baseline.get(module_rel, {})
        for src_rel, cur_hash in sources.items():
            old_hash = old_sources.get(src_rel)
            if cur_hash == "MISSING":
                missing_sources.append((module_rel, src_rel))
            elif old_hash and old_hash != cur_hash:
                modified_modules.append((module_rel, src_rel))
            elif old_hash is None:
                modified_modules.append((module_rel, src_rel + " (nguồn mới thêm vào module)"))

    untracked = find_untracked_raw_docs(all_tracked)

    print("=" * 70)
    print("KB DRIFT REPORT")
    print("=" * 70)
    if modified_modules:
        print(f"\n🔴 STALE — {len(modified_modules)} nguồn đã đổi, cần re-distill module tương ứng:")
        for mod, src in modified_modules:
            print(f"   - {mod}  <-  {src}")
    if missing_sources:
        print(f"\n⚠️  MISSING — {len(missing_sources)} file nguồn bị tham chiếu nhưng không còn tồn tại:")
        for mod, src in missing_sources:
            print(f"   - {mod}  <-  {src}")
    if untracked:
        print(f"\n🆕 UNTRACKED — {len(untracked)} file .md mới/chưa được distill vào KB nào:")
        for u in untracked[:20]:
            print(f"   - {u}")
        if len(untracked) > 20:
            print(f"   ... và {len(untracked) - 20} file khác")
    if not modified_modules and not missing_sources and not untracked:
        print("\n✅ KB đang đồng bộ hoàn toàn với raw source. Không có drift.")
    print()


if __name__ == "__main__":
    main()
