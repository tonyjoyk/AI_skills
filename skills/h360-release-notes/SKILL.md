---
name: "h360-release-notes"
description: "Write or update HEARTS360 Toolkit release notes on the Confluence Release History page: plain user-facing language, one expand per release, screenshots placed safely."
metadata:
  summary: "Write plain-language release notes on a Confluence page without breaking images."
  category: Product and delivery
---

# HEARTS360 release notes

Use this when adding a new release, editing an old one, or restructuring the Release History page.

Page: `<your Confluence Release History page URL>` (set `cloudId` and `pageId` for your site before use).

## Who reads these

Country partners, EHR vendors, health office staff and RTSL program people. Mostly not engineers. Many read English as a second language. Write so they know what changed for them and what they must do.

## Writing style: about 80% ASD-STE100

Use ASD-STE100 (Simplified Technical English) as the base. Apply its rules about 80% of the time. Break a rule only when the result is clearer for this reader, for example to keep a product name, a Grafana label or a file name exactly as it appears.

### Rules to follow

- **Say what happens, not how it feels.** Do not use vague words such as "tighter", "safer", "better", "improved", "enhanced", "cleaner", "smoother". Write the actual result.
  - Bad: "Tighter access." Good: "Users see only the locations they can access."
  - Bad: "Safer passwords." Good: "Passwords are in the .env file, not in docker-compose.yml."
  - Bad: "Fixed uploads." Good: "File uploads work again."
- **One topic per sentence.** One instruction per sentence in steps.
- **Short sentences.** Maximum 20 words in instructions. Maximum 25 words in descriptions. Aim for 10 to 15.
- **Active voice.** Name who or what does the action. "The dashboard shows…", not "…is shown".
- **Simple tenses.** Present for what the toolkit does now. Past only for what it did before. Future only for scheduled events.
- **Keep articles.** Write "the", "a" and "an". Do not drop them to make text shorter.
- **Verbs, not nouns.** "Back up the database", not "Database backup". Do not use "-ing" words as nouns.
- **No noun clusters longer than three words.** Bad: "drill-down title month display fix". Good: "the title of the drill-down shows the month".
- **One word, one meaning.** Pick one term for a thing and use it everywhere on the page. Do not switch between "location", "org unit" and "area" in one release.
- **Common words.** Use "use" not "utilise", "start" not "initiate", "show" not "display" (unless it is a UI label), "help" not "facilitate".
- **Use the same order every time:** what changed, then what the user can do, then what the user must do.

### Check every title and label

Before you finish, read each expand title, bullet label and table cell. Ask: "Can a reader who does not know the toolkit say what changed?" If the answer is no, rewrite it.

### Also

- No em dashes.
- No hedging, no hype words (seamless, robust, leverage, powerful).
- No engineering terms a partner cannot act on ("materialised views", "SQL fix", "dedup", "refactor", "migration script"). If a technical term is necessary, explain it in plain words right after.
- Be concrete. "Panels load in less than half a second" is better than "faster loading".
- End each bullet and each table cell with a full stop.

## Name the two setups in plain words

"Leaf node" and "central node" are engineering terms. Most readers do not know them. Always write the plain name first, and put the technical term in brackets after it, one time.

| Technical term | Plain name to use | What it is |
| --- | --- | --- |
| Leaf node | **Toolkit installed on your EHR's servers** | The copy of the toolkit that each EHR vendor runs. It holds patient data and line lists. |
| Central node | **National dashboard** | The one dashboard that combines summary numbers from all EHRs. It has no patient data. |

After the first use, the short forms "your EHR's toolkit" and "the national dashboard" are fine. Never write "leaf" or "central" without the plain name near it.

## Page structure

- Newest release at the top.
- Each release is in its own **expand** element. No release is outside an expand.
- No horizontal rules between expands.
- Keep the wide layout on expands if the page already has it.

### Expand title

`vX.Y.Z: <the main result for the user, in plain words> · <D Month YYYY>`

- Say the main result. Good: "Users see only the locations they can access". Bad: "Tighter access" or "Refactor aggregation queries".
- Name one or two main results. Put the others in the bullets.
- Use a middle dot ( · ) before the date. Never an em dash.
- For a release that is not out yet, write `· Scheduled for D Month YYYY`. When it ships, change it to `· D Month YYYY`.
- If the date is not known, leave it out. Do not invent one.
- Titles are plain text. No bold, no links.

## Pick a layout for the release

### Layout A: bullets only

Use when the release affects one setup only, or the changes are the same on both.

1. **How-to line** (if an upgrade or setup page exists): `How-to: <inline smart link to the page>`.
2. **Loom or video** (if one exists): embed card, full view.
3. **Bullets.** One for each change.
4. **Read more link** (optional): `Read more about the features.` as a plain link.

If both setups are affected and you use bullets, put them under bold paragraphs:
- **For the toolkit installed on your EHR's servers (leaf node)**
- **For the national dashboard (central node)**

### Layout B: top changes and a comparison table

Use when the release changes both setups in different ways. When you are not sure, and the release affects both setups, use Layout B.

1. **How-to line** (if any).
2. **Loom or video** (if any).
3. **Top changes.** 2 to 4 bullets with the most important changes. A reader who stops here must know what the release does.
4. **Comparison table.** One row for each change. Columns:

| What changed | Toolkit installed on your EHR's servers (leaf node) | National dashboard (central node) |
| --- | --- | --- |
| Bold label | What a user can do now, or "No change." | What a user can do now, or "No change." |

   - The first column uses the same bold label as the matching bullet.
   - Each cell has one or two short sentences that say what the user can do now.
   - Write "No change." when a setup is not affected. Never leave a cell empty.
   - Do not use a "Leaf or Central?" column. Each setup gets its own column, so readers read only their column.
   - Put a screenshot in the cell where it belongs, after the text of the cell (see Screenshots).
   - Add an **Upgrade from X** row if either setup needs an upgrade or a manual step.
5. **Read more link** (optional).

Keep the table to about 9 rows. If it gets longer, the release needs its own feature page. Link it from "Read more".

## How to write each bullet

Format: **Bold label:** one or two short sentences.

- Label = the feature or area, 1 to 3 words. Examples: **Import status:**, **Region filter:**, **Bug fixes:**, **Upgrade from 0.5.1:**.
- Start with what the user can do or will see. Start with a verb when you can: "Check…", "Select…", "Move between…".
- For a bug fix, say what works now. Do not describe the bug. Good: "All dashboard cards use the selected date filter."
- When a feature is removed, write **Removed.** and give the reason in one sentence.
- Write screen and button names exactly as Grafana shows them. Use bold if the user clicks them.
- If an upgrade needs a manual step, or something stops working, add an **Upgrade from X:** bullet. Say what to do and if the user must upload data again.
- Put links to guides in brackets: `(view guide)`.

## Screenshots

Add a screenshot when a release changes something the user sees: a new panel, filter, screen, button, message or dashboard. Do not add one for a change the user cannot see.

- In bullets: put the screenshot **in the bullet it shows, after the text paragraph of the bullet**.
- In tables: put it **in the cell, after the text paragraph of the cell**. Keep it small (about 300px wide) so the table stays easy to read.
- **Never** put an image in its own sub-bullet, or as the first item in a list item or table cell. Confluence deletes images in those places and does not tell you.
- Centre the image. Use the natural pixel width of the image, to a maximum of about 700px in bullets.
- Crop to the part of the screen that changed. Use demo data only. Never show real patient names.
- Upload images as page attachments first. When you move an image, use its existing media `id` and `collection` (`contentId-<pageId>`). Never invent IDs.
- When you share a draft in chat before publishing, show each screenshot as `[Screenshot: what it shows]` in the place it will go.

## Edit the Confluence page safely

Do these steps every time. Screenshots were deleted before because these steps were not done.

1. **Read first.** Get the page with `contentFormat: "adf"`. Write down the version number and each `media` node (id, collection, alt, width, height), each `embedCard` and each `table`.
2. **Write in ADF**, not HTML or markdown, when the page has images, embeds, tables or expands. ADF needs no conversion, so nothing is lost.
3. **ADF shapes to use:**
   - Expand: `{"type":"expand","attrs":{"title":"..."},"content":[...]}`
   - Bullet with a screenshot: `{"type":"listItem","content":[{"type":"paragraph",...},{"type":"mediaSingle","attrs":{"layout":"center","width":544,"widthType":"pixel"},"content":[{"type":"media","attrs":{"type":"file","id":"...","collection":"contentId-<pageId>","alt":"...","width":1000,"height":547}}]}]}`
   - Table in an expand: `{"type":"table","content":[{"type":"tableRow","content":[{"type":"tableHeader","content":[{"type":"paragraph","content":[{"type":"text","text":"What changed"}]}]}, ...]}, {"type":"tableRow","content":[{"type":"tableCell","content":[{"type":"paragraph",...},{"type":"mediaSingle",...}]}, ...]}]}`
   - The paragraph is always first in a list item or table cell. Each cell has at least one paragraph.
4. **Keep changes from other people.** If the version changed after you read it, read it again and merge. Keep layout marks (breakout), column widths and existing text.
5. **Check after you save.** Get the page again. Count `media` nodes, embeds and tables before and after. If a count is lower, fix it before you tell the user the work is done.
6. **Tell the user** the new version number and the last version before your edits, so they can go back from the page history.

## Before you publish

- Do not publish passwords, keys or real credentials. If a source document (for example an upgrade guide) has them, tell the user and use placeholders such as `<your-password>`.
- If the user asked to see the draft first, share the title, top changes and table in chat. Wait for approval.

## Checklist for a new release

- [ ] Got the version, the date or scheduled date, the how-to page, the Loom link and the screenshots, or asked for them.
- [ ] Asked which setups the release affects: the toolkit on EHR servers, the national dashboard, or both.
- [ ] Picked Layout A or B.
- [ ] The title says the main result in plain words. No vague words.
- [ ] Each bullet and table row has a bold label and follows the STE rules.
- [ ] "Leaf" and "central" never appear without their plain names.
- [ ] Upgrade steps are stated.
- [ ] Screenshots are in place for changes the user can see, after the text in their bullet or cell.
- [ ] No passwords or credentials.
- [ ] The new expand is at the top. Older expands are not changed.
- [ ] Saved in ADF, read the page again, checked media and table counts.