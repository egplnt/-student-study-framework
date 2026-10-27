# Changelog

All notable changes to this skill are documented here.

## 1.1.0 — 2026-10-27

**Scope: documentation rewrite for rigorous external distribution.** The framework's mechanisms, templates, and script are unchanged. This release rewrites the README (both languages) to replace narrative description with checkable claims, and corrects one factual error in the evidence citations.

### Added
- README: glossary section (14 terms with authoritative definitions: study engineering, scan gaps, bridge plans, gating tests, concept attack supplement, 5-step daily loop, red-line checklist, readability probe).
- README: "where it applies — and where it does not" table (7 verdicts covering STEM / humanities / lower grades / no-coordinator / no-library / no-score-expectation / university).
- README: **contradictory evidence section** documenting known failure conditions of the cited mechanisms, with sources — Loibl et al. (2017), Sinha & Kapur (2021), Chen & Kalyuga (2020), Loibl et al. (2020), Mazziotti (2017). Previously the evidence table listed only supporting evidence.
- README: verification section with 5 measurable criteria plus a meta-rule ("any step without a criterion counts as unverified").
- README: explicit evidence-strength scale (strong / moderate–strong / moderate / empirical).
- README: anonymization scope-and-method table, replacing a one-line blanket claim.
- README: guidance on `examples_zh` / `examples_en` frontmatter fields per the official skill spec.
- SKILL.md: `examples_zh` / `examples_en` frontmatter fields (shown on the marketplace detail page).
- CHANGELOG.md shipped in the package.

### Corrected
- **Factual error**: the evidence table described Collins, Brown & Newman (1989) as "six methods including fading and problem setting". The original paper proposes six strategies — modeling, coaching, scaffolding, articulation, reflection, exploration. Fading is a design orientation running through them, not one of the six.
- Kapur (2016) was cited as *Productive Failure*; the article's title is *Examining Productive Failure, Productive Success, Unproductive Failure, and Unproductive Success in Learning*.
- Laursen et al. (2014) was cited with the journal abbreviated as "JRME"; the full title is now given (*Journal for Research in Mathematics Education*).
- Chi et al. (1989) and Carless & Boud (2018) now carry full journal, volume, issue, and page ranges instead of author-year only.
- The evidence strength for "attempt first, then consult external input" was downgraded from strong to moderate, since the underlying literature is contested and context-dependent (see the new contradictory-evidence section).
- "Swap parameters and reuse" no longer implies red-line items transfer as-is; the framework now states they must be re-cut to the learner.

### Changed
- README and README.en.md rewritten: descriptions changed from narrative framing ("assets", "philosophy") to checkable assertions with explicit boundaries, and the two files are now section-for-section aligned.
- README: the "脱敏说明" claim was replaced by a scope-and-method table plus a reusable self-check procedure.
- SKILL.md: references to `study-deliverable-precheck` and `study-plan-bridge` now state that neither is on the marketplace, so the skill remains independently usable without them.

### Packaging
- `build_market_pkg.py` now copies `CHANGELOG.md` and the `scripts/` directory, and writes the zip under the current version number. Previously the published zip omitted `scripts/` (so the documented `pdf_readability_probe.py` command was not shippable) and the changelog.

## 1.0.1 — 2026-10-09

- Removed the local question-generation / cloud-grading track (Ollama `qwen2.5:7b`): question sourcing now follows the read-from-source discipline exclusively — real archived materials first; model-generated questions are a last resort and must be declared.
- Removed `references/ollama_qgen.md` and the matching red-line item ("local model generates questions only, grading in the cloud").
- Neutralized wording in the daily loop: step 4 now reads "send hard pages for grading" instead of referencing a cloud grading channel.
- Removed the "local model question accuracy" known-limitation note; no such track exists anymore.
- No changes to the core framework: scan gaps → bridge, 5-step daily loop, parameterized red-line checklist, readability probe.

## 1.0.0

- Initial release.
