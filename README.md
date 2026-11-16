# AI skills

Reusable skills for Claude and other AI agents: writing, documents, slides, comics, product work, meetings and music.

Each skill is one folder with a `SKILL.md` file. The file tells the AI what the skill is for and the exact steps to follow. You can read any of them like a short guide.

**Jump to:** [Skills map](#skills-map) · [Use a skill](#use-a-skill) · [Add a skill](#add-a-skill)

---

## Skills map

Skills with `rtsl` or `h360` in the name were built for Resolve to Save Lives and the HEARTS360 toolkit. They work elsewhere, but you may want to swap in your own organization's rules.

<!-- SKILLS:START -->

**15 skills.** Click a name to open it.

### Writing

| Skill | What it does |
|---|---|
| [`clear-writing`](skills/clear-writing/SKILL.md) | Write, edit or tighten any work text in a plain, direct style that busy readers act on. |
| [`rtsl-writing-style-guide`](skills/rtsl-writing-style-guide/SKILL.md) | Apply Resolve to Save Lives voice, tone and messaging rules to any RTSL text. |

### Documents and visuals

| Skill | What it does |
|---|---|
| [`comic-report-creator`](skills/comic-report-creator/SKILL.md) | Turn trip reports and meeting notes into accurate, readable comic-book reports. |
| [`docx-styling`](skills/docx-styling/SKILL.md) | One clean, consistent visual style (palette, type, tables) for every Word document. |
| [`rtsl-slide-deck`](skills/rtsl-slide-deck/SKILL.md) | Build or redesign a restrained, one-idea-per-slide deck in Claude Design. |

### Product and delivery

| Skill | What it does |
|---|---|
| [`h360-release-notes`](skills/h360-release-notes/SKILL.md) | Write plain-language release notes on a Confluence page without breaking images. |
| [`product-designer`](skills/product-designer/SKILL.md) | Turn a PRD into a clear visual concept and specs anyone can read at a glance. |
| [`product-manager`](skills/product-manager/SKILL.md) | Scope an MVP, write a short PRD, and push back on feature creep. |
| [`software-developer`](skills/software-developer/SKILL.md) | Build the smallest reliable implementation that meets the spec, and verify it. |
| [`team-builder`](skills/team-builder/SKILL.md) | Decide which roles a project needs and write a clear spec for each one. |

### Meetings and admin

| Skill | What it does |
|---|---|
| [`meeting-summary`](skills/meeting-summary/SKILL.md) | Turn a Teams meeting transcript into an action-first, one-screen notes doc. |
| [`nightly-meeting-notes`](skills/nightly-meeting-notes/SKILL.md) | Scheduled task: every evening, save notes for the day's recorded Teams meetings. |
| [`rtsl-reimbursement-and-per-diem`](skills/rtsl-reimbursement-and-per-diem/SKILL.md) | Turn a trip folder of receipts into copy-paste expense and per diem entries. |

### Creative

| Skill | What it does |
|---|---|
| [`music-composer`](skills/music-composer/SKILL.md) | Compose simple, original, royalty-free instrumental music scored to a project. |
| [`music-director`](skills/music-director/SKILL.md) | Set the musical direction and review a composer's drafts against it. |

<!-- SKILLS:END -->

---

## Use a skill

Pick the way that matches your tool.

### Claude app (claude.ai or desktop)
1. Download this repo: **Code → Download ZIP**, then unzip it.
2. Zip the one skill folder you want, for example `skills/clear-writing`.
3. In Claude, go to **Settings → Capabilities → Skills → Upload skill** and choose that zip.

### Claude Code
Copy the skill folder into your skills directory:

```bash
git clone https://github.com/tonyjoyk/AI_skills.git
cp -R AI_skills/skills/clear-writing ~/.claude/skills/
```

Use `.claude/skills/` inside a project instead to share it with that project only.

### Any other AI tool
Open the skill's `SKILL.md`, copy everything below the `---` header, and paste it as instructions (system prompt, custom instructions or project knowledge).

---

## Add a skill

One command creates the folder from the template and adds the skill to the map above:

```bash
python3 scripts/new_skill.py poster-maker "Documents and visuals" "Design a clear one-page poster."
```

Then open `skills/poster-maker/SKILL.md` and fill in the description and steps.

Already have a skill folder (for example, exported from Claude)? Drop it into `skills/`, add a `metadata` block to its header, and rebuild the map:

```yaml
metadata:
  summary: "One line for the map."
  category: Writing
```

```bash
python3 scripts/build_index.py
```

You can skip the rebuild. When you push to `main`, a GitHub Action rebuilds the map for you.

### Rules for every skill
- **Folder name = `name`** in the header, lowercase with hyphens (`poster-maker`).
- **Name the job, not a person.** `product-manager`, not a character name.
- **`description`** says what it does and when to use it. The AI reads this to decide when to load the skill.
- **`summary`** is one short line for the map.
- **`category`** is one of: Writing, Documents and visuals, Product and delivery, Meetings and admin, Creative. A new category name also works; it shows up at the end of the map.
- Put long reference material in a `references/` folder inside the skill, and link it from `SKILL.md`.
- No passwords, personal emails, private URLs or real people's details.

---

## Repo layout

```
skills/<skill-name>/SKILL.md   one folder per skill (plus optional references/, scripts/, assets/)
templates/SKILL.md             starting point for new skills
scripts/new_skill.py           create a skill and update the map
scripts/build_index.py         rebuild the skills map in this README
```
