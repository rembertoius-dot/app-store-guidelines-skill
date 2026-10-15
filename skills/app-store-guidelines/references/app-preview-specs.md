# App preview (video) specifications

Source: https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications (captured 2026-10-15). Confirm against the live page before a submission.

## Limits

| Item | Value |
|---|---|
| Count | Optional. Up to **3 app previews per device size and language** (iOS, macOS, tvOS, visionOS). Not available for iMessage apps. |
| Length | **15 s minimum, 30 s maximum** |
| File size | **500 MB maximum** |
| Frame rate | **30 fps maximum** |
| Formats | `.mov`, `.m4v`, `.mp4` (H.264); `.mov` only for ProRes 422 (HQ only) |
| Orientation | iOS: portrait or landscape (rotates to original orientation on play). macOS, tvOS, visionOS: landscape only |
| Poster frame | You pick it in App Store Connect; default is the frame at **5 s**. It is shown on the product page and during install, so choose it deliberately. |
| Processing | Up to **24 hours** after upload |
| Display order | Previews always appear **before** screenshots. A preview whose aspect ratio differs from the screenshots is moved to the "A Closer Look" section. |
| Scaling | Same as screenshots: upload the highest required resolution and it scales down; missing locales fall back to the next best language. |
| Content rule | Guideline 2.3.4: previews may only use **screen captures of the app itself**. Narration, text and video overlays are allowed to explain things. Stickers/iMessage extensions may show the Messages app. |

## Encoding

| | H.264 | ProRes 422 (HQ only) |
|---|---|---|
| Target bit rate | 10–12 Mbps | VBR ~220 Mbps |
| Video | Progressive, up to High Profile Level 4.0 | Progressive, no external references |
| Max frame rate | 30 fps | 30 fps |
| Audio codec | 256 kbps AAC | PCM (16/24/32-bit) or 256 kbps AAC |
| Sample rate | 44.1 or 48 kHz | 44.1 or 48 kHz |
| Channels | Stereo: 1 track with 2 channels (L, R) **or** 2 mono tracks (track 1 = L, track 2 = R). All tracks enabled. | same |
| Extensions | `.mov`, `.m4v`, `.mp4` | `.mov` |

## Accepted resolutions

Use the **accepted** resolution, not the device's native resolution. App Store Connect accepts one standard size per display class because most previews are screen recordings.

| Display class | Accepted (portrait / landscape) | Fallback if missing |
|---|---|---|
| iPhone Duo | `886×1920` / `1920×886` | — |
| iPhone with Dynamic Island, large (Air, 18/17/16/15/14 Pro Max, 16/15 Plus) | `886×1920` / `1920×886` | Face ID large |
| iPhone with Face ID, large (14 Plus, 13/12/11 Pro Max, 11, XS Max, XR) | `886×1920` / `1920×886` | Dynamic Island large |
| iPhone with Dynamic Island, medium (18/17/16/15/14 Pro, 17, 16, 15) | `886×1920` / `1920×886` | Face ID large |
| iPhone with Face ID, medium (17e, 16e, 14, 13 family, 12 family, 11 Pro, XS, X) | `886×1920` / `1920×886` | Dynamic Island medium |
| iPhone with Home button, large (8/7/6S/6 Plus) | `1080×1920` / `1920×1080` | Face ID medium |
| iPhone with Home button, medium (SE 2/3, 8, 7, 6S, 6) | `750×1334` / `1334×750` | Home button large |
| iPhone with Home button, 4" (SE 1, 5S, 5C, 5) | `640×1136` / `1136×640` | Home button medium |
| iPad 13" | `1200×1600` / `1600×1200` | — |
| iPad 12.9" | `1200×1600` / `1600×1200` or `900×1200` / `1200×900` | 13" |
| iPad 11" | `1200×1600` / `1600×1200` | 13" |
| iPad 10.5" | `1200×1600` / `1600×1200` | 12.9" |
| iPad 9.7" | `900×1200` / `1200×900` | 10.5" |
| Mac | `1920×1080` landscape | — |
| Apple TV | `1920×1080` landscape | — |
| Apple Vision Pro | `3840×2160` landscape | — |

All modern iPhones (Face ID, Dynamic Island, Duo) share **`886×1920` portrait, 19.5:9**. One file covers them all.

## Practical recipe

1. Record the real app with a screen recording at the device's native size; do not mock the UI (2.3.4).
2. Edit to 15–30 s, 30 fps, with a strong first 3 seconds and a seamless loop (it autoplays muted and repeats).
3. Export H.264 `.mp4`, 10–12 Mbps, 256 kbps stereo AAC at 48 kHz, scaled to the accepted resolution (`886×1920` for iPhone, `1200×1600` for iPad).
4. Upload, then set the poster frame; don't leave the 5 s default unless it is the best frame.
5. Allow up to 24 h processing before the preview appears.
