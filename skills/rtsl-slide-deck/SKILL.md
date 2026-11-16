---
name: "rtsl-slide-deck"
description: "Build or improve an RTSL-style slide deck inside Claude Design — restrained visual language, one idea per slide, minimal purposeful visuals. Use whenever the user asks for slides, a deck or a presentation for Resolve to Save Lives, pastes content to turn into slides, or uploads an existing deck (.pptx, .potx, PDF or screenshots) and asks to improve, redesign, tidy or RTSL-ify it. The deliverable is always slides in Claude Design; do NOT use this skill to write out a .pptx or .potx file (use the pptx skill for that). Apply rtsl-writing-style to the words on the slides."
metadata:
  summary: "Build or redesign a restrained, one-idea-per-slide deck in Claude Design."
  category: Documents and visuals
---

# RTSL slide deck

The deliverable is always slides in Claude Design. This skill never writes a .pptx file
— if the user wants a downloadable PowerPoint, say so and hand off to the pptx skill.

Users invoke this skill with little framing. Your first job is to fill the gaps, not to
start designing.

## 1. Which path are you on?

**No deck attached** — the user pasted or described content. Go to step 2.

**A deck is attached** — the user uploaded something to improve. Go to step 2a, and do
not skip the read or the critique.

## 2. Ask before designing

If **audience, purpose or length** is missing or vague, ask before anything else — one
question form, not a chat paragraph. Never guess these three.

- **Audience** — who is in the room, and what they already know.
- **Purpose** — the decision, approval or action wanted at the end. "Inform" is not a
  purpose; push for what changes after the meeting.
- **Length** — minutes or slide count. If minutes, convert at 1–2 minutes per content
  slide and confirm.

Ask about tone, available data and images, and anything off-limits only when unclear.
Never ask about visual style — the RTSL design system in Claude Design settles that.

If the user says "just make it," pick sensible values, state them in one line and proceed.

## 2a. Read the uploaded deck, then critique

**Read it first.** Use the pptx skill to extract content from .pptx and .potx, the pdf
skill for PDFs, and read screenshots directly. Capture every slide's title, body text,
numbers, labels, sources and speaker notes before you judge anything. If a chart's
underlying numbers aren't recoverable from the file, ask for them — never re-key figures
by eye from an image.

**Then infer, don't interrogate.** An existing deck usually reveals its audience, purpose
and length. State what you inferred in one line and ask only about what the deck can't
tell you — most often the purpose ("what should change after this meeting?").

**Then critique before rebuilding.** Show a short list — the ten or so changes that
matter, not every nit. Say what's wrong and what you'd do instead:

- Slides carrying two ideas, and where you'd split them.
- Titles that break the sequence's logic or parallelism.
- Colour, boxes or icons doing decoration rather than work.
- Colour carrying meaning with no text label.
- Prose paragraphs that should be a list, a number, a table or a diagram.
- Overflow, clipping, crowding.
- Content that is thin, unsourced or contradicts itself.

Flag anything you'd cut, and wait for the user's OK before rebuilding. Keep their content
and their argument unless they ask otherwise — you are redesigning, not rewriting the
case. Carry over every number and source exactly.

## 3. Titles before slides

Write the full title sequence and show it before designing. Titles are chapter headings,
not punchlines: plain, sentence case, one grammatical style throughout ("Where we are
today," "Where we invest in 2026–27"). Someone reading only the titles should follow the
argument. One idea per slide — split any slide carrying two.

## 4. Restraint first

Apply the RTSL design system in Claude Design for colour, type and components. Don't
restate or invent it. Then hold back:

- Hairline rules, not boxes and coloured cards. No coloured panel per item, no icon on
  every bullet, no colour for decoration.
- If two elements do the same job on a slide, cut one.
- Never prose paragraphs. Decide what each slide's content wants to be — a short list,
  columns, one number, a simple diagram, a quote, a table.

## 5. Then earn back interest

Give each slide one small, relevant visual that makes it clear at a glance: a dot rail,
a segmented bar, a hairline connector tree, a single line icon per item. Use simple
markers so separate points stay distinguishable.

## 6. Non-negotiables

- **Colour never carries meaning alone.** Every colour-coded item gets a text label, and
  the deck says somewhere what the colours mean.
- **Label and value must look different.** Separate them by size, weight and colour —
  not just position.
- **One numbering scheme.** Not a section number in the header and a slide number in
  the corner.
- **Nothing touching.** Space between elements, breathing room at the bottom. Open space
  low on a slide is correct composition, not a gap to fill.
- **Everything fits.** Check each slide fits 1080px with no overflow or clipping. Report
  what doesn't rather than shrinking type below the design system's floor.
- **Ask for real data, images and logos.** Never invent or draw them.

## 7. Before handing over

Report briefly: slides that overflow, titles that broke parallelism, content you cut or
shortened to fit, and anything you had to invent for lack of source material. When you
rebuilt an uploaded deck, also name anything from the original you dropped, and any
figure you couldn't verify against the source file.

