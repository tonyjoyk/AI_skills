---
name: nightly-meeting-notes
description: Every day at 6:30pm, turn the day's recorded Teams meetings into structured notes (from downloaded transcripts) in a local knowledge base folder.
metadata:
  summary: "Scheduled task: every evening, save notes for the day's recorded Teams meetings."
  category: Meetings and admin
---

Build structured notes for today's recorded Teams meetings and save them to the user's knowledge base. Follow these steps in order and STOP as early as possible to save tokens.

## Efficiency rules (obey strictly)
- Do the cheap discovery step first. If nothing new to process, finish immediately.
- Get each meeting's content by DOWNLOADING its transcript .docx and reading it as text — do NOT open "View recap" (the video player hangs the page) and do NOT screenshot the recap. Screenshots are the last resort only.
- Never re-process a meeting that already has a saved note.
- Use the transcript only as temporary input. Save only the structured note. Delete the downloaded .docx afterward. Never store raw transcripts in the knowledge base.

## Step 1 — Discover today's meetings (cheap, no browser)
Use outlook_calendar_search to list online meetings from today (afterDateTime "today 00:00", beforeDateTime "now") where the user was organizer or attendee. Read each event; a meeting is a candidate if it has a `meetingTranscriptUrl` or was an online Teams meeting that has ended. If there are no candidates, write nothing and finish: "No recorded meetings today." Stop.

## Step 2 — Skip ones already done
List <knowledge-base>/meeting-notes/. The note filename is `YYYY-MM-DD HHmm — {exact Teams meeting name}.md` (meeting date + start time). If it exists, skip that meeting. If all candidates are already saved, finish and stop.

## Step 3 — Download and read the transcript for each new meeting
Connect to the user's already-connected Chrome (if exactly one browser is connected, use it; do not send an interactive picker). If a browser choice or a Teams sign-in is required and can't be resolved without the user, write `<knowledge-base>/meeting-notes/_STATUS.md` saying "Nightly notes need Chrome open and signed into Teams" and finish — do not loop or screenshot repeatedly.
For each new meeting: open teams.microsoft.com → the meeting's chat → scroll to the recap card at the end → click the **Transcript** chip. This downloads `{Meeting name}.docx` to the Downloads folder. Do NOT click "View recap". Then read the newest matching .docx and extract its text:
```
python3 - <<'PY'
import zipfile, re, glob, os
f = max(glob.glob('/sessions/*/mnt/Downloads/*.docx'), key=os.path.getmtime)
xml = zipfile.ZipFile(f).read('word/document.xml').decode('utf-8','ignore')
for p in re.split(r'</w:p>', xml):
    t=''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p))
    if t.strip(): print(t)
PY
```
(Use the correct Downloads mount path for bash.) Also read the meeting Chat tab for anything the user posted (epics, tasks, open questions, Jira links). Capture verbatim: decisions, owners, file names, figures/quantities, Jira IDs, and the mm:ss timestamps. If the Transcript chip is missing or the download fails, fall back to View recap → AI summary → Expand all (slower).

## Step 4 — Structure it
Use the "meeting-summary" skill to turn each meeting into the one-screen Notion-shape action doc it defines: substance-first TL;DR; a single Action items checklist (the user's first, Jira ID trailing); 3-6 themed sections of plain bullets with bold lead-in labels and `**Decided:**` inline with a trailing (mm:ss); Open questions. No tables. Plain, direct voice (see the clear-writing skill).

## Step 5 — Save and clean up
Save each note to <knowledge-base>/meeting-notes/ as `YYYY-MM-DD HHmm — {exact Teams meeting name}.md`. Then delete the downloaded transcript .docx from Downloads.

## Step 6 — Report
Finish with one line per meeting: which notes you created, and any skipped or unreachable. Keep it short.