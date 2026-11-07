#!/usr/bin/env python3
"""Sinh 06-formulas-index.yaml từ modules/*.yaml và kiểm tra toàn bộ skill.

Chạy (từ bất kỳ thư mục nào):  python3 tools/build_and_validate.py
Yêu cầu: Python 3 + PyYAML (pip install pyyaml). Không phụ thuộc đường dẫn tuyệt đối.
"""
import glob
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_MODULE_KEYS = ["id", "name_vi", "name_en", "purpose", "concepts", "formulas", "procedures"]
REQUIRED_FORMULA_KEYS = ["id", "name_vi", "expression_latex", "expression_python", "variables", "when_to_use", "why_it_works"]


def load(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    errors, index = [], []
    seen_ids = set()
    for path in sorted(glob.glob(os.path.join(ROOT, "modules", "*.yaml"))):
        name = os.path.basename(path)
        try:
            mod = load(path)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: YAML lỗi: {e}")
            continue
        for k in REQUIRED_MODULE_KEYS:
            if k not in mod:
                errors.append(f"{name}: thiếu khóa module '{k}'")
        for fm in mod.get("formulas") or []:
            for k in REQUIRED_FORMULA_KEYS:
                if k not in fm:
                    errors.append(f"{name}: công thức {fm.get('id')} thiếu '{k}'")
            fid = fm.get("id")
            if fid in seen_ids:
                errors.append(f"{name}: trùng id công thức {fid}")
            seen_ids.add(fid)
            index.append({
                "id": fid,
                "module": mod.get("id"),
                "name_vi": fm.get("name_vi"),
                "name_en": fm.get("name_en"),
                "expression_latex": fm.get("expression_latex"),
                "expression_python": fm.get("expression_python"),
                "excel": fm.get("excel"),
                "variables": [v.get("symbol") for v in fm.get("variables") or [] if isinstance(v, dict)],
                "when_to_use": fm.get("when_to_use"),
            })
    for top in ["00-README.yaml", "01-agent-profile.yaml", "02-decision-router.yaml",
                "03-playbooks.yaml", "04-report-templates.yaml", "05-glossary.yaml", "SCHEMA.yaml"]:
        p = os.path.join(ROOT, top)
        if not os.path.exists(p):
            errors.append(f"thiếu file {top}")
            continue
        try:
            load(p)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{top}: YAML lỗi: {e}")
    out = os.path.join(ROOT, "06-formulas-index.yaml")
    header = ("# 06-formulas-index.yaml — SINH TỰ ĐỘNG bởi tools/build_and_validate.py từ modules/*.yaml. Không sửa tay.\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.safe_dump({"total": len(index), "formulas": index}, f, allow_unicode=True,
                       sort_keys=False, width=120)
    print(f"Công thức: {len(index)} | Lỗi: {len(errors)}")
    for e in errors:
        print(" -", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
