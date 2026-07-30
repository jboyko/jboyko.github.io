#!/usr/bin/env python3
"""Generate _data/publications.yml from the CV's refs.bib.

refs.bib is the single source of truth for the publication record. This script
derives the site's data file from it, so the list is never maintained twice.

Usage:
    python3 tools/bib2publications.py [path/to/refs.bib]

With no argument it reads the path in tools/bib-source.txt, which defaults to
the CV directory in Dropbox. Run it whenever refs.bib changes, then commit the
regenerated _data/publications.yml.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SOURCE_POINTER = os.path.join(HERE, "bib-source.txt")
OUT = os.path.join(REPO, "_data", "publications.yml")

# Order in which status groups are emitted, and the keyword that marks each.
STATUS_ORDER = ["published", "review", "preprint"]
KEYWORD_TO_STATUS = {
    "published": "published",
    "underreview": "review",
    "inreview": "review",
    "preprint": "preprint",
}

LATEX_CHARS = {
    r'{\"o}': "ö", r'{\"u}': "ü", r'{\"a}': "ä", r'{\"e}': "ë",
    r"{\'i}": "í", r"{\'e}": "é", r"{\'a}": "á", r"{\'o}": "ó", r"{\'u}": "ú",
    r"{\`e}": "è", r"{\`a}": "à",
    r"{\c c}": "ç", r"{\~a}": "ã", r"{\~n}": "ñ",
    r"{\ss}": "ß",
}


def strip_latex(text):
    """Turn a BibTeX field value into plain text."""
    for tex, char in LATEX_CHARS.items():
        text = text.replace(tex, char)
    # Accents written without enclosing braces, e.g. \'{i} or \"o
    text = re.sub(r"\\[\"'`^~]\{?(\w)\}?", r"\1", text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("--", "\u2013")          # en dash for page ranges
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_entries(bib):
    """Yield (entry_type, {field: value}) for each @entry in the file."""
    for match in re.finditer(r"@(\w+)\s*\{", bib):
        entry_type = match.group(1).lower()
        # Walk forward to the matching closing brace.
        depth, i = 1, match.end()
        while i < len(bib) and depth:
            if bib[i] == "{":
                depth += 1
            elif bib[i] == "}":
                depth -= 1
            i += 1
        body = bib[match.end():i - 1]

        # Drop the citation key, then split fields on top-level commas.
        body = body.split(",", 1)[1] if "," in body else ""
        fields, depth, current = {}, 0, ""
        for ch in body:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            if ch == "," and depth == 0:
                _add_field(fields, current)
                current = ""
            else:
                current += ch
        _add_field(fields, current)
        yield entry_type, fields


def _add_field(fields, chunk):
    if "=" not in chunk:
        return
    key, value = chunk.split("=", 1)
    key = key.strip().lower()
    value = value.strip().rstrip(",").strip()
    if value.startswith("{") and value.endswith("}"):
        value = value[1:-1]
    elif value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    if key and value:
        fields[key] = value


def format_author(raw):
    """Render one BibTeX author as `Last, F. M.`."""
    raw = raw.strip()
    if not raw:
        return ""

    # Protect braced multi-word surnames: {Rodrigues Ferreira de Melo}, Lilian
    braced = re.match(r"^\{([^}]*)\}\s*,\s*(.*)$", raw)
    if braced:
        last, first = braced.group(1), braced.group(2)
    elif "," in raw:
        last, first = [p.strip() for p in raw.split(",", 1)]
    else:
        # "James D. Boyko" — last token is the surname.
        parts = strip_latex(raw).split()
        if len(parts) == 1:
            return parts[0]
        last, first = parts[-1], " ".join(parts[:-1])

    last = strip_latex(last)
    initials = " ".join(
        _initial(p) for p in strip_latex(first).replace(".", " ").split() if p
    )
    return f"{last}, {initials}" if initials else last


def _initial(part):
    """`Jennifer` -> `J.`;  `I-Hsiu` -> `I.-H.` (hyphenated names keep both)."""
    return "-".join(f"{seg[0]}." for seg in part.split("-") if seg)


def format_authors(raw):
    people = [format_author(a) for a in re.split(r"\s+and\s+", raw) if a.strip()]
    if len(people) == 1:
        return people[0]
    if len(people) == 2:
        return f"{people[0]} and {people[1]}"
    return ", ".join(people[:-1]) + f", and {people[-1]}"


def build_detail(f):
    """Volume/issue/pages, rendered the way the CV does."""
    volume, number, pages = f.get("volume"), f.get("number"), f.get("pages")
    if volume in ("0", None) and number in ("0", None):
        volume = number = None
    if pages in ("000-000", None):
        pages = None

    bits = ""
    if volume:
        bits = volume
        if number:
            bits += f"({number})"
    if pages:
        bits = f"{bits}, {pages}" if bits else pages
    return strip_latex(bits) if bits else None


def yaml_quote(value):
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    if len(sys.argv) > 1:
        source = sys.argv[1]
    elif os.path.exists(SOURCE_POINTER):
        source = open(SOURCE_POINTER).read().strip()
    else:
        sys.exit("No refs.bib path given and tools/bib-source.txt is missing.")

    source = os.path.expanduser(source)
    if not os.path.exists(source):
        sys.exit(f"refs.bib not found at: {source}")

    with open(source, encoding="utf-8") as fh:
        bib = fh.read()

    records = []
    for entry_type, f in parse_entries(bib):
        keywords = f.get("keywords", "").lower().replace(" ", "")
        status = next(
            (KEYWORD_TO_STATUS[k] for k in KEYWORD_TO_STATUS if k in keywords),
            "published",
        )

        venue = f.get("journal") or f.get("booktitle")
        detail = build_detail(f)
        if not venue and f.get("howpublished"):
            # Preprints: "arXiv:2311.04929 [cs.CL]" -> venue arXiv, detail id
            hp = strip_latex(f["howpublished"])
            if ":" in hp:
                venue, detail = hp.split(":", 1)
                detail = detail.strip()
            else:
                venue = hp

        url = f.get("url") or f.get("URL")
        if not url and f.get("doi"):
            url = "https://doi.org/" + strip_latex(f["doi"])
        if not url and venue and venue.lower().startswith("arxiv") and detail:
            url = "https://arxiv.org/abs/" + detail.split()[0]

        records.append({
            "status": status,
            "year": int(re.sub(r"\D", "", f.get("year", "0")) or 0),
            "authors": format_authors(f.get("author", "")),
            "title": strip_latex(f.get("title", "")).rstrip("."),
            "venue": strip_latex(venue) if venue else "",
            "detail": detail,
            "url": strip_latex(url) if url else None,
        })

    records.sort(key=lambda r: (STATUS_ORDER.index(r["status"]), -r["year"],
                                r["authors"]))

    lines = [
        "# GENERATED FILE — DO NOT EDIT BY HAND.",
        "#",
        "# Source of truth is the CV's refs.bib. Regenerate with:",
        "#     python3 tools/bib2publications.py",
        "#",
        f"# {len(records)} records.",
        "",
    ]
    current_status = None
    for r in records:
        if r["status"] != current_status:
            current_status = r["status"]
            label = {"published": "PUBLISHED & ACCEPTED",
                     "review": "UNDER REVIEW",
                     "preprint": "PREPRINTS"}[current_status]
            lines.append(f"# {'-' * 8} {label}")
            lines.append("")
        lines.append(f"- status: {r['status']}")
        lines.append(f"  year: {r['year']}")
        lines.append(f"  authors: {yaml_quote(r['authors'])}")
        lines.append(f"  title: {yaml_quote(r['title'])}")
        lines.append(f"  venue: {yaml_quote(r['venue'])}")
        if r["detail"]:
            lines.append(f"  detail: {yaml_quote(r['detail'])}")
        if r["url"]:
            lines.append(f"  url: {yaml_quote(r['url'])}")
        lines.append("")

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines).rstrip() + "\n")

    counts = {s: sum(1 for r in records if r["status"] == s) for s in STATUS_ORDER}
    print(f"Wrote {OUT}")
    print("  " + "  ".join(f"{s}: {n}" for s, n in counts.items()))


if __name__ == "__main__":
    main()
