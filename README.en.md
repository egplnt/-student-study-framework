# student-study-framework

A reusable **study-engineering methodology skill for high-school students** (for the WorkBuddy agent).

## What it is
Four reusable assets:

1. **Scan gaps → bridge**: locate knowledge jumps and conceptual blockers, design bridging plans, and gate progress with tests.
2. **5-step daily loop**: print list → handwritten execution → 90-second triple check → send hard pages for grading → report answers.
3. **Local question generation + cloud grading**: a local model (Ollama `qwen2.5:7b`) generates questions only; grading stays in the cloud.
4. **Parameterized red-line checklist**: progress / content red lines + tool / data red lines, each checkable.

The framework is parameterized (grade level / subject / exam year / target band / main textbooks) — switching to another student only means replacing parameters.

> **Background & philosophy**: see [`ORIGIN.md`](ORIGIN.md). **Prerequisites & limits**: see the top of [`SKILL.md`](SKILL.md) (must read).

## Install

### Option 1: local (recommended)
Place this repo under the WorkBuddy user-level skills directory:

- **Windows**: `%USERPROFILE%\.workbuddy\skills\student-study-framework\`
- **macOS / Linux**: `~/.workbuddy/skills/student-study-framework/`

`git clone` or unzip; make sure `SKILL.md` sits inside. Restart WorkBuddy or mention the skill in a chat.

### Option 2: WorkBuddy marketplace
Submit through the official process so it appears in the install list.

## Usage
Describe your needs (study plan / bridging / weekly task sheet / local question generation / red-line check) and the skill loads automatically.

## License
CC BY-NC-SA 4.0 — free to share and adapt, **non-commercial**, with attribution and share-alike. See [`LICENSE`](LICENSE).

## Files
```
student-study-framework/
├── SKILL.md            # core framework (self-contained, incl. prerequisites & limits)
├── ORIGIN.md           # background & philosophy
├── README.md           # Chinese
├── README.en.md        # English (this file)
├── LICENSE             # CC BY-NC-SA 4.0
└── references/         # optional templates
    ├── daily_loop.md
    ├── redline_checklist.md
    └── ollama_qgen.md
```
