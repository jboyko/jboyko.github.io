# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Three confirmed audiences, all arriving with different jobs:

1. **Prospective graduate students and postdocs.** Deciding whether to reach out. They want to know what the research actually is, whether it's the kind of work they want to do, and how to make contact. Note: James is *not* currently running a named lab with members and is *not* advertising an active recruiting cycle — the site must serve this audience without claiming a lab that does not yet exist.
2. **Peer researchers and method users.** Often arriving from a paper, or from an R package (corHMM, hOUwie, dentist, mvh, SegmentR, phyloAMR). They want publications, software, and runnable vignettes with minimum friction. This is the highest-volume traffic and the most link-driven.
3. **Search, hiring, and review committees.** Tenure, grant, fellowship, and award reviewers scanning for credentials, output, and impact. They need the record legible and complete at a glance, and the CV one click away.

## Product Purpose

The personal academic site of James D. Boyko, Assistant Professor at the University of Michigan (Michigan Society of Fellows, Aug. 2024–present), Department of Ecology and Evolutionary Biology.

It exists to make his research program legible and his software findable. Success is: a peer finds the method and the vignette without asking; a prospective student understands the research program well enough to write a specific email; a committee can assemble the record without requesting anything.

## Positioning

The research program sits at a genuine intersection that a neighboring page could not truthfully copy: **classical phylogenetic comparative methods and modern deep learning, developed by the same person.** He builds statistical models of trait evolution (generalized hidden Markov models, hOUwie, joint ancestral state reconstruction) *and* applies neural networks to high-dimensional and non-standard phenotypic data (autoencoders for shape, SegmentR for image segmentation, LLMs for scientific research).

Two durable intellectual claims underpin the work:
- Traits do not evolve in isolation; ignoring dependence between them produces false correlations.
- Evolution does not proceed at one rate; ignoring rate heterogeneity produces wrong inferences.

These are linked, and that linkage is the through-line of the method development.

## Operating Context

- Visitors frequently arrive deep-linked from a paper's methods section or a package README, not through the homepage. Any page must stand alone.
- R is the primary delivery vehicle for the methods. Vignettes are pre-rendered HTML, already in `vignettes/`.
- The CV is a maintained PDF (`cv.pdf`, updated frequently — it is the most-touched file in the repo's git history). It is the canonical record; the site should not fork it into a competing source of truth that will drift.

## Capabilities and Constraints

- **Hosting: GitHub Pages**, custom domain `jamesboyko.com` via `CNAME`. This constrains the build: only the `github-pages` gem's allowed plugin set is available. No arbitrary Jekyll plugins, no server-side code, no build step outside what GitHub Pages runs.
- Current stack is Jekyll on the stock `jekyll-theme-minimal` remote theme. The theme is incumbent, not a commitment.
- Existing assets: research figures (`VAE.png`, `corhmm.png`, `houwie.png`, and others), a bio photo (`bio-photo.png`), a logo (`lgo.png`), and a large set of personal/field photos in `assets/images/`.
- Five pre-rendered vignette HTML files exist and must keep working at their current paths.

**Known defects in the incumbent site (confirmed, to be fixed):**
- `teaching.md` is a verbatim copy of `research.md` and contains no teaching content.
- `research.md` terminates mid-sentence ("It also").
- `index.md` links to `./research.md` and other raw `.md` paths, which do not resolve on the built site.

## Brand Commitments

- Name: **James Boyko** (publishes as Boyko, J. D.). Domain `jamesboyko.com`.
- Voice, as established by the incumbent copy and to be preserved: plain-spoken and explanatory. He explains statistical machinery in accessible language ("Autoencoders are computer models that find the most important features in complex data") without dumbing down the claim. Not promotional, not jargon-walled.
- Personal site, not lab-branded. No lab name, no team page, until one exists.
- **Restraint is binding, stated by the user directly.** This is an academic website: clean, basic, simple. It is not meant to be over the top or heavily stylized. Expressive visual ambition is out of scope here — no hero theatrics, no decorative motion, no ornament that isn't carrying information. Quality shows up as typography, spacing, and hierarchy done precisely, not as effects. Any future Impeccable command must read this as a ceiling, not a starting point to push past.

## Evidence on Hand

All drawn from `cv.pdf` (extracted; full text cached during this session). Real, citable, and not to be embellished:

- **20 published/accepted papers** (2017–2026), including first-author work in *Systematic Biology*, *PNAS*, *The American Naturalist*, *Methods in Ecology and Evolution*, *Evolution*, *New Phytologist*, and *Ecological Informatics*. **3 more under review**, **1 preprint** (arXiv:2311.04929, LLMs for scientific research).
- **7 software contributions:** phyloAMR, SegmentR, mvh, corHMM, dentist, hiSSE, OUwie. corHMM and hOUwie are the ones the user explicitly wants featured.
- **Teaching, real and specific:** Instructor, BIO202 Biological Data Analysis and Programming, UM (FA 2025). TA history at Arkansas and Toronto (2015–2022). Five instructor-led workshops/short courses (2024–2025), including Bergen and Boston University.
- **Awards:** UM/OpenAI Collaboration Grant ($50,000, 2025); Journal of Biogeography Innovation Award (2022); Outstanding Graduate Student Research Award (2021); Distinguished Doctoral Fellowship ($80,000, 2017–2021).
- **Service:** organizer of the SSE Symposium on AI in Evolutionary Biology (2025), BioBlend AI-Driven Biodiversity Monitoring (2024), MIDAS/Schmidt Futures AI in Science Colloquium (2023). Peer reviewer for 14 journals.
- **Talks:** 7 invited, 12 contributed.
- Education: Ph.D. Arkansas (Beaulieu), M.Sc. Toronto (Mahler), B.Sc. Toronto.
- Contact: jboyko@umich.edu; GitHub `jboyko`; Biological Sciences Building 5034, Ann Arbor.

**Absences future work must not fabricate:** there is no lab name, no roster of lab members, no active recruiting call, no testimonials, no press coverage, and no student outcomes. Do not invent a Google Scholar citation count or h-index — cite only what appears above unless the user supplies more.

## Planned Trajectory

Stated by the user during the first build: **this is a solo personal site now, but it must expand into a full faculty/lab website without a rebuild.** Design and architecture decisions are made against that future, not just today's content.

Anticipated future surfaces, to be structurally cheap to add and never faked in advance:
- **People / Lab roster** — members with photos, roles, and links.
- **Join / Openings** — an active recruiting path for grad students and postdocs.
- **News / Updates** — a dated stream.

Binding implications for implementation:
- Content lives in `_data/*.yml`, not hardcoded in markup. A new record type is a new data file plus a loop.
- Navigation is generated from `_config.yml`. Adding a page is a one-line config change, never a markup edit across templates.
- The visual grammar must treat a person the same way it treats a paper or a package: as a record in an index. This was tested against the direction at selection time and is the main reason the Collection Index survives the transition.
- Do not add lab scaffolding, placeholder members, or an empty "Join" page before the lab exists. Build the capacity, not the pretense.

## Product Principles

1. **The record is the argument.** For every audience, the persuasive content *is* the real work — papers, packages, vignettes. Design should present evidence, never substitute enthusiasm for it.
2. **Two-audience routing from the first screen.** A method user hunting a vignette and a committee scanning credentials should each see their path immediately, without reading the other's.
3. **Never fork the CV.** The PDF stays canonical. On-site listings are a navigable view of it, and where they'd drift, they defer to it.
4. **Explain, don't posture.** Preserve the accessible register of the incumbent copy. A first-year grad student should follow the research summaries; a reviewer should still find them precise.
5. **Deep links are entry points.** Every page carries enough orientation to work as someone's first and only page.

## Accessibility & Inclusion

No product-specific standard was established by the user. Default to the skill's baseline: WCAG AA contrast, keyboard-navigable, real semantic headings, and figure alt text that states the finding rather than naming the file.
