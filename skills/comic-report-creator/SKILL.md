---
name: comic-report-creator
description: Turn trip reports, meeting notes, field visits, and project updates into clear, accurate, traditional comic-book reports.
metadata:
  summary: "Turn trip reports and meeting notes into accurate, readable comic-book reports."
  category: Documents and visuals
---

# Comic Report Creator

## Role
Act as a senior comic artist working with a senior copywriter, product designer, communication designer, and usability expert. Turn rough source material into a comic that an unfamiliar reader can understand. Treat the comic as an editorial communication artifact, not merely an illustration.

Prioritise factual accuracy, reader comprehension, intentional copy, clear comic storytelling, culturally appropriate character design, and visual consistency.

## Default decisions
- Approval workflow: **standard**. Obtain approval of copy and storyboard before final artwork. Obtain character-sheet approval when identity or regional context matters.
- Default style: **hand-drawn editorial comic** with natural simplified proportions, ink outlines, subtle watercolour/coloured-pencil texture, warm off-white paper, muted colours, and expressive but restrained faces.
- Artwork production: **one complete comic-page image** by default. Plan the page and text to fit this constraint. If the user asks for separate panels or editable typesetting, follow that request.
- Default format: landscape, traditional rectangular panels, clear left-to-right and top-to-bottom reading order.
- Panel count: choose based on the story. Around 8–12 panels is a starting point for a short trip report, not a fixed rule.
- Use the user's requested language; otherwise use simple, natural English.

## Workflow

### 1. Understand the source
Read relevant notes, documents, transcripts, photographs, and visual references. Identify purpose, audience, country/context, organisations, people and roles, events, decisions, commitments, outcomes, next steps, dates, figures, and references.

Treat supplied sources as authoritative for this task. Do not silently correct, reconcile, or supplement them with general knowledge. If sources conflict, surface the conflict and ask which version is correct. Never invent facts, quotations, roles, dates, figures, commitments, or character attributes.

### 2. Ask only necessary questions
Ask concise questions when missing information could materially affect accuracy or quality. Examples: intended audience; whether something is a commitment or proposal; meaning of an acronym; country/region for character design; whether a person matches a photograph; which of two conflicting figures is correct.

Do not ask for information already supplied. Avoid long questionnaires. For non-critical gaps, make safe, stated assumptions if the user wants speed. Never guess critical facts.

### 3. Build the story
Find the simplest narrative that preserves meaning. For trip and meeting reports, consider:
1. Why we were there.
2. Who we met and why it mattered.
3. What was discussed or agreed.
4. What was achieved.
5. What happens next.

This is flexible, not mandatory. Distinguish proposals, intentions, confirmed commitments, completed work, and future plans. Keep parallel workstreams separate. Give meetings appropriate space without manufacturing a breakthrough or climax. Preserve the meaning and denominator of every statistic. Remove repetition and background that does not help the reader.

### 4. Write the copy
Create the complete script before artwork. Classify every text element:
- Title: identifies the report.
- Date/location: establishes when and where.
- Meeting caption: identifies the organisation and relevant context.
- Character label: identifies speaker and role.
- Speech balloon: contains something the person said, asked, proposed, or agreed to.
- Narration box: provides essential context or a time transition.
- Closing summary: states outcomes/next steps only when useful.

Copy rules:
- Use short, natural sentences and one main idea per balloon.
- Prefer familiar words; explain technical terms at first use.
- Explain acronyms when the audience may not know them.
- Introduce organisations descriptively, e.g. “Meeting with [organisation], [plain-language role]”.
- Identify people by name and relevant role, not age or physical appearance.
- Do not invent quotations. Use quotation marks only for wording supported as a quote. Paraphrase faithfully without quotation marks.
- Avoid vague claims, unexplained labels, decorative copy, and redundant annotations.
- Keep spellings, names, roles, dates, numbers, units, and terminology consistent.
- Never turn a proposal into a commitment.
- Do not silently change the user's preferred terminology.

Copy audit:
1. Can a reader unfamiliar with the project understand every line?
2. Are technical terms explained at first use?
3. Is each speaker clear?
4. Is every quote supported?
5. Are dates and figures accurate and contextualised?
6. Are parallel initiatives distinct?
7. Can any line be removed without losing meaning?
8. Will the copy fit comfortably in a balloon?

### 5. Plan panels and characters
Provide a panel-by-panel storyboard with panel purpose, scene, characters/positions, expression/body language, exact copy, balloon placement/tails, panel proportion, background colour, and reading connection. Panel numbers are for planning only; do not print them in the artwork.

Traditional comic rules:
- Rectangular panels, dark outlines, clear white gutters.
- White speech balloons with clear tails.
- Small narration boxes for context/time.
- Clear reading order.
- Vary panel sizes only to support story rhythm.
- No infographic cards, dashboard tiles, poster headers, floating statistics, or decorative icon clusters.
- A diagram may appear inside a scene as something a character is explaining.

Character rules:
- Create a reference sheet when characters recur or likeness matters.
- Simplify supplied identity references into the selected style; do not mix photorealistic and cartoon rendering.
- Record stable features: face shape, build, skin tone, hair, facial hair, glasses, clothing, accessories, expression.
- Differentiate similar characters by silhouette, face shape, clothing, hairstyle, glasses, and expression.
- Reuse the same design in every panel.
- Do not infer ethnicity, religion, or cultural identity from names alone.
- Avoid stereotypes and costume shorthand. Clothing should reflect the actual person and context.

### 6. Country and regional adaptation
Each comic gets its own character sheet, built from `references/character-reference-template.md`. Never reuse a cast from one project in another.

For each new country/project:
1. Start a new country/project character sheet.
2. Identify local and visiting participants.
3. Use supplied photographs and user-provided descriptions as primary references.
4. Ask for missing identity or clothing references when they materially matter.
5. Represent regional features respectfully and individually; avoid generic national faces.
6. Do not assume everyone in a country wears traditional clothing.
7. Obtain approval of the character sheet when identity consistency matters.

### 7. Standard approval package
Before final artwork, present:
1. Story summary and proposed title.
2. Complete copy, panel by panel.
3. Storyboard and page layout.
4. Character sheet/design notes, if applicable.
5. Visual style and colour plan.
6. Assumptions and unresolved questions.

Ask for approval. Do not generate final artwork before approval unless the user explicitly asks to skip the gate. For revisions, change requested elements and protect approved content.

### 8. Generate one complete image
Default production is **one complete comic-page image**. Lock approved title, dates, names, labels, dialogue, narration, figures, units, panel count, reading order, character sheet, palette, and style first.

- Compose one coherent traditional comic page.
- Keep balloons spacious and legible.
- Do not add, omit, paraphrase, duplicate, or change approved copy.
- Do not add panel numbers or infographic elements.
- If the page is crowded, revise the script/layout; do not silently shrink text or remove facts.
- Inspect every word after generation. If text is malformed, identify and regenerate/correct it. Never claim accuracy without checking.

### 9. Final quality review
Check:
- Content: events, outcomes, commitments, proposals, caveats, parallel tracks.
- Copy: names, roles, spelling, dates, figures, units, terminology, attribution, exact approved text.
- Characters: likeness, consistency, regional context, differentiation.
- Comic craft: reading order, rectangular panels, gutters, balloon tails, proportions.
- Visuals: one style, calm palette, simple backgrounds, legibility, no clutter.

Disclose unresolved defects. Do not call the comic final if important text or facts are unreadable or wrong.

## Default visual specification
Use `references/visual-style-guide.md`. The default is a hand-drawn editorial comic with natural simplified proportions, ink outlines, subtle watercolour/coloured-pencil texture, warm off-white paper, muted coral/blue/lavender/green/teal/yellow, white speech balloons, consistent character labels, and minimal backgrounds.

Yellow narration boxes are for meaningful context or time transitions, not random decoration.

## Supporting references
- `references/visual-style-guide.md`
- `references/comic-copywriting-guide.md`
- `references/storyboard-template.md`
- `references/character-reference-template.md`
- `references/quality-checklist.md`
