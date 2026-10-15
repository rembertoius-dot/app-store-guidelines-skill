# app-store-guidelines

A skill for Claude (and any agent that reads `SKILL.md`) that carries Apple's App Store rules
locally: the asset best practices, the exact screenshot and app preview specifications, and the
full App Store Review Guidelines, so the agent quotes the real rule and number instead of
remembering an old one.

## Install

```bash
npx skills add rembertoius-dot/app-store-guidelines-skill
```

Then ask Claude things like *"check my screenshots before I submit"*, *"what size do iPhone
screenshots need to be?"*, *"we got rejected under 2.3.8, what does it say?"* or *"review my
App Store metadata"*.

## What's inside

- `skills/app-store-guidelines/SKILL.md`: quick reference (required sizes, preview limits, what can
  never appear in an asset), a table mapping common asset problems to the guideline to cite, a
  pre-submission checklist and the mistakes the model makes from memory.
- `references/asset-best-practices.md`: Apple's guidance per asset type (icon, product page header,
  search results creative, In-App Events, screenshots, app previews) and per format (image, video).
- `references/screenshot-specs.md`: every accepted pixel size for iPhone, iPad, Mac, Apple TV,
  Apple Vision Pro and Apple Watch, the required sets and the fallback chain.
- `references/app-preview-specs.md`: video length, file size, codec, audio and accepted resolutions.
- `references/review-guidelines.md`: the App Store Review Guidelines, verbatim, as Markdown with one
  searchable line per numbered rule.

The Apple text is © Apple Inc. and is not under this repo's license; see `NOTICE`. The copy was
captured on 2026-10-15 (the guidelines page says "Last Updated: June 8, 2026"). The skill tells the
agent to confirm against the live page before quoting a rule back to Apple.

## Why

Asked without this skill, a fresh agent named the wrong required iPhone screenshot size, used
inch-based names Apple no longer uses, missed the iPhone Duo requirement, misquoted the last
sentence of guideline 2.3.8 and missed 5.2.4 for a fake award badge. With the skill it answered
every number and quote correctly from the files.

## Keeping it current

```bash
python3 scripts/refresh.py
```

Re-downloads the four pages. It regenerates `review-guidelines.md` in place and writes the raw
text of the other three pages to `scripts/raw/` (git-ignored) so you can diff them against the
hand-written spec and best-practice files and update any size or rule that changed.

## Related

`apple-appstore-reviewer` from [github/awesome-copilot](https://github.com/github/awesome-copilot)
audits a codebase from a reviewer's point of view. This skill is the rulebook it can cite from.
