#!/usr/bin/env python3
"""SDL pre-commit path validation wrapper.

Calls the shared helper in ``.stibdedlom/lib/sdl_hooks.py``. Validates only
staged paths against the branch-inferred routing attestation; commit-message
trailer validation happens in the commit-msg hook via validate-commit.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

lib_dir = Path(__file__).resolve().parent.parent / "lib"
sys.path.insert(0, str(lib_dir))

from sdl_hooks import pre_commit_cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(pre_commit_cli())
