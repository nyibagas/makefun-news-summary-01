import os
import pathlib
import shutil

out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(pathlib.Path(__file__).resolve().parent / "summary.txt", out / "entry.txt")
