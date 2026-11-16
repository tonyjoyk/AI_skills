---
name: "meeting-summary"
description: "Turn a Teams meeting transcript into an action-first notes doc, in the clean Notion meeting-notes shape. Use when the user asks for \"action items and notes from the [meeting]\", to \"summarize the [X] meeting\", \"pull the transcript\", \"meeting notes from Teams\", or any post-meeting write-up of an RTSL/HEARTS360 planning or engineering call. Do NOT use for live note-taking during a meeting."
metadata:
  summary: "Turn a Teams meeting transcript into an action-first, one-screen notes doc."
  category: Meetings and admin
---

# RTSL Meeting → Action Doc (Notion shape)

Turn a recorded Teams meeting into a clean, scannable notes page — modeled on how Notion AI writes meeting notes. Lead with substance and actions, then a tidy themed body. One consistent shape, no visual clutter.

## The one principle (anti-drift rule)
**If a line doesn't change what the user does next, or something they'd have to defend, cut it.** Every bullet earns its place. Detail is fine when it's clean; noise is not.

## Step 1 — Get the transcript (download the .docx — this is the efficient path)

The verbatim transcript downloads as a Word file with speaker names and timestamps. Reading that file is far cheaper and more accurate than screenshotting the recap. Do this:

1. Find the meeting with outlook_calendar_search (title). Read the event for the exact name, date, start time, duration, and attendees.
2. In the connected Chrome, open `teams.microsoft.com` → the meeting's chat. Scroll to the recap card at the end of the chat.
3. Click the **Transcript** chip on that recap card. This downloads the transcript to the user's Downloads folder as `{Meeting name}.docx`. **Do not click "View recap"** — that opens the video player and hangs the page.
4. Read the downloaded `.docx` from the Downloads folder. Extract text with this (no extra installs needed):
   ```
   python3 - <<'PY'
   import zipfile, re, glob, os
   f = max(glob.glob('/sessions/.../Downloads/*.docx'), key=os.path.getmtime)  # newest docx
   xml = zipfile.ZipFile(f).read('word/document.xml').decode('utf-8','ignore')
   for p in re.split(r'</w:p>', xml):
       t = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p))
       if t.strip(): print(t)
   PY
   ```
   (Use the bash mount path for Downloads. Match the file by the meeting name or newest-modified.)
5. Also read the meeting **Chat** tab for anything the user posted (epics, tasks, open questions, Jira links).
6. **Fallback only if the Transcript chip is unavailable or the download fails:** open View recap → AI summary → Expand all and read the topic notes + Follow-up tasks. This is slower and costs screenshots — use it only as a backup.

Capture verbatim from the transcript: decisions, owners, file names (`mapping.yaml`), figures/quantities ("~10M patients", "SHA-256"), Jira IDs, and the `mm:ss` timestamps that precede each turn. **Use the transcript only as temporary input, then discard it — never save the raw transcript or the .docx into the knowledge base. Delete the downloaded .docx when done.**

## Step 2 — Write the doc in this exact shape

```
# {Meeting name} — {date}
{attendees} · {duration} · [recap]({link})

## TL;DR
{2-4 plain sentences of real substance. Lead with the single biggest decision or outcome, then the next. Name concrete things, not counts. End with the one or two things the user owns.}

## Action items
- [ ] {Owner} to {specific thing, with the quantity/target} — {H360-xxx | needs ticket}

## {Theme header}
- **{lead-in label}:** {the point, concrete}. {(mm:ss) if it's a decision}
- **Decided:** {what}, because {why}. ({mm:ss})

## {next theme header}
- ...

## Open questions
- {question} — needs {name}
```

Shape rules — this is what keeps it clean:
- **One Action Items list**, not three. Every action is a checkbox `- [ ]` starting with the owner. the user's items first, then everyone else's. Jira ID or "needs ticket" at the end after a `—`. Ticket-worthy work lives here, not in a separate table.
- **No tables. Ever.** The body is plain bullets only.
- **Every body bullet starts with a bold lead-in label**, then the detail.
- **Decisions live inside the relevant theme**, flagged `**Decided:**`, with the reason and a trailing timestamp `(mm:ss)`.
- **Timestamps go only on decisions and hard facts**, trailing in parentheses. Never a column, never on every line.
- **3-6 theme sections.** Group related points. More than 6 means you're over-splitting — merge.
- Key facts (hostnames, figures, file names) are bold-label bullets inside the right theme — not a separate section.
- Omit any section that would be empty.

## Step 3 — Wording (clear-writing voice)
- Lead with the verb that matters: an action is `{Owner} to {do X}`; a decision is `Decided: {what}`. Never "discussed", "explored", "emphasized the need".
- **Name the concrete thing with its number — non-negotiable.** "~10 facilities, ~100 patients each", `mapping.yaml`. Kill category nouns ("strategies", "tools", "support").
- One idea per line. Active voice. Plain 8th-grade words. No hedging. No em dashes.
- Every action names an owner; add a date when one was given.
- If a topic settled nothing, it's an Open question, not a Decision.

## Step 4 — Deliver
- Save as Markdown in the user's connected folder and present it. For the knowledge base, that's `<knowledge-base>/meeting-notes/` named `YYYY-MM-DD HHmm — {exact Teams meeting name}.md`.
- Delete the temporary transcript .docx.
- Offer, in one line, to create/update the Jira tickets or push the doc to Notion.

## Self-check before delivering
1. Is the TL;DR real substance (the actual decisions), not counts?
2. Is there exactly one Action Items list, checkboxes, owner-first, the user's items first?
3. Are there any tables? Delete them — plain bullets only.
4. Does every body bullet start with a bold label?
5. Are timestamps only on decisions and hard facts, trailing, never a column?
6. Are there 6 or fewer theme sections?
7. Did you delete the downloaded transcript and save only the structured note?

