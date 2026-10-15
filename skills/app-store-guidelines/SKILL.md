---
name: app-store-guidelines
description: Use when creating, reviewing or fixing App Store assets (screenshots, app previews, app icon, product page header, search results creative, In-App Events media) or metadata (app name, subtitle, keywords, description, What's New, review notes), when checking an app or a feature against the App Store Review Guidelines before submitting, or when answering an App Review rejection that cites a guideline number. Also use for exact screenshot and app preview pixel sizes, lengths, formats and counts for iPhone, iPad, Mac, Apple TV, Apple Vision Pro and Apple Watch.
---

# App Store guidelines

Local copy of three Apple pages: the asset best practices, the screenshot and app preview specifications, and the full App Store Review Guidelines. **Answer from these files, not from memory.** Model memory of this material is stale (old display names, wrong required size, misquoted rules). Quote the guideline number and its text from `references/review-guidelines.md`; before sending a quote to Apple, confirm it against the live page.

## When to use
- Making or auditing screenshots, previews, icons, header or search creative, In-App Events media.
- Writing or reviewing app name, subtitle, keywords, description, What's New, promotional text, IAP display names.
- Pre-submission check of a feature, business model, login, privacy or kids-related behavior.
- Replying to a rejection: find the cited number, read the exact rule, map it to the fix.
- Not for: auditing a codebase end to end (use apple-appstore-reviewer; it should cite rules from this skill's reference), Google Play, or marketing outside the App Store.

## Files
| File | Use it for | Find things with |
|---|---|---|
| `references/review-guidelines.md` | Verbatim App Review Guidelines (sections 1–5, Before/After You Submit) | Rules are either bold inline (`**2.3.8**`) or headings (`#### 5.1.4`), so search both: `grep -nE "^\*\*5\.1\.4\*\*|^#+ 5\.1\.4"` |
| `references/screenshot-specs.md` | Required sets, every accepted pixel size, fallbacks | search the device name |
| `references/app-preview-specs.md` | Video length, size, codec, audio, accepted resolutions | — |
| `references/asset-best-practices.md` | Apple's guidance per asset type and format | search the asset name |

## Quick reference (as of 2026-10-15)
| Question | Answer |
|---|---|
| Required iPhone screenshot set | iPhone with Dynamic Island, **medium** display: `1179×2556` or `1206×2622` (landscape swapped). Large-display set (`1260×2736`, `1290×2796`, `1320×2868`) accepted instead and scales down. |
| Required iPad set | 13": `2064×2752` or `2048×2732`. Only if the app runs on iPad. |
| iPhone Duo | Outer `1398×2034`, inner `2007×2853`. Required from April 2027 for iOS 27.1 SDK+. |
| Screenshot count / format | 1–10 per device size; JPEG or PNG; no alpha. |
| App preview | Up to 3 per size and language; 15–30 s; ≤500 MB; ≤30 fps; H.264 `.mp4/.mov/.m4v` 10–12 Mbps or ProRes 422 HQ `.mov`; stereo 256 kbps AAC at 44.1/48 kHz; iPhone `886×1920`, iPad `1200×1600`, Mac/TV `1920×1080`, Vision Pro `3840×2160`. Poster frame defaults to 5 s. |
| Never in any asset | Prices/discounts, URLs, © symbols; unverifiable awards; other platforms' names or logos; Editor's Choice / App of the Day / Game of the Day / Apple Design Award badges; anything above a 4+ rating; gore or a weapon aimed at a person or the viewer; real people's account data; login, splash or title art as the screenshot. |
| App name limit | 30 characters (2.3.7). "For Kids"/"For Children" only in the Kids Category (2.3.8, 5.1.4). |

## Asset problem → guideline
| Seen in asset or metadata | Cite |
|---|---|
| Login screen, splash, title art as a screenshot | 2.3.3 |
| Preview that is not a screen capture of the app | 2.3.4 |
| Price, "limited time", terms, keyword stuffing, trademarks, other app names | 2.3.7 |
| Gun aimed at a character or viewer, gore, anything above 4+ | 2.3.8 |
| Real person's data, unlicensed images or music | 2.3.9, 5.2.1 |
| Google Play / other platform logos or mentions | 2.3.10 |
| Fake award, "Apple Design Award", implied Apple endorsement | 5.2.4(a), 2.3.1(a); Editor's Choice badge is applied by Apple only, 5.2.4(b) |
| IAP-gated content shown as if free | 2.3.2 |
| Imitating another app's icon, brand or name | 4.1(c), 5.2.1 |
| Mimicking an Apple app, Apple emoji in assets, Activity rings look-alike | 5.2.5 |
| Kid-targeted wording outside the Kids Category | 2.3.8, 5.1.4 |
| In-App Event media about the app in general, wrong dates, bad deep link | 2.3.13 |

## Workflow
1. Name the task: new asset, metadata review, pre-submission check, or rejection reply.
2. Open the matching reference file. For a rejection, grep the cited number and read the whole section around it, plus the "Before You Submit" list.
3. For sizes, copy the exact pixel values from the spec file; name display classes the way Apple does (Dynamic Island medium/large, Face ID, Home button), not by inches.
4. Report each finding as: what is wrong, the guideline number, the quoted rule, the fix.
5. Before submitting: run the checklist below and view everything in the App Store Connect Preview tool.

## Pre-submission asset checklist
- Screenshots at an accepted size for every required class, no alpha, app in use, best feature first, text short and localized, focal point centered in the safe area.
- Previews 15–30 s, real screen capture, strong first seconds, clean loop, works muted, poster frame chosen.
- Icon legible at every size; built with Icon Composer for Liquid Glass.
- Header and search creative: one idea each, same palette and type as the rest, designed for a first-time visitor.
- In-App Events: both 16:9 and 9:16 media, complements the badge.
- Metadata: name ≤30 chars, no prices or claims, IAP requirements disclosed, honest age rating, specific What's New, review notes describe every non-obvious feature, demo account or demo mode, backend live.

## If a code audit cites these rules, check them here first
Two rules in common audit checklists (including apple-appstore-reviewer) are older than Apple's current text:
- **4.8 Login Services.** Not "Sign in with Apple is required". Any equivalent login that limits data to name and email, lets users hide their email, and doesn't collect interactions for ads without consent satisfies it.
- **3.1.1(a) / 3.1.3 External purchase links.** On the United States storefront, buttons and links to other purchase methods are allowed without an entitlement. The blanket "no external purchase links" finding applies to other storefronts only.

## Common mistakes
- Quoting a guideline from memory. The last sentence of 2.3.8 is about keeping icons and names consistent, not a generic "no objectionable content" line; read the file.
- Calling the required size "6.9 inch" or "6.7 inch". Apple's page names classes by Dynamic Island / Face ID / Home button and requires the **medium** Dynamic Island set.
- Rendering previews at the screenshot size. Previews use the accepted resolution (`886×1920` on every modern iPhone).
- Treating the asset best practices as advice only. "Focus on your core experience" and "4+ for every asset" are enforced through 2.3.
- Forgetting the fallback chain: a missing size silently reuses a scaled neighbor, which may crop differently.
