---
name: jamesboyko.com
description: A working collection index — every paper, package, course, and vignette is a record in a ruled index.
colors:
  paper: "#fbfbf9"
  paper-sunk: "#f4f4f0"
  ink: "#16181a"
  ink-muted: "#5b6165"
  rule: "#dcdcd6"
  rule-firm: "#b9bab3"
  accent: "#2e5d4e"
  accent-lift: "#3f7864"
  dark-paper: "#14161a"
  dark-paper-sunk: "#1b1e23"
  dark-ink: "#e8e7e1"
  dark-ink-muted: "#a2a8ac"
  dark-rule: "#2c3036"
  dark-rule-firm: "#444a52"
  dark-accent: "#7fc0a6"
  dark-accent-lift: "#9ad6bd"
typography:
  display:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(1.9rem, 1.4rem + 1.8vw, 2.6rem)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.021em"
  heading:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(1.6rem, 1.3rem + 1.1vw, 2.1rem)"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.014em"
  body:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "normal"
  lede:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  section:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "1.32rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.014em"
  title:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "1.08rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "normal"
  secondary:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "0.98rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  meta:
    fontFamily: "Literata, Georgia, 'Times New Roman', serif"
    fontSize: "0.92rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  name:
    fontFamily: "Archivo, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.08em"
  label:
    fontFamily: "Archivo, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.09em"
  tab:
    fontFamily: "Archivo, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.07em"
rounded:
  none: "0px"
spacing:
  hairline: "1px"
  xs: "0.35rem"
  sm: "0.6rem"
  md: "1.15rem"
  lg: "2rem"
  xl: "3.2rem"
  gutter: "2rem"
  gutter-narrow: "1.25rem"
components:
  tab:
    textColor: "{colors.ink-muted}"
    typography: "{typography.tab}"
    padding: "0.55rem 0"
    rounded: "{rounded.none}"
  tab-active:
    textColor: "{colors.accent}"
    typography: "{typography.tab}"
    padding: "0.55rem 0"
  holding-row:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "1.15rem 0"
    rounded: "{rounded.none}"
  holding-row-hover:
    backgroundColor: "{colors.paper-sunk}"
    textColor: "{colors.accent}"
  record-item:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "1.05rem 0"
    rounded: "{rounded.none}"
  figure:
    backgroundColor: "#ffffff"
    rounded: "{rounded.none}"
    width: "46rem"
---

# Design

## Overview

The site is a **collection index**, drawn from natural-history catalogues rather than from
faculty-page convention. Every unit of content — a paper, a package, a course, a vignette —
is an *accessioned record*: an identifier in a left column, a title, and its metadata, seated
on a hairline rule. The index is the interface.

It deliberately refuses three things the category ships by default: the headshot sidebar, the
"Welcome, I am…" opening paragraph, and the card grid. The homepage instead opens on the
holdings themselves, with live counts, so a method user goes straight to their row and a
review committee reads the size of the record without scrolling.

Visitor mode is **Read**. Comprehension and wayfinding outrank expression everywhere. The
restraint is a binding constraint from the site owner, recorded in `PRODUCT.md`: this is an
academic website, clean and simple, and quality shows up as typography, spacing, and hierarchy
done precisely — never as effects.

The system is built to absorb a future lab site (People, Join, News) without a redesign,
because a person is just another record in the same grammar. See `PRODUCT.md` → Planned Trajectory.

## Colors

Restrained: neutrals plus a single accent. Color never carries meaning on its own.

- **`paper` / `ink`** are the ground and text. Both are tinted, never pure white or pure black.
- **`accent` (`#2e5d4e`, cabinet green)** is the only chromatic value. It marks links, the
  active tab, and hover state — nothing else. It was chosen against the AI-default warm-cream
  + terracotta palette, and reads as institutional steel-cabinet green rather than decoration.
- **`rule`** divides records; **`rule-firm`** closes structural regions (masthead, footer,
  the top of a record list).
- **`paper-sunk`** is the only fill in the system, used solely for row hover.

A full dark scheme ships under `prefers-color-scheme: dark`, with the accent lightened to
`#7fc0a6` to hold contrast on the dark ground. Both schemes clear WCAG AA for body and
secondary text.

## Typography

Two families, each with one job.

- **Literata** — all reading matter: display name, headings, body, ledes, record titles. A
  workhorse reading serif, appropriate to a Read surface, chosen over the Playfair/Fraunces/
  Cormorant defaults.
- **Archivo** — all *labels*: tabs, uppercase section names, counts, years, metadata,
  colophon. Set small, uppercase, with wide tracking (`0.07`–`0.09em`).

The split is the system's central rule: **serif reads, sans labels.** If a piece of text names
or identifies something rather than being read as prose, it is Archivo.

Numerals in record years, counts, and volume/page details use `font-variant-numeric: tabular-nums`
so columns align down the index. Body measure is capped at `66ch` (`--measure`), ledes at `58ch`.

**The ramp is closed.** Every size on the site is a named role in the `typography` block:
`display` and `heading` (the two clamps), `section` for `h2`, `title` for `h3` and record
titles, `lede`, `body`, `secondary` for descriptions, `meta` for authors and venues, `name`
for index row names, `tab` for tabs, years, and captions, and `label` for footer labels and
the colophon. That is eleven steps and it is meant to be the whole set. Introducing a
twelfth literal size is a design-system change rather than a local tweak: reuse a role, or
add one here deliberately.

## Layout

- One centered column, `max-width: 62rem`, with `--gutter` of `2rem` (`1.25rem` under `40rem`).
- **Records are grids, not cards.** Publications use `5.5rem 1fr` (year, then content);
  software and vignettes use `9.5rem 1fr` (identifier, then content); the homepage index uses
  `minmax(9rem,12rem) 1fr auto` (name, description, count).
- Under `40rem` every record grid collapses to a single column and the homepage index drops to
  `1fr auto` with the description spanning both.
- Vertical rhythm: `3.2rem` above an `h2`, `1rem` below it — more space above a heading than
  below, throughout.
- **Known trap:** `.wrap` sets the `padding` shorthand at class specificity, so a bare element
  selector cannot add vertical padding to it. `main.wrap` carries `padding-block` for exactly
  this reason. Match that specificity when adding vertical space to a `.wrap` element.

## Elevation & Depth

**There is none, and that is the system.** No `box-shadow` anywhere. No `border-radius`
anywhere. No gradients, no glass, no blur.

Separation is achieved entirely by hairline rules and whitespace. The one non-rule surface
treatment is the `paper-sunk` hover fill on index rows. Figures take a `1px` `rule` border on a
white ground, the way a plate is mounted — not a shadowed card.

## Shapes

Right angles only; `rounded.none` is the sole radius token. The form language is ruled paper:
horizontal hairlines, aligned columns, and a `2px` accent underline seating the active tab on
the masthead rule, which is the one place a shape carries state.

## Components

- **Masthead** — name (an `h1` on the index, a link elsewhere), one uppercase metadata line,
  then tabs. Closed by a `rule-firm` bottom border that the active tab sits on.
- **Tabs** — generated from `site.nav` in `_config.yml`. Adding a page is a one-line config
  change; never hand-edit nav markup.
- **Holdings index** (homepage) — the signature component. A row per section: uppercase name,
  one-line description, and a live count computed from the data files. Counts must always be
  derived, never typed.
- **Record item** — the universal content unit. Identifier column, then title (a link when a
  URL exists, plain text otherwise), authors with the site owner's name in `ink` at weight 600
  while co-authors stay `ink-muted`, then venue in italic with tabular detail.
- **Figure** — bordered image plus an Archivo caption that states the finding, not the filename.
- **Footer** — a `dl` of contact records in an auto-fit grid, closed by a colophon line.

## Do's and Don'ts

**Do**

- Keep every list of things in the record grammar: identifier column, title, metadata, hairline.
- Derive all counts and lists from `_data/*.yml`. Publications specifically are generated from
  the CV's `refs.bib` by `tools/bib2publications.py` — regenerate, never hand-edit
  `_data/publications.yml`.
- Add new sections by adding a data file, a `site.nav` entry, and a loop.
- Use Archivo for anything that labels, Literata for anything that is read.
- State figure alt text as the finding the figure shows.

**Don't**

- Don't introduce cards, shadows, or rounded corners. The whole system is rules and space.
- Don't add a second accent colour, or use colour as the only signal for state.
- Don't add decorative motion. There is no animation in this system beyond instant state
  changes, and `prefers-reduced-motion` is already honoured.
- Don't add a headshot sidebar or a "Welcome, I am…" opener — those are the defaults this
  design was chosen against.
- Don't fabricate record content. Absent a real URL, render the name as plain text; the
  templates already handle it.
- Don't add lab scaffolding (empty People or Join pages) before the lab exists.
