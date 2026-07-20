"""Make the src-layout aura_export package importable without installation.

pytest inserts the test file's directory (tests/) into sys.path via rootdir
conventions, but the package lives in src/. Insert it here so
`from aura_export import ...` works in a bare checkout.
"""

import sys
from pathlib import Path

SRC = str(Path(__file__).resolve().parent.parent / "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
