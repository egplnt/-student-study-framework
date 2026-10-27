# High-School Study Engineering Framework (student-study-framework)

A **process framework for high-school study**, built for WorkBuddy agents. It decomposes "organizing a study routine" into four executable, checkable components: a method for locating knowledge gaps and designing bridges, a daily closed-loop routine, a checklist of enforceable red lines, and a pre-archiving readability probe for source materials.

**This file is a manual, not an outcome guarantee.** Every mechanism below states its source and evidence strength; anything without third-party research support is explicitly labeled "project experience". The framework does not promise score gains — real effect depends on your material library, daily human effort, and execution discipline (see [§7 Effect boundaries](#7-effect-boundaries)).

Current version: **1.1.0** | See [`CHANGELOG.md`](CHANGELOG.md)

---

## Contents

1. [Glossary](#1-glossary)
2. [What the framework contains](#2-what-the-framework-contains)
3. [Where it applies — and where it does not](#3-where-it-applies--and-where-it-does-not)
4. [Evidence behind each mechanism](#4-evidence-behind-each-mechanism)
5. [Contrary evidence: known failure conditions](#5-contrary-evidence-known-failure-conditions)
6. [How to verify whether it works](#6-how-to-verify-whether-it-works)
7. [Effect boundaries](#7-effect-boundaries)
8. [Repository and release status](#repository-and-release-status)
9. [Install](#8-install)
10. [Usage](#9-usage)
11. [Readability probe](#10-readability-probe)
12. [Known gaps](#11-known-gaps)
13. [Anonymization and data handling](#12-anonymization-and-data-handling)
14. [Citation and versioning](#13-citation-and-versioning)
15. [License](#14-license)
16. [Files](#15-files)

---

## 1. Glossary

Definitions here are authoritative for how these terms are used in this framework.

| Term | Definition |
| --- | --- |
| **Study engineering** | Treating study as a designable, measurable, iterable engineering object: explicit inputs (materials, time, effort), an explicit process (bridge, execute, verify), and explicit outputs (checkable artifacts), with a criterion retained for every step. |
| **Scan gaps** | Locating breaks in a student's knowledge structure. Two kinds are produced: ① **knowledge jumps** — missing prerequisite knowledge that blocks later material; ② **conceptual blockers** — the concept itself is not understood, shown by repeated errors on the same point. |
| **Bridge plans** | An ordered remediation path for each located gap, with a checkable pass condition attached to every step. |
| **Gating tests** | A checkpoint after a bridge is completed. Passing is required before the next stage; failing sends you back to the relevant bridge segment. Gate criteria should be countable (number of items, right/wrong, ability to explain aloud) — "feels like I've got it" is not accepted. |
| **Concept attack supplement** | An isolated attachment for conceptual blockers. Until the blocker is broken, it is not mixed into regular tests, so other items' performance cannot mask an unresolved concept. |
| **5-step daily loop** | ① generate print list → ② handwritten execution → ③ 90-second triple check → ④ send hard pages for grading → ⑤ report answers. |
| **Red-line checklist** | Item-by-item checkable prohibitions and preconditions, split into "progress/content" and "tool/data". |
| **Readability probe** | Measuring before archiving whether a document's text layer is actually extractable, judged by common-character hit rate rather than "characters came out". |

## 2. What the framework contains

| Component | Purpose | Artifact form | Main basis |
| --- | --- | --- | --- |
| Scan gaps → bridge | Locate gaps, design remediation, set gates | Bridge file (printable HTML) | Research-backed, see [§4](#4-evidence-behind-each-mechanism) |
| 5-step daily loop | Turn "a plan" into "done today and checkable" | Daily print list + weekly task sheet | Research-backed (self-explanation, scaffolding fading) |
| Parameterized red-line checklist | Fix prohibitions and preconditions so known errors stop recurring | Checkbox sheet | Mixed, see [§4](#4-evidence-behind-each-mechanism) |
| Readability probe | Stop "the file is on disk" from being taken as "the content is usable" | CLI script + verdict table | Project experience, no third-party research |

The framework is parameterized by: grade level, subject, target band, main textbooks, exam year. Switching students means replacing those parameters and reusing the process — but **red-line items and bridging logic come from concrete cases and must be re-cut to fit** (see [§3](#3-where-it-applies--and-where-it-does-not)).

## 3. Where it applies — and where it does not

| Verdict | Conditions |
| --- | --- |
| **Applies** | High-school STEM (mathematics, physics, chemistry); a parent or coordinator who can commit daily; an existing per-subject searchable local material library. |
| **Conditionally applies** | High-school humanities: the process still works, but bridge design must be adjusted — humanities gaps are more about conceptual boundaries and argument structure than computational chains. |
| **Conditionally applies** | Middle school, repeat year, primary-to-junior transition: the 5-step loop and red lines carry over; the scan-gaps→bridge criteria (gating tests) must be rewritten for the stage. |
| **Does not apply** | No one owns daily coordination: loop steps ②③④⑤ break, and the framework degrades into a one-shot plan generator. |
| **Does not apply** | No local material library and no OCR capability: bridge plans have nothing to draw on. |
| **Does not apply** | Expecting "install it and scores go up": this framework ships no data assets and no labor, see [§7](#7-effect-boundaries). |
| **Does not apply** | University level or adult self-study: target bands and exam structures differ too much; the parameterized shell does not hold. |

## 4. Evidence behind each mechanism

Each row lists its **source** and **evidence strength and limits**. Strength levels:

- **Strong** = supported by multiple meta-analyses or large-sample randomized controlled studies
- **Moderate–strong** = empirically supported, but sample or setting is bounded
- **Moderate** = contested, or effect size depends on design details
- **Empirical (project-level)** = practice-based conclusion of this project, no third-party research

| Mechanism | Source | Strength & limits |
| --- | --- | --- |
| Attempt first, then consult external input; never read the answer first | Kapur, M. (2016). *Examining Productive Failure, Productive Success, Unproductive Failure, and Unproductive Success in Learning*. Educational Psychologist, 51(2), 289–299. Self-explanation: Chi, M. T. H., et al. (1989). *Self-explanations: How students study and use examples in learning to solve problems*. Cognitive Science, 13(2), 145–182. | Moderate — **not "strong"**: effect sizes for Productive Failure depend heavily on design fidelity and subject area; boundary conditions in [§5](#5-contrary-evidence-known-failure-conditions). The original self-explanation studies had small samples. |
| Attribution belongs to the student: self-assess first, then compare side by side with external feedback | Sadler, R. S. (1989). *Reflections on expertise: A cognitive basis for instructional design*. Instructional Science, 18(2), 119–144. Feedback literacy: Carless, D., & Boud, D. (2018). *Student feedback literacy in higher education: a critical review*. Teaching in Higher Education, 23(8), 1315–1340. | Moderate–strong. The first is a theoretical paper, not an effect trial; the second is a literature review. Students need basic evaluative vocabulary first. |
| Teacher/AI scaffolding fades out by design | Collins, A., Brown, J. S., & Newman, S. J. (1989). *Cognitive apprenticeship: Teaching crafts the learning of authentic activity*. In Lave, J., & Wenger, E. (Eds.), Knowing, Learning, and Instruction. Lawrence Erlbaum. | Moderate–strong. The original proposes six strategies — modeling, coaching, scaffolding, articulation, reflection, exploration; **fading is a design orientation running through them, not one of the six**. Evidence comes mainly from classroom and apprenticeship studies. |
| AI use needs guardrails; do not hand over the answer | Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. PNAS, 122(26), e2422633122. | Moderate–strong. Field experiment with nearly a thousand high-school students: during practice the GPT-access group gained 48%, but after AI removal that group scored 17% below the never-used control; the hint-guarded version largely offset the harm. Single platform and subject; guardrail form must be built by you. |
| Inquiry-based learning holds in university mathematics too | Laursen, S. L., Hassi, M.-L., Kogan, M., & Weston, T. J. (2014). *Benefits for women and men of inquiry-based learning in college mathematics: A multi-institution study*. Journal for Research in Mathematics Education, 45(4), 406–418. | Moderate–strong. Over 100 course sections at 4 universities. The study population is university classrooms; the fit to a 1-on-1 home setting is yours to assess. |
| Probe readability before archiving a document | Project experience, not published research | Empirical (project-level). Text-layer usability of different PDF versions of the same content can be exactly opposite. Criteria in [`scripts/pdf_readability_probe.py`](scripts/pdf_readability_probe.py). |

> This table is an index, not a review. Except for the last row, all entries are published research — read the originals before relying on them; this framework does not warrant their validity. For the **contrary and boundary** evidence, see the next section.

## 5. Contrary evidence: known failure conditions

Listing only supporting evidence makes the table above look more reliable than it is. Here is where the same body of research **does not** support the framework's claims. Read this section before using it.

| Mechanism | Known failure conditions | Source |
| --- | --- | --- |
| Attempt first, then instruct | Problem-solving-then-instruction (PS-I) is not universally superior. For **procedural knowledge**, instruction-first (I-PS) performs comparably or better; for conceptual knowledge PS-I wins. Advantage is largest at high design fidelity (Hedge's g ≈ 0.58) and disappears when fidelity is low. | Sinha, T., & Kapur, M. (2021). *When problem solving followed by instruction works: Evidence for productive failure*. Journal of Research in Science Teaching, 58(6), 1682–1703; Chen, S., & Kalyuga, S. (2020). *Is the learning from generative AI...?* European Journal of Psychology of Education, 35, 607–624. |
| Attempt first, then instruct | An earlier review notes most supporting research concentrates on STEM (mainly mathematics); **two quasi-experiments in non-STEM domains found no advantage**. The literature also concentrates on a small number of authors with narrow samples. | Loibl, K., Roll, I., & Rummel, N. (2017). *Towards a theory of when and how problem solving followed by instruction supports learning*. Educational Psychology Review, 29, 693–715; Loibl, K., Roll, I., Rummel, N., & Rummel, S. (2020). *When failure fails to be productive*. Instructional Science, 48, 789–807. |
| Attempt first, then instruct | **Younger students** may fail to benefit because they cannot yet recognize knowledge gaps; the PF effect often does not hold at primary-school level. | Mazziotti, C. (2017). *When young students fail to productively learn with Productive Failure* (doctoral dissertation, Ruhr-Universität Bochum). |
| AI use needs guardrails | Guardrail effectiveness depends on the guardrail actually blocking "just give me the answer". The study shows the mitigation comes from the hint design; if guardrails are bypassed, the harm returns. | Bastani et al. (2025), as above. |

**Practical consequence**: the "attempt first" step in this framework mainly applies to **conceptual gaps in high-school STEM**. If the gap sits in a calculation procedure or a procedural skill, direct instruction may be faster — do not force a failure-then-consolidation path.

## 6. How to verify whether it works

The framework produces no effect on its own; it needs matching criteria to tell whether continued investment is warranted. Write these down before switching on, then check them item by item after 4–6 weeks:

| Criterion | How to measure | Pass standard |
| --- | --- | --- |
| Are gap diagnoses accurate | Compare against the student's actual wrong answers: were items judged "knowledge jumps" really caused by missing prerequisites? | Sample 5 items, misdiagnosis ≤ 1 |
| Do gating tests discriminate | For a student who failed a gate, does re-bridging produce an observable change on the gate items? | At least one observable change; otherwise that gate carries no information |
| Does the loop actually loop | Count 5-step completion across 5 consecutive working days | ≥ 80%; every unfinished day must have an explicit carry-over entry as the next day's first item |
| Does the triple check ever catch something | Record how many errors the triple check actually intercepts | ≥ 1 per week; otherwise the step is a no-op |
| Overall cost–benefit | Record the coordinator's weekly hours | If it exceeds ~30% of the student's effective study time, cut the process down |

**Meta-rule for criteria**: any step without a criterion counts as unverified. If a "bridge is complete" or "status is good" statement in this framework cannot be tied to a countable criterion, it does not constitute a closed loop.

## 7. Effect boundaries

- The framework can establish "plan → execute → verify" process discipline from scratch. It **does not automatically produce score gains**.
- Effect ≈ methodology × material assets × daily human effort × environment fit. This skill provides part of the first factor only.
- Subject fit: STEM (mathematics / physics / chemistry) is the best-validated case; humanities require adjusted bridging logic, see [§3](#3-where-it-applies--and-where-it-does-not).
- Red-line items are mostly distilled from concrete cases and must be re-cut to your own situation — **do not copy verbatim**.
- What this framework provides is **process and criteria**. It does not ship textbooks, question banks, or data assets.

## Repository and release status

- **GitHub**: https://github.com/egplnt/-student-study-framework — the repository containing this file, with full source, `LICENSE`, and release downloads.
- **WorkBuddy SkillHub marketplace**: searchable as "高中生学习工程框架" (High-School Study Engineering Framework). v1.1.0 is under review (about 7 working days). Until it is approved, use method 2 below (local placement).

## 8. Install

### Option 1: WorkBuddy marketplace (SkillHub)

In the WorkBuddy client go to 【Experts · Skills · Connectors】→【Skills】→【Skill Market】, search for "High-School Study Engineering Framework", and install.

### Option 2: local

Place this repo under the WorkBuddy user-level skills directory:

- **Windows**: `%USERPROFILE%\.workbuddy\skills\student-study-framework\`
- **macOS / Linux**: `~/.workbuddy/skills/student-study-framework/`

`git clone` or unzip; make sure `SKILL.md` sits inside. Restart WorkBuddy or mention the skill in a chat.

Developer submission flow and package spec: [WorkBuddy open-platform skill docs](https://open.workbuddy.cn/docs/skill).

## 9. Usage

Describe your needs (study plan / bridging / weekly task sheet / red-line check) and the skill loads automatically.

Per the official spec, `examples_zh` / `examples_en` should also be filled in the `SKILL.md` frontmatter so the market listing can show them under 【Try it like this】. Examples:

- "Run a gap scan for first-year high-school math, list the knowledge jumps and design bridge plans"
- "Generate this week's task sheet and the daily 5-step loop checklist"
- "Check my study plan against the red-line checklist"

## 10. Readability probe

**The problem**: whether a PDF is searchable cannot be read off its filename, page count, or size. In testing, two versions of the *same* content behaved oppositely: the one with the most pages and the most extracted characters was in fact garbage text (text layer present, character mapping broken), while the smaller one had a perfectly clean text layer.

**The method**: probe before archiving, and judge by **common-character hit rate** (share of high-frequency characters among all CJK characters on sampled pages), not by "how many characters came out":

```bash
pip install pypdf
python scripts/pdf_readability_probe.py <file.pdf> [<file2.pdf> ...]
python scripts/pdf_readability_probe.py <dir-or-glob> --json out.json
python scripts/pdf_readability_probe.py --selftest
```

Verdicts: OK / garbled (needs another version or OCR) / no text layer (scan, needs OCR) / sparse (formulas are images, low retrieval value). **Exit code 2 when anything is unusable**, so it can be wired into an ingest pipeline as a gate.

## 11. Known gaps

The framework **does not provide** the following; supply it yourself:

- **No export path**: deliverables are self-contained HTML (printable, offline, inline SVG interaction), but there is **no Markdown / Anki export**. If you need the content inside other tools, build that layer yourself.
- **When to animate**: only for spatial relations, dynamic processes, or multi-state comparison. If a static figure plus three sentences explains it, do not animate.
- **No question bank**: the framework produces no questions; they must come from your own material library.
- **Not validated across subjects**: effects outside STEM have not been systematically examined.
- **No controlled experiment on the framework itself**: every "effective" statement refers to single-case observation, not a group effect size.

## 12. Anonymization and data handling

This skill is the externally published version. Scope and method of anonymization:

| Item | Treatment |
| --- | --- |
| Internal code names and aliases | All replaced with neutral wording ("Student A" etc.); no real names or family-internal labels appear |
| Internal file paths and IDs | Not referenced; indicated only by neutral description |
| Example data | All synthetic rewrites, not real student records |
| Public sources | The public discussion link retained in `ORIGIN.md` is a public web page containing no workspace information |

**Data handling convention**: this skill contains no data collection or reporting logic. In real use, learning materials containing personally identifiable information should stay local; if handed to a cloud model, assess against that product's data policy.

**Suggested pre-publication self-check** (for anyone modifying this): search all text in this directory for real names, internal paths, and internal IDs; confirm example data cannot be matched back to real records.

## 13. Citation and versioning

Please cite the version number when referencing this framework. If you cite its mechanisms in research or articles, cite the corresponding literature as well (see [§4](#4-evidence-behind-each-mechanism)).

- Current version: **1.1.0**
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- English: [`README.en.md`](README.en.md)
- Background and design constraints: [`ORIGIN.md`](ORIGIN.md); prerequisites and effect boundaries: the top of [`SKILL.md`](SKILL.md) (must read)

## 14. License

CC BY-NC-SA 4.0 — free to share and adapt, **non-commercial**, with attribution and share-alike. See [`LICENSE`](LICENSE).

## 15. Files

```
student-study-framework/
├── SKILL.md            # core framework (self-contained, incl. prerequisites & limits)
├── ORIGIN.md           # background & design constraints
├── README.md           # Chinese
├── README.en.md        # English (this file)
├── CHANGELOG.md        # changelog
├── LICENSE             # CC BY-NC-SA 4.0
├── scripts/            # executable tools
│   └── pdf_readability_probe.py   # PDF readability gate
└── references/         # optional templates
    ├── daily_loop.md
    └── redline_checklist.md
```
