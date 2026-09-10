from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    "boliglan.html",
    "forbrukslan.html",
    "omstartslan.html",
    "kredittkort.html",
    "sjekk/boliglan/index.html",
    "sjekk/forbrukslan/index.html",
    "sjekk/omstartslan/index.html",
    "sjekk/kredittkort/index.html",
]


def patch(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    before = text

    css_href = "../../design-v34.css?v=1" if "sjekk/" in path.as_posix() else "design-v34.css?v=1"
    css_tag = f'<link href="{css_href}" rel="stylesheet"/>'
    css_tag_alt = f'<link href="{css_href}" rel="stylesheet">'
    if css_tag not in text and css_tag_alt not in text:
        marker = "</head>"
        text = text.replace(marker, css_tag + marker, 1)

    if '<body class="' in text:
        start = text.index('<body class="') + len('<body class="')
        end = text.index('"', start)
        classes = text[start:end].split()
        if "design-v34" not in classes:
            classes.append("design-v34")
            text = text[:start] + " ".join(classes) + text[end:]
    elif "<body>" in text:
        text = text.replace("<body>", '<body class="design-v34">', 1)

    if "menu-btn" not in text and '<nav class="topnav">' in text:
        button = '<button aria-label="Åpne meny" class="menu-btn" onclick="document.querySelector(\'.topnav\').classList.toggle(\'open\')">☰</button>'
        text = text.replace('<nav class="topnav">', button + '<nav class="topnav">', 1)

    if text != before:
        path.write_text(text, encoding="utf-8")
        return True
    return False


changed = []
for rel in TARGETS:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"Missing design target: {rel}")
    if patch(path):
        changed.append(rel)

print(f"V34 design attachment complete: {len(changed)} files changed")
for item in changed:
    print(f"- {item}")
