# Screenshot specifications (App Store Connect)

Source: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications (captured 2026-10-15). Confirm against the live page before a submission; Apple adds sizes with each device generation.

## Rules that apply to every screenshot

- At least 1 and at most **10 screenshots per device size**, in **.jpeg, .jpg or .png**.
- **No alpha channel / transparency.**
- Every screenshot must follow the App Review Guidelines (2.3.3: show the app in use, not title art, login or splash; 2.3.8: 4+ age rating; 2.3.9: rights to all materials, fictional account data; 2.3.10: no other platforms).
- **Scaling:** if the UI is the same across sizes and locales, upload only the highest required resolution. App Store Connect scales it down for smaller devices. Upload per-size or per-locale sets only when you want control.
- **Fallback chain:** when a size is missing, App Store Connect uses the scaled set from the next size in the chain noted under each row below.

## Required sizes

| App runs on | Required set |
|---|---|
| iPhone | iPhone with Dynamic Island (**medium** display): one of `1179×2556`, `1206×2622` portrait (or landscape equivalents). Large display set accepted instead. |
| iPad | iPad **13"** display: `2064×2752` or `2048×2732` portrait (or landscape). |
| Mac | Mac, 16:10: `1280×800`, `1440×900`, `2560×1600` or `2880×1800`. |
| Apple TV | `1920×1080` or `3840×2160`. |
| Apple Vision Pro | `3840×2160`. |
| Apple Watch | One size, used consistently across all localizations (see table). |
| iPhone Duo | Not required yet. From **April 2027** required for apps built with the **iOS 27.1 SDK or later**. |

## iPhone

| Display class | Devices | Accepted sizes (portrait / landscape) | Fallback if missing |
|---|---|---|---|
| iPhone Duo | iPhone Duo | Outer: `1398×2034` / `2034×1398`. Inner: `2007×2853` / `2853×2007` | (new; required April 2027 for iOS 27.1 SDK+) |
| Dynamic Island, large | iPhone Air, 18 Pro Max, 17 Pro Max, 16 Pro Max, 16 Plus, 15 Pro Max, 15 Plus, 14 Pro Max | `1260×2736` / `2736×1260`; `1290×2796` / `2796×1290`; `1320×2868` / `2868×1320` | Face ID large |
| Face ID, large | 14 Plus, 13 Pro Max, 12 Pro Max, 11 Pro Max, 11, XS Max, XR | `1284×2778` / `2778×1284`; `1242×2688` / `2688×1242` | Dynamic Island large |
| **Dynamic Island, medium (required)** | 18 Pro, 17 Pro, 17, 16 Pro, 16, 15 Pro, 15, 14 Pro | `1179×2556` / `2556×1179`; `1206×2622` / `2622×1206` | Face ID large |
| Face ID, medium | 17e, 16e, 14, 13 Pro, 13, 13 mini, 12 Pro, 12, 12 mini, 11 Pro, XS, X | `1170×2532` / `2532×1170`; `1125×2436` / `2436×1125`; `1080×2340` / `2340×1080` | Dynamic Island medium |
| Home button, large | 8 Plus, 7 Plus, 6S Plus, 6 Plus | `1242×2208` / `2208×1242` | Face ID medium |
| Home button, medium | SE (2nd, 3rd gen), 8, 7, 6S, 6 | `750×1334` / `1334×750` | Home button large |
| Home button, 4" | SE (1st gen), 5S, 5C, 5 | `640×1096` (no status bar) or `640×1136` (with); landscape `1136×600` / `1136×640` | Home button medium |
| Home button, 3.5" | 4S, 4 | `640×920` / `640×960`; landscape `960×600` / `960×640` | Home button 4" |

## iPad

| Display | Devices | Accepted sizes (portrait / landscape) | Fallback if missing |
|---|---|---|---|
| **13" (required if app runs on iPad)** | iPad Pro (M5, M4), iPad Pro 1st–6th gen 12.9", iPad Air (M4, M3, M2) | `2064×2752` / `2752×2064`; `2048×2732` / `2732×2048` | — |
| 12.9" | iPad Pro (2nd gen) | `2048×2732` / `2732×2048` | 13" |
| 11" | iPad Pro (M5, M4), iPad Pro 11" 1st–4th gen, iPad Air (M4, M3, M2, 5th, 4th gen), iPad (A16, 10th gen), iPad mini (A17 Pro, 6th gen) | `1488×2266` / `2266×1488`; `1668×2420` / `2420×1668`; `1668×2388` / `2388×1668`; `1640×2360` / `2360×1640` | 13" |
| 10.5" | iPad Pro 10.5", iPad Air (3rd gen), iPad (7th–9th gen) | `1668×2224` / `2224×1668` | 12.9" |
| 9.7" | iPad Pro 9.7", iPad Air, iPad Air 2, iPad, iPad 2, iPad (3rd–6th gen), iPad mini 2/3/4/5th gen | `1536×2008` (no status bar) or `1536×2048` (with); landscape `2048×1496` / `2048×1536`; or `768×1004` / `768×1024`; landscape `1024×748` / `1024×768` | 10.5" |

## Mac, Apple TV, Apple Vision Pro

| Platform | Accepted sizes | Requirement |
|---|---|---|
| Mac | 16:10 only: `1280×800`, `1440×900`, `2560×1600`, `2880×1800` | Required for Mac apps |
| Apple TV | `1920×1080`, `3840×2160` | Required for Apple TV apps |
| Apple Vision Pro | `3840×2160` | Required for visionOS apps |

## Apple Watch

Pick **one** size and use it for every localization.

| Size | Models |
|---|---|
| `422×514` | Ultra 4, Ultra 3 |
| `410×502` | Ultra 2, Ultra |
| `416×496` | Series 12, 11, 10 |
| `396×484` | Series 9, 8, 7 |
| `368×448` | Series 6, 5, 4, SE 3, SE 2, SE |
| `312×390` | Series 3, 2, 1 |

## Practical minimum set for a new app

- iPhone-only app: one set at `1179×2556` (Dynamic Island medium, the size Apple labels required) **or** `1290×2796` (Dynamic Island large, accepted in its place and scaled down to everything). Either satisfies the requirement.
- iPhone + iPad: add a `2064×2752` (or `2048×2732`) iPad 13" set.
- Rendering tip: build screenshots at the device's native pixel size listed above, export PNG without alpha (flatten on a solid background), and check them in the App Store Connect Preview tool before submitting.
