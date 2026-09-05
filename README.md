# prabhavarma.in — v1 (static)

Plain HTML/CSS/JS, no build step. Deploy on Vercel by dropping this folder in a repo
(`vercel --prod` or connect the repo). `vercel.json` gives clean URLs (/works, /honours …).

## To add
- `images/portrait.jpg` (3:4, ≥1200px) — hero portrait. Placeholder shows until present.
- `images/shyama-madhavam.jpg`, `kanal-chilambu.jpg`, `roudra-sathwikam.jpg`, `adayala-vakyam.jpg` — covers (2:3).
- Malayalam originals of the three excerpts on `writings.html` and in the home verse band
  (`[ശ്യാമമാധവം — മൂലം …]` placeholder).
- Full text of the ONV / Leelavathy / Jayakumar essays and the Akademi speech (with permission).
- Recording links on `stage.html` (YouTube embeds replace the three placeholders).

## Regenerating pages
Pages are generated from `build_site.py` (kept alongside the site). Edit content there,
run `python3 build_site.py`, commit. Every text node is bilingual: `b("English", "മലയാളം")`.

## Review before launch
All Malayalam copy is a first draft for the poet's review. Facts to confirm: birth date
(dossier 1958 vs Wikipedia 30 May 1959), dates of individual awards, current designation.
