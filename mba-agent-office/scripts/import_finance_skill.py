#!/usr/bin/env python3
"""Giữ tương thích: chạy import_agent_skill.py cho bộ skill tài chính. Xem import_agent_skill.py (hỗ trợ finance | marketing | strategy)."""
import os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable, os.path.join(here, 'import_agent_skill.py'), 'finance', *sys.argv[1:]]))
