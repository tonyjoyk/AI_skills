---
name: "docx-styling"
description: "A general clean visual style for Word documents: a fixed teal-and-ink palette, type scale, page setup, table and code-block treatment. Use this whenever the user asks for a Word document, a .docx, a runbook, a deployment guide, a technical guide, a brief, a memo, an SOP, or a report for RTSL, H360, HEARTS360, or Simple. Also use it when the user says 'in our usual style', 'the same style as the last doc', or 'make it look like our other docs'. Apply it even if they only say 'write me a doc' without naming a style, since every RTSL Word document should look the same. This skill covers appearance only, not writing voice. For the mechanics of reading, editing, redlining, or commenting on existing .docx files, use the built-in docx skill alongside this one."
metadata:
  summary: "One clean, consistent visual style (palette, type, tables) for every Word document."
  category: Documents and visuals
---

# RTSL visual style for Word documents

Derived from the H360 AWS deployment runbook, which is the reference document.

## How to use this skill

1. Read the design tokens below.
2. Copy the builder block into a Node script. Do not retype the values.
3. Run it, render the output to images, and look at the result before handing
   it over.

The builder is tested and works. Retyping the XML or the colours by hand is how
this drifts.

---

## Design tokens

Every value is fixed. Do not invent new colours or sizes.

### Colour

| Hex | Name | Used for |
|---|---|---|
| `1b2422` | ink | body text, H2, table body text, code block text |
| `0e4a46` | deep teal | H1 text, inline code |
| `16645f` | accent teal | eyebrow line, H1 underline, bullet glyphs, code block left bar |
| `5f6c69` | grey | table header text, footer, code comments |
| `edf1f0` | header fill | table header row background |
| `f1f5f4` | code fill | code block background |
| `d4dcda` | rule | table borders, footer rule |

Seven colours. That is the whole palette.

### Type

| Element | Font | Size | Weight | Colour |
|---|---|---|---|---|
| Eyebrow | Calibri | 9pt (`18`) | bold, caps | accent teal |
| Title | Calibri | 24pt (`48`) | bold | ink |
| H1 | Calibri | 15pt (`30`) | bold | deep teal |
| H2 | Calibri | 12pt (`24`) | bold | ink |
| Body | Calibri | 10.5pt (`21`) | regular | ink |
| Inline code | Consolas | 9.5pt (`19`) | regular | deep teal |
| Table header | Calibri | 9pt (`18`) | bold | grey |
| Table body | Calibri | 9.5pt (`19`) | regular | ink |
| Table code | Consolas | 8.5pt (`17`) | regular | deep teal |
| Code block | Consolas | 9pt (`18`) | regular | ink |
| Footer | Calibri | 8pt (`16`) | regular | grey |

Sizes in brackets are docx-js half-points. Pass those, not the point values.

### Page and spacing

- A4 portrait, 11906 x 16838 twips.
- Margins 1083 twips on all four sides. Content width is exactly **9740**.
- Every table is 9740 wide. Column widths must sum to 9740.
- Body paragraphs: 140 after, line 276 (1.15).
- H1: 400 before, 160 after, 1.5pt accent rule underneath with 6 space.
- H2: 300 before, 110 after.
- Bullets: 70 after, indent left 360 hanging 220, teal glyph.
- Table cells: margins 90 top and bottom, 130 left and right.
- Code block cells: margins 120 top and bottom, 180 left and right.
- Footer: right aligned, thin rule above, text then page number.

---

## The builder

Copy this whole block into `build.js`. It is tested. Add content at the bottom.

```js
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat,
  HeadingLevel, PageNumber, Footer,
} = require("docx");
const fs = require("fs");

const C = {
  ink: "1b2422", deep: "0e4a46", accent: "16645f", grey: "5f6c69",
  headFill: "edf1f0", codeFill: "f1f5f4", rule: "d4dcda",
};
const BODY_FONT = "Calibri", CODE_FONT = "Consolas";
const CONTENT_W = 9740;
const hair = { style: BorderStyle.SINGLE, size: 4, color: C.rule };
const none = { style: BorderStyle.NONE, size: 0, color: "auto" };

const eyebrow = (t) => new Paragraph({
  spacing: { after: 200 },
  children: [new TextRun({ text: t.toUpperCase(), bold: true, color: C.accent, size: 18, font: BODY_FONT })],
});

const title = (t) => new Paragraph({
  spacing: { after: 160 },
  children: [new TextRun({ text: t, bold: true, color: C.ink, size: 48, font: BODY_FONT })],
});

const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });

// parts: a plain string, or an array mixing "plain", ["code", x], ["bold", x]
const body = (parts) => new Paragraph({
  spacing: { after: 140, line: 276 },
  children: (typeof parts === "string" ? [parts] : parts).map((p) => {
    if (typeof p === "string") return new TextRun({ text: p, color: C.ink, size: 21, font: BODY_FONT });
    if (p[0] === "code") return new TextRun({ text: p[1], color: C.deep, size: 19, font: CODE_FONT });
    return new TextRun({ text: p[1], bold: true, color: C.ink, size: 21, font: BODY_FONT });
  }),
});

const bullet = (parts) => new Paragraph({
  numbering: { reference: "house-bullets", level: 0 },
  spacing: { after: 70, line: 276 },
  children: (typeof parts === "string" ? [parts] : parts).map((p) =>
    typeof p === "string"
      ? new TextRun({ text: p, color: C.ink, size: 21, font: BODY_FONT })
      : new TextRun({ text: p[1], color: C.deep, size: 19, font: CODE_FONT })),
});

// headers: [string]; rows: [[cell]]; cell is a string, {code:"x"} or {bold:"x"}
const dataTable = (headers, rows, widths) => {
  const cellP = (c, header) => {
    let run;
    if (header) run = new TextRun({ text: String(c), bold: true, color: C.grey, size: 18, font: BODY_FONT });
    else if (typeof c === "string" || typeof c === "number")
      run = new TextRun({ text: String(c), color: C.ink, size: 19, font: BODY_FONT });
    else if (c.code) run = new TextRun({ text: c.code, color: C.deep, size: 17, font: CODE_FONT });
    else run = new TextRun({ text: c.bold, bold: true, color: C.ink, size: 19, font: BODY_FONT });
    return new Paragraph({ spacing: { after: 0, line: header ? 240 : 252 }, children: [run] });
  };
  const mkCell = (c, i, header) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    margins: { top: 90, bottom: 90, left: 130, right: 130 },
    shading: header ? { type: ShadingType.CLEAR, fill: C.headFill, color: "auto" } : undefined,
    children: [cellP(c, header)],
  });
  return new Table({
    columnWidths: widths,
    width: { size: CONTENT_W, type: WidthType.DXA },
    layout: "fixed",
    borders: { top: hair, bottom: hair, left: hair, right: hair, insideHorizontal: hair, insideVertical: hair },
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((h, i) => mkCell(h, i, true)) }),
      ...rows.map((r) => new TableRow({ children: r.map((c, i) => mkCell(c, i, false)) })),
    ],
  });
};

// lines starting with "# " render as grey italic comments
const codeBlock = (lines) => new Table({
  columnWidths: [CONTENT_W],
  width: { size: CONTENT_W, type: WidthType.DXA },
  layout: "fixed",
  borders: {
    top: none, bottom: none, right: none,
    left: { style: BorderStyle.SINGLE, size: 18, color: C.accent },
    insideHorizontal: none, insideVertical: none,
  },
  rows: [new TableRow({
    children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      margins: { top: 120, bottom: 120, left: 180, right: 180 },
      shading: { type: ShadingType.CLEAR, fill: C.codeFill, color: "auto" },
      children: lines.map((l, i) => new Paragraph({
        spacing: { after: i === lines.length - 1 ? 0 : 20, line: 240 },
        children: [new TextRun({
          text: l,
          italics: l.startsWith("# "),
          color: l.startsWith("# ") ? C.grey : C.ink,
          size: 18, font: CODE_FONT,
        })],
      })),
    })],
  })],
});

const spacer = (after = 160) => new Paragraph({ spacing: { after, line: 276 }, children: [] });

const FOOTER_TEXT = "Document name \u00b7 short descriptor";

const doc = new Document({
  styles: {
    default: { document: { run: { font: BODY_FONT, size: 21, color: C.ink } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: BODY_FONT, size: 30, bold: true, color: C.deep },
        paragraph: {
          spacing: { before: 400, after: 160, line: 240 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 12, space: 6, color: C.accent } },
        },
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: BODY_FONT, size: 24, bold: true, color: C.ink },
        paragraph: { spacing: { before: 300, after: 110, line: 240 } },
      },
    ],
  },
  numbering: {
    config: [{
      reference: "house-bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
        style: { run: { color: C.accent }, paragraph: { indent: { left: 360, hanging: 220 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1083, bottom: 1083, left: 1083, right: 1083 },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          border: { top: { style: BorderStyle.SINGLE, size: 4, space: 6, color: C.rule } },
          children: [
            new TextRun({ text: FOOTER_TEXT + "     ", color: C.grey, size: 16, font: BODY_FONT }),
            new TextRun({ children: [PageNumber.CURRENT], bold: true, color: C.grey, size: 16, font: BODY_FONT }),
          ],
        })],
      }),
    },
    children: [
      // ---- content goes here ----
      eyebrow("deployment runbook \u00b7 h360 toolkit"),
      title("Document Title in Title Case"),
      body("Opening paragraph."),
    ],
  }],
});

Packer.toBuffer(doc).then((b) => fs.writeFileSync("out.docx", b));
```

Run it, then render and look:

```bash
node build.js
python3 /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf out.docx
pdftoppm -jpeg -r 90 out.pdf page
```

Read the images. Do not skip this.

---

## Composition rules

**Eyebrow, then title.** A short uppercase kicker, two parts joined by a middle
dot. Then the title. Never a title on its own.

**Numbered H1.** "1.", "2.", with two spaces after the dot. Sub sections under
an H1 are H2 numbered "3.1", "3.2". An H2 outside a numbered run has no number.
Never go deeper than two levels.

**Two table treatments, not one.** Data tables get hairline borders all round
plus a shaded header row. Code blocks are single-cell tables with no borders
except the teal left bar and a pale fill. Do not mix them.

**Full-width tables only.** No floating, no centring, no partial widths.

**Repeat the header row.** Already set with `tableHeader: true` in the builder.
Leave it on.

**Bullets are teal glyphs from the numbering config.** Never a typed character.

**No callout boxes, panels, emoji, or coloured warning blocks.** The style has
none. Emphasis is bold text inline.

---

## Gotchas

- **`"string".bold` is truthy.** It is a legacy JavaScript String method. Any
  cell handler that checks `c.bold` before checking `typeof c === "string"` will
  silently drop every plain-text cell. The builder above tests for string first.
  Keep that order.
- **Column widths must sum to 9740.** Nothing warns you. It just renders wrong.
- **Set both `columnWidths` on the table and `width` on every cell**, both in
  DXA. Percentages break in Google Docs, and these documents get opened there.
- **Use `ShadingType.CLEAR`, never `SOLID`.** Solid renders black.
- **Never put `\n` in a TextRun.** Use one Paragraph per line.
- **Do not use a table as a horizontal rule.** The H1 style already has one.
- **Border `size` is in eighths of a point.** 4 is 0.5pt, 12 is 1.5pt, 18 is
  2.25pt.

## Before handing it over

Render it and look at the pages. Check the four things that break most often:
the H1 rule is present and teal, table columns line up, code blocks have the
left bar and no other border, and the footer shows the page number.