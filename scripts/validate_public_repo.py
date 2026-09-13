"""Validate the generated Fatti Trust Centre repository using stdlib only."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "index.md": "/",
    "architecture.md": "/architecture/",
    "security.md": "/security/",
    "privacy.md": "/privacy/",
    "resilience.md": "/resilience/",
    "faq.md": "/faq/",
}
FORBIDDEN = [
    (re.compile(r"\b(?:SRC|CTL|GAP|EVD)-\d{3}\b"), "internal record identifier"),
    (re.compile(r"src-docs|sources/extracted", re.I), "private source path"),
    (re.compile(r"(?:password|secret|api[_-]?key)\s*[:=]\s*[^\s${][^\s]+", re.I), "possible credential"),
    (re.compile(r"\b(?:10\.\d{1,3}(?:\.\d{1,3}){2}|192\.168\.\d{1,3}\.\d{1,3})\b"), "private network address"),
]


def main() -> int:
    errors = []
    for name, permalink in PAGES.items():
        path = ROOT / name
        if not path.exists():
            errors.append(f"missing public page: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{name}: missing front matter")
        if f"permalink: {permalink}" not in text:
            errors.append(f"{name}: expected permalink {permalink}")

    required = [
        "README.md", "CONTRIBUTING.md", "_config.yml", "_layouts/default.html",
        "assets/css/style.css", "publication.json", ".github/CODEOWNERS",
        ".github/workflows/validate.yml", ".github/workflows/pages.yml",
    ]
    for name in required:
        if not (ROOT / name).exists():
            errors.append(f"missing required file: {name}")

    publication = ROOT / "publication.json"
    try:
        data = json.loads(publication.read_text(encoding="utf-8"))
        for key in ("source", "source_commit", "published_at", "method"):
            if not data.get(key):
                errors.append(f"publication.json: missing {key}")
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"publication.json: {exc}")

    scan_ext = {".md", ".html", ".yml", ".yaml", ".json", ".txt", ".css"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in scan_ext:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for pattern, label in FORBIDDEN:
            if pattern.search(text):
                errors.append(f"{rel}: {label}")
        for target in re.findall(r"href=[\"']([^\"']+)[\"']", text):
            if target.startswith(("http://", "https://", "#", "{{")):
                continue
            errors.append(f"{rel}: unmanaged local HTML link {target}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(PAGES)} public pages; required files present; disclosure patterns clear.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

