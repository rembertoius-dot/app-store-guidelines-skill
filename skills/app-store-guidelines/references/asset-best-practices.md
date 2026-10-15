# App Store asset best practices (Apple)

Source: https://developer.apple.com/app-store/asset-best-practices/ (captured 2026-10-15). Apple's own guidance on what makes an asset effective and what it evaluates when deciding what to feature. Policy rules live in the App Review Guidelines (section 2.3 Accurate Metadata) and the Apple Advertising Policies (https://developer.apple.com/app-store/marketing/guidelines/).

## Asset types

| Asset | What it is | Where it shows |
|---|---|---|
| App icon | The app's identity | App Store, Spotlight, Home Screen |
| Screenshots | Static images of the app in use (up to 10) | Product page; up to 3 in search results depending on orientation |
| App previews | 15–30 s videos of the app in use (up to 3) | Product page, before screenshots; up to 3 in search results |
| Product page header | Creative asset (image or video) at the top of the product page | Product page (iOS 27 / iPadOS 27 and later) |
| Search results creative | Creative asset shown in the Search tab | Search results; if absent, In-App Events, previews and screenshots show instead |
| In-App Events media | 16:9 event card + 9:16 event details page | Today tab, search, product page |
| Universal creative asset | One asset reused for header and search results | Both, for brand consistency |

Creative assets (header, search results, universal) are new with iOS 27 / iPadOS 27 and are managed in the **Asset Library** in App Store Connect.

## Policy-level rules for every asset (Apple's words, condensed)

**Focus on your core experience.** Content outside the app may appear only if it relates to the app's actual functionality.
- No specific pricing, discounts, website URLs or copyright symbols (keeps assets global and evergreen).
- No claims that can't be verified, such as awards the app didn't receive.
- No logos or references to other platforms or marketplaces.
- No Apple-designated recognitions: Editor's Choice, App of the Day, Game of the Day, Apple Design Award winner. Apple shows these itself.

**Design with all customers in mind.**
- Build for a global audience: inclusive imagery; localize metadata, images and videos per region.
- Create for all ages: **every asset must meet a 4+ age rating even if the app is rated higher.** No explicit or harmful imagery, profanity, illegal drugs, self-harm, hate speech, stereotypes, sexually suggestive content, inflammatory religious commentary, or misleading religious quotations.
- Keep violence in check: games may use action imagery but no gore, graphic imagery, or weapons pointed directly at a person or at the viewer.

## Format best practices

### Images
- **Compelling visuals.** Photography, illustration and graphics should feel current; use the latest UI and the app's own aesthetic. Strong composition, one clear focal point per asset.
- **Intentional text.** Text should enhance the visual, not describe it. Short phrases. Overlays may demonstrate input (touch point, Apple Pencil) or highlight a feature. Localize every supported language.
- **Legibility.** Key elements, especially text, must stay readable wherever the asset appears. Keep the focal point in the center and inside a safe area so cropping across devices and orientations doesn't clip it. Check with the **Preview tool in App Store Connect** before going live.

### Videos
- **Poster frame.** It is the first thing people see; pick a frame that represents the app and stands on its own.
- **Start strong.** Lead with the value proposition or best feature. Pace cuts so people can follow; avoid quick cuts and fast motion (hard to follow, not accessible to everyone).
- **Loop seamlessly.** Videos autoplay and repeat; no visible jump at the loop point.
- **Audio is muted by default.** The video must work silently. If adding sound, treat it as brand texture, not information: a short music loop over heavy sound effects, no sudden loud moments, audio that loops cleanly.

## Asset-specific guidance

Collectively the assets should tell one cohesive story: same palette, iconography, fonts, message and tone.

### App icon
- Unique, expressive of purpose and personality, recognizable at a glance.
- Use **Icon Composer** to produce layered Liquid Glass icons from one design for iPhone, iPad, Mac and Apple Watch.
- Legible at every size: App Store, Spotlight, Home Screen.
- HIG: https://developer.apple.com/design/human-interface-guidelines/app-icons

### Product page header
- The first thing a visitor notices. Use it to set tone: brand, seasonal offer, new content.
- One single, clear idea; dense or cluttered assets dilute impact.
- Design for a first-time visitor: what is most compelling to someone who has never seen the app?
- A **universal creative asset** can serve both header and search results. **Product page optimization** can A/B test alternative headers.
- Templates: Figma (universal), Photoshop (header, universal), Pixelmator (header, universal), Sketch (universal), linked from the source page.

### Search results creative
- Seen before the product page, by people looking for something specific.
- **State the obvious:** the app's purpose must be clear at a glance.
- **Show the firsthand experience:** interface, content or gameplay.
- Without one, In-App Events, app previews and screenshots appear in search instead.
- Search docs: https://developer.apple.com/app-store/discoverability/

### In-App Events
- Timely, limited-time moments: competitions, premieres, live experiences, seasonal launches.
- Supply media for **both** the event card (**16:9 landscape**) and the event details page (**9:16 portrait**); keep colors and illustration style consistent across the two.
- The badge (Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event) already names the event type; the media should complement it, not repeat it.
- Guideline 2.3.13 governs event metadata and deep links. Docs: https://developer.apple.com/app-store/in-app-events/

### Screenshots
- Up to **10** on the product page; up to **3** in search results depending on orientation.
- **Show what people can expect:** the app in use, a clear, detailed view of the experience. Don't spend a whole screenshot on accolades or a call-to-action.
- **Lead with your best features,** sequenced into a story that mirrors how someone would actually use the app.
- Specs: see screenshot-specs.md. Product page guide: https://developer.apple.com/app-store/product-page/

### App previews
- Up to **3** on the product page; up to **3** may appear in search results.
- **Real UI or gameplay** only; compelling visuals in the first few seconds.
- **Tell a complete story:** beginning, middle, end. For example, top features in order of popularity, or levels in order of progression.
- Specs: see app-preview-specs.md.

## Submitting and testing assets
- Submit in App Store Connect with a new version or via the **Asset Library**, or through the App Store Connect API. Approved assets land in the Asset Library, which also shows where each asset can be used.
- Use the **product page preview tool** to see header, app name, description, screenshots and search results creative together before publishing.
- Beyond the default page: **custom product pages** (creative assets per audience), **product page optimization** (A/B tests), and the promotion tools at https://developer.apple.com/app-store/promote/.
- Related sessions: "Enhance your presence on the App Store" (WWDC26 session 205), "Say hello to the new look of app icons" (WWDC25 session 220), "Icon Composer for Beginners" (WWDC26 group lab 8012).
