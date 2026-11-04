# Kestrel Localization Run

**Live:** https://dekelgit2026.github.io/Marketing-live-run-/

An interactive walkthrough of a **Solution Design v1**, built for Meeting 4 of the AI Solutions Architect course (Product Experts).

The design covers campaign localization with brand guardrails. It was produced by the six design commands in the `m04-design-kit`: `/spec`, `/pattern`, `/flow`, `/cost`, `/testset` and `/design-check`. This page shows that design running.

| Tab | What it shows |
|---|---|
| **Live run** | Three demo briefs go through the six workflow stations. Toggle between a **Flow** view and an **Architecture** view; a "you are here" marker follows the run, and a map shows each market's status. The rule checks are real code, so you can edit the copy and watch the flags change. |
| **Month-1 sample** | A simulated blind A/B comparison of 120 pieces, by market (map) and by medium (sensitivity bars and heatmap), checked against the spec's decision rule. |
| **Scope** | The "It will NOT…" fences, and what enforces each one. |
| **Pattern** | The pattern ladder and why the design stops at rung 1 + 2. |
| **Proof** | The 18-case golden test set against the ship bar. |

**What's real and what's simulated:**
- **Real:** the rule checks, the brand rules, the workflow and architecture, and the test cases. They come from the design files.
- **Simulated:** the AI drafts (pre-written, so the demo never stalls), the month-1 sample numbers and the test results. The page labels these.

## Run it locally
Open `index.html` in a browser. There's no server and no build step.

## Host it on GitHub Pages
This repo is already hosted: **https://dekelgit2026.github.io/Marketing-live-run-/**

To host your own copy:
1. On github.com, create a new **public** repository. Don't add a README.
2. Push this folder:
   ```
   git remote add origin https://github.com/<you>/<repo-name>.git
   git push -u origin main
   ```
3. In the repository, go to **Settings → Pages**. Under **Build and deployment**, set the source to **Deploy from a branch**, the branch to **main** and the folder to **/ (root)**, then **Save**.
4. After about a minute the site is live at `https://<you>.github.io/<repo-name>/`.

Every later push to `main` updates the live site.

## Update the content
- **New test cases:** after re-running `/testset`, rebuild with the new file. This needs only Python's standard library:
  ```
  python build.py path/to/designs/marketing/testset.csv
  ```
- **Layout, briefs, stations or architecture text:** edit `src/template.html`, then run `python build.py`.
- **Never edit `index.html` by hand.** It is generated from `src/template.html` and `data/`.

```
src/template.html      the page, with placeholders for the data
data/tests.json        the test cases shown on the Proof tab (made from testset.csv)
data/testset.csv       the source test set, from /testset
data/world-dots.json   dotted world map
data/europe-dots.json  dotted Europe map, used when zoomed in
build.py               inlines the data and writes index.html
index.html             the built page that GitHub Pages serves
```

## Credits and notes
- Kestrel Analytics, its products, briefs, competitors and people are **fictional**. All examples are anonymized course material.
- Map dots are derived from **Natural Earth** (public domain).
- Fonts come from Google Fonts (Plus Jakarta Sans, Source Sans 3, JetBrains Mono). Without internet access, the page falls back to system fonts.
