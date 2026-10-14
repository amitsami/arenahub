# ArenaHub — Tournament Command

![ArenaHub gaming arena](assets/arena-hero.webp)

**Your arena. Your rules.** A customizable, responsive tournament command center built with vanilla HTML, CSS and JavaScript. No fixed eight-team setup, no seeded demo records, no build dependencies.

> **Local-first frontend:** records stay in your current browser. Organizer/captain/spectator modes are interface views—not authenticated accounts or access controls. This is not a hosted multiplayer backend.

## Quick start

1. Download or clone this repository.
2. Open `index.html` in a modern browser, keeping `style.css`, `script.js` and `assets/` alongside it.
3. Alternatively, open `ArenaHub.html` for the portable single-file edition.
4. Create a tournament, set your rules, register squads, approve entries and generate fixtures.

For a stable local origin, run this inside the project folder:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. Keep using the same origin for the same saved records.

### Static hosting

The split-source edition works on ordinary static hosting, including GitHub Pages. Publish the repository root and use `index.html` as the entry point. Hosting does **not** sync tournament data across devices or users; export/import JSON backups to move records.

## The 12 sections

Arena Lobby · Squad Rosters · Team Entry · Player Index · Match Center · Result Review · Dispute Desk · Leaderboard · Bulletins · Rulebook · Event Control · Personalize


## Open the app
Open `ArenaHub.html` for the single-file app, or extract this folder and open `index.html`. Keep the HTML/CSS/JS/assets together for the split-source version. No packages or internet are required.

The initial app has no tournaments, squads, players, matches, submissions, disputes or announcements. Create your own tournament first. Existing records from the previous ArenaHub build are automatically converted if the new app can access the same browser storage. Export/import backups when changing browser profiles or file origins.

## Customize
- Multiple independently managed tournaments with unlimited-count creation subject to device capacity.
- Any game name; suggested games are not mandatory.
- Squad cap: set 0 for no fixed limit or choose a positive limit.
- Roster size: 1–100 players per squad. Existing rosters must be removed before changing their required size.
- Knockout with automatic byes or round-robin league.
- Points scoring or odd-length best-of series (1, 3, 5, 7, ...).
- Configurable league win/draw points and optional draws outside knockout/series matches.
- Optional screenshot requirement, entry deadline, event start date and roster locking.
- Custom event rules and event accent color.
- App name, tagline, two-line lobby headline, theme and four navigation names.

## Valuable features
- Full squad rosters, squad logos/colors, captain contact and notes; organizer approvals/rejections; edit/delete; search/filter.
- Player index with searchable names, IDs and squads.
- Flexible generated fixtures for any approved squad count ≥2. Knockout byes advance automatically; league generates every unique pairing.
- Create any number of additional custom/friendly matches. Choose whether each custom match counts in standings. Custom matches do not change the knockout bracket.
- Match names, stage labels, instructions, date/time, duration and squad check-ins.
- Shared-team schedule conflict checks and knockout round-order checks.
- Score/evidence submission, correction requests, repeat submissions and revision history.
- Multiple dispute tickets per match; priority, reviewer assignment, due date, in-review status, organizer decisions and ticket history.
- All open tickets must resolve before a result can be confirmed.
- Automatic bracket advancement; resetting a result invalidates dependent rounds/evidence/schedules safely.
- Leaderboard with configurable points, wins/draws/losses, score difference and CSV export.
- Bulletins with pinned state, priority and edit/delete.
- Activity log, upcoming matches, progress and champion display.
- Event switcher, quick search, responsive mobile menu, live rulebook and three gaming themes.
- Device-wide JSON backups and import validation; backward-compatible import of the previous ArenaHub backup.

## Device database
IndexedDB `ArenaHubDevice`, object store `workspace`. Settings, all events, images, rosters, scores, history and tickets persist in this browser. Save success is shown only after the database transaction commits. On storage failure, the app restores its last committed in-memory state and reports the failure.

Use the same browser/profile and file origin. Private browsing and separate profiles have separate storage. Clearing browser/site data removes records. Keep JSON backups. HTML embeds may restrict storage; use the downloaded app for persistent use.

There is no arbitrary fixed cap on tournaments, squad entries (when cap=0), custom matches, result revisions, tickets or bulletins. Practical capacity depends on the browser/device. Screenshot uploads are limited to 2 MB; logos to 1 MB. Backup imports are limited to 100 MB per file to protect memory. Very large round-robin events generate n(n−1)/2 fixtures and may be slow; large generations prompt before proceeding.

## Workflow
1. Create tournament; set game, squad size/limit, format/scoring and rules.
2. Register squads and approve them. Players/IDs must be unique within the same event; separate events may reuse them.
3. Close registration and generate fixtures, or add custom matches after approving at least two squads.
4. Schedule, check in and submit results. Organizer reviews or returns submissions for correction.
5. Resolve every active dispute before approving a result.
6. Track the bracket, standings, activity and event bulletins.
7. Export a backup before moving devices or clearing records.

## Rules / implementation notes
- Changing format/series scoring requires clearing that event's matches first. Roster size cannot change while squads exist. Other settings remain adjustable.
- Reopening registration does not automatically erase matches. Roster locks remain configurable. Participating squads cannot be deleted/rejected until fixtures are cleared.
- A knockout champion comes from the final. Leaderboard points are supplementary, not the knockout winner rule.
- Ranking ties: points, wins, score difference, squad name. Byes and unranked friendlies are excluded.
- Schedule conflicts use half-open intervals [start, start+duration) in device local time.
- Match evidence is reviewed manually; uploads are validated as readable PNG/JPG/WebP images.
- Workspace selection is an interface switch for a local single-device application, not account authentication.
- Audit history is local and editable by someone with access to browser developer tools; it is not tamper-proof.

## Source
index.html: layout and app shell.
style.css: neon gaming surfaces, responsive design and themes.
script.js: database/migration, customization, validation, fixtures, submissions, disputes, standings, bulletins and backup logic.
assets/arena-hero.webp: bundled artwork used across lobby and section banners.
ArenaHub.html: portable single-file version.


## Development

No npm install or bundler is required. To regenerate the portable edition after changing the source:

```bash
python3 scripts/build_single_file.py
```

Optional JavaScript syntax check (requires Node.js):

```bash
node --check script.js
```

## Privacy and limitations

- Do not store passwords, access tokens or payment information in app fields.
- Backups may contain player IDs, captain contact details and match evidence; share them carefully.
- Local role selectors do not enforce permissions. Use a real authentication/API backend for a multi-user production service.
- Clearing site data deletes locally saved records. Export backups regularly.
- Changing a file location, hostname, browser profile or hosting URL may select a different browser storage origin.
