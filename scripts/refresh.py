#!/usr/bin/env python3
"""Refresh the Apple reference files.

Downloads the four Apple pages and:
  * regenerates skills/app-store-guidelines/references/review-guidelines.md in place
    (fully automatic: the page is verbatim text with numbered rules), and
  * writes the plain text of the other three pages to scripts/raw/ so you can diff
    them against the hand-written screenshot-specs.md, app-preview-specs.md and
    asset-best-practices.md and update anything that changed.

Usage: python3 scripts/refresh.py
Needs only the standard library.
"""
import datetime
import html
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
REFS = ROOT / "skills" / "app-store-guidelines" / "references"
RAW = ROOT / "scripts" / "raw"

PAGES = {
    "guidelines": "https://developer.apple.com/app-store/review/guidelines/",
    "asset-best-practices": "https://developer.apple.com/app-store/asset-best-practices/",
    "screenshot-specifications": "https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications",
    "app-preview-specifications": "https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def to_text(page: str) -> str:
    """Crude HTML to Markdown: headings, links, list items, paragraphs."""
    s = re.sub(r"<(script|style|svg|noscript|nav|header|footer)[^>]*>.*?</\1>", "", page, flags=re.S | re.I)
    s = re.sub(r"<(h[1-6])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)[1]) + " ", s, flags=re.I)
    s = re.sub(
        r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        lambda m: f"[{re.sub('<[^>]+>', '', m.group(2)).strip()}]({m.group(1)})",
        s,
        flags=re.S | re.I,
    )
    s = re.sub(r"</t[dh]>", " | ", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "\n- ", s, flags=re.I)
    s = re.sub(r"<(p|div|br|tr|section)[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s


def absolute_links(s: str) -> str:
    s = re.sub(r"\]\((/[^)]*)\)", r"](https://developer.apple.com\1)", s)
    s = re.sub(r"\]\((#[^)]*)\)", r"](https://developer.apple.com/app-store/review/guidelines/\1)", s)
    return s


def guidelines_markdown(page: str, today: str) -> str:
    s = to_text(page)
    i = s.find("## Introduction")
    if i < 0:
        sys.exit("guidelines page: could not find '## Introduction'; the page layout changed")
    s = s[i:]
    j = s.find("### Developer Footer")
    if j > 0:
        s = s[:j]
    s = absolute_links(s)
    out = []
    for line in s.split("\n"):
        m = re.match(r"^### (.+)$", line)
        if m:
            out.append("## " + m.group(1))
            continue
        m = re.match(r"^- (\d+(?:\.\d+)+)\s*(.*)$", line)
        if m:
            num, rest = m.group(1), m.group(2).strip()
            depth = num.count(".")
            short = rest == "" or (len(rest) <= 48 and not rest.endswith((".", ":"))) or rest == "Intentionally omitted."
            if short:
                out.append("#" * (depth + 2) + " " + num + (" " + rest if rest else ""))
            else:
                out.append(f"**{num}** {rest}")
            continue
        out.append(line)
    s = "\n".join(out)
    s = re.sub(r"\n- \n\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    # Long titles that fell through as bold (4.7 today).
    s = re.sub(r"^\*\*(\d+\.\d+)\*\* ([A-Z][^.]{48,}[a-z])$", r"### \1 \2", s, flags=re.M)
    # The notarization icon is stripped by the converter.
    s = s.replace("Guidelines that include apply to", "Note: on the live page, guidelines marked with a notarization icon also apply to")
    for key in ("Timing", "Status Updates", "Expedite Requests", "Release Date", "Rejections", "Appeals", "Bug Fix Submissions"):
        s = s.replace(f"- {key}:", f"- **{key}:**")
    updated = re.search(r"Last Updated: \[([^\]]+)\]", s)
    updated = updated.group(1) if updated else "unknown"
    header = (
        "# App Store Review Guidelines\n\n"
        f"Source: https://developer.apple.com/app-store/review/guidelines/ (captured {today}; "
        f'page states "Last Updated: {updated}"). Verbatim text of Apple\'s guidelines, re-formatted as Markdown '
        "so the numbered rules can be found with grep. Always confirm against the live page before quoting a rule to Apple.\n\n"
    )
    s = s.replace("## Introduction", header + "## Introduction", 1)
    return s.strip() + "\n"


def main() -> None:
    today = datetime.date.today().isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    for name, url in PAGES.items():
        print(f"fetching {url}")
        page = fetch(url)
        if name == "guidelines":
            out = REFS / "review-guidelines.md"
            out.write_text(guidelines_markdown(page, today), encoding="utf-8")
            print(f"  wrote {out.relative_to(ROOT)}")
        else:
            text = to_text(page)
            k = text.find("\n# ")
            text = text[k:] if k >= 0 else text
            out = RAW / f"{name}.md"
            out.write_text(text, encoding="utf-8")
            print(f"  wrote {out.relative_to(ROOT)} (diff by hand against references/)")
    print("\nNow update the 'captured' date in SKILL.md, NOTICE and the three hand-written reference files if anything changed.")


if __name__ == "__main__":
    main()
