"""Build index.html from src/template.html and the files in data/.

Usage:
    python build.py                      # rebuild from data/
    python build.py path/to/testset.csv  # refresh the test cases first, then rebuild

No dependencies beyond the Python standard library.
"""
import csv
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data"

if len(sys.argv) > 1:
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    keep = ("id", "source_row", "input_summary", "difficulty", "notes")
    tests = [{k: r.get(k, "") for k in keep} for r in rows]
    (DATA / "tests.json").write_text(json.dumps(tests, ensure_ascii=False), encoding="utf-8")
    (DATA / "testset.csv").write_text(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Refreshed {len(tests)} test cases from {sys.argv[1]}")

template = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
template = template.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
head, body = template.split('<div class="wrap">', 1)
body = '<div class="wrap">' + body
body = (body.replace("__TESTS__", (DATA / "tests.json").read_text(encoding="utf-8").strip())
            .replace("__DOTSEU__", (DATA / "europe-dots.json").read_text(encoding="utf-8").strip())
            .replace("__DOTS__", (DATA / "world-dots.json").read_text(encoding="utf-8").strip()))

favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Ccircle cx='16' cy='16' r='13' fill='none' stroke='%23D3155C' stroke-width='3'/%3E"
           "%3Ccircle cx='16' cy='16' r='5' fill='%23D3155C'/%3E%3C/svg%3E")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Interactive run of a Solution Design v1: campaign localization with brand guardrails. AI Solutions Architect course, Meeting 4.">
<link rel="icon" href="{favicon}">
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"Wrote index.html ({len(html) // 1024} KB)")
