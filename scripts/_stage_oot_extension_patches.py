"""Stage DuckDB's out-of-tree extension patch tooling at the repo root.

DuckDB resolves the extension patch script and the patch directory against
CMAKE_SOURCE_DIR. When duckdb is built as a subdirectory (as it is here), that
resolves to THIS repo's root, but the files actually live under external/duckdb.
Copy them into place before configuring so the httpfs APPLY_PATCHES step can find
`scripts/apply_extension_patches.py` and `.github/patches/extensions/httpfs/`.
"""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
duckdb = root / "external" / "duckdb"

shutil.copy(
    duckdb / "scripts" / "apply_extension_patches.py",
    root / "scripts",
)
shutil.copytree(
    duckdb / ".github" / "patches",
    root / ".github" / "patches",
    dirs_exist_ok=True,
)
print("Staged out-of-tree extension patch tooling at repo root")
