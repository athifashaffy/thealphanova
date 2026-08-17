# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this is

The Alpha Nova marketing site. Hand-written static HTML, one shared stylesheet,
one shared JS file, one PHP endpoint. **No build step, no framework, no package
manager.** You edit HTML and upload it.

`labs/index.html` is a separate page served at `labs.thealphanova.com`. It keeps
its own visual identity and defence-tech positioning; only its nav, footer and
shared plumbing are aligned with the main site.

## Deployment

The site is on cPanel at LankaHost. **Git is not the deploy mechanism** — pushing
to GitHub changes nothing on the live site. Files reach production by upload
through the cPanel API, using the `cpanel-deploy` skill:

```bash
C=~/.claude/skills/cpanel-deploy/cpanel.sh
export CPANEL_ENV=~/.cpanel-thealphanova.env
$C put index.html /public_html index.html
$C put css/style.css /public_html/css style.css
$C put labs/index.html /public_html/labs index.html
```

### The rule that matters most

**Assume the live server is ahead of git.** People edit files through the cPanel
File Manager and those changes are never committed. Uploading straight from the
repo silently destroys that work.

This has already happened here. The live site had been repositioned from
"global / tri-continental" to Canadian, had a hero scroll cue, real photography,
a new Cambrian testimonial and a `/signa` nav link — none of it in git. The repo
was behind on **every page**: 131 lines on `about.html`, 12–48 per case study,
117 in the stylesheet, 26 in `main.js`.

So before any significant deploy:

```bash
curl -sL "https://thealphanova.com/about" -o /tmp/live.html
diff /tmp/live.html about.html      # reconcile BEFORE editing
```

If the server is ahead, pull its version into the repo first, commit that as its
own baseline, then apply your changes on top.

### Verifying a deploy

Compare the live page to the local file. Two traps:

- **Request the clean URL, not the `.html` one.** `.htaccess` 301-redirects
  `/about.html` to `/about`, so hashing the `.html` URL compares redirect bodies,
  not pages. Use `curl -sL`.
- **Don't hash via `$(...)`.** Command substitution strips the trailing newline,
  so a correct file reports as DIFFER. Write to a file and `diff` instead.

```bash
curl -sL "https://thealphanova.com/" -o /tmp/live.html
diff -q index.html /tmp/live.html && echo MATCH
```

### The host's bot challenge

Under load, an openresty layer serves a JavaScript challenge: HTTP **200** with
`<title>One moment, please...</title>` and a spinner, for *every* path including
ones that should 404. Rapid `curl` loops trigger it. It affects port 2083 (the
cPanel API) too, and clears on its own after a few minutes.

It is not an outage and not your `.htaccess`. Real browsers pass it instantly.
If you need to verify while it is active, use headless Chrome, which runs the JS:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --disable-gpu --virtual-time-budget=25000 --dump-dom "https://thealphanova.com/"
```

Pace your requests. Add `sleep 2` between checks rather than firing hundreds.

## Secrets

**This repository is public on GitHub.** A reCAPTCHA secret was once hardcoded in
`sendemail.php` and had to be rotated because of it.

Secrets live in `.env` in the document root: gitignored, `chmod 600`, uploaded
separately from any deploy. `.env.sample` is the committed template.
`sendemail.php` parses `.env` at request time and **fails closed** — an empty or
unreadable secret redirects to `?status=config` rather than quietly accepting
unverified submissions.

`.htaccess` refuses to serve dotfiles and backup files. Do not remove that block:

```apache
<FilesMatch "(^\.|\.(env|bak|backup|old|orig|save|swp|sample|dist|log|sql|ini)([.\-~].*)?$)">
```

Note the trailing `.*` on the suffixes. A bare `\.bak$` does **not** match
`sendemail.php.bak-20260814`, and a backup like that is served as plain text
rather than executed, publishing whatever secret the original contained. If you
create server-side backups in the docroot, delete them when you are done.

## Conventions, each learned from a real bug

**Never put `grid-template-columns` in an inline `style`.** Inline styles outrank
every stylesheet rule, so the `@media (max-width: 900px)` collapse to one column
never applies and cards stay multi-up and crushed on phones. Use a modifier class
(`.cap-grid-2`) instead. This was introduced, fixed, and then reintroduced once.

**Counters must contain the real number in the HTML.** `main.js` animates
`[data-count]` on scroll, but the markup itself has to read `50+`, not `0+`.
Otherwise crawlers, screen readers and no-JS visitors see zeros. Check both
`index.html` and `about.html`.

**Put a space before `<br>` in headings.** `Who<br>Get Stuff Done` extracts as
`WhoGet Stuff Done`.

**Never leave an element empty for JS to fill.** The old hero used an empty
`.typed-text` span, so crawlers read `Build the  with Intelligent Software`.

**No em dashes.** House style. Use commas or full stops. They hide in JSON-LD
blocks and `content=` meta attributes as `&mdash;`, so check there too.

**Bump the stylesheet cache-bust whenever CSS changes rendering.** Pages link
`css/style.css?v=YYYYMMDD`. Without a bump, returning visitors keep the cached
file and see none of your work. `labs/index.html` uses an absolute URL and was
once missed entirely. Deleting unused rules does not need a bump.

**Every internal link must resolve.** The footer once pointed six service links
at `#`.

## Regenerating pages

The service, industries, products, booking and Sudbury pages are generated by
`ops/gen_pages*.py`, so nav, footer, schema and CTA blocks stay identical across
them. Output is committed as plain HTML and hand-editable; the generators exist
to make sweeping changes consistent.

```bash
cd ops && python3 gen_pages.py && python3 gen_pages2.py && python3 gen_pages3.py
```

If you change nav or footer, change it in `gen_pages.py` **and** in the
hand-written pages (`index.html`, `about.html`, `case-*.html`, `labs/index.html`),
or they drift apart.

## Positioning

The Alpha Nova is a **technology company that builds intelligent software and
industrial systems**, not a software development agency. Brand line:
**AI. Software. IoT. One Technology Partner.**

- **Canadian.** Headquartered in Greater Sudbury. Do not reintroduce claims about
  offices in Passau or Colombo, or "three continents" / "global partner".
  Clients abroad (UKE Hamburg, comAlpine) are fine to name as clients.
- Four capabilities, not six services: AI & Intelligent Systems, Industrial IoT
  & Edge, Software Engineering, Product Engineering.
- Homepage flow: hero → brand strip → credibility → logos → capabilities →
  industrial → We Design/Build/Integrate → proof → testimonials → products →
  Labs → FAQ → CTA.
- Lines shared with the brand video: "Build What's Next.", "Power Autonomous
  Workflows.", "Drive Intelligent Action.", "Whatever you're building next."
- **AN Labs** is advanced R&D (autonomy, edge AI, computer vision, dual-use).
  Keep it distinct so a hospital or college does not read the company as
  defence-and-mining only.

Booking is the primary conversion path. `[data-calendly]` elements open the
Calendly popup; `CALENDLY_URL` at the top of `js/main.js` is the single source of
truth. Every such element also has a working `/book` href, so it degrades
properly without JS.

## Uptime monitor

`ops/site-monitor.sh` runs from cron every 15 minutes on the server
(`*/15 * * * *`, calling `/home/thealpha/site-monitor.sh`).

- Emails only on **state change**, so a long outage is two emails rather than
  ninety-six, plus a daily summary.
- Checks **HTTP status only**. Matching page content would fire false DOWN alerts
  every time the bot challenge above kicks in.
- **The server clock is IST**, 9.5 hours ahead of Eastern. `DAILY_AT="18:30"` is
  09:00 in Ontario. It drifts an hour when Eastern changes.
- Recipient comes from `MONITOR_EMAIL` in `.env`, never hardcoded, because this
  repo is public.
- Logs each run to `/home/thealpha/site-monitor.log` with the mailer used and its
  exit code, so a silently broken monitor is detectable.

## Gotchas specific to this site

- `/public_html/labs/index.html` is the live Labs page. A stale `labs.html` used
  to sit in the repo root, shadowed by the `/labs/` directory and served to
  nobody. It has been deleted; do not recreate it.
- The Labs form posts to the **main site's** `sendemail.php`. If you rotate the
  reCAPTCHA keys, update the site key in `labs/index.html` too, or every Labs
  enquiry silently fails verification.
- Pages carrying the reCAPTCHA site key: `index.html`, `book.html`,
  `labs/index.html`.
- `sendemail.php` accepts `budget` and `timeline` from the qualification form.
  Adding a form field without adding it there means the answer is dropped.

## Open decisions

- **Dr. Markus Lehmann** appears as Strategic Advisor on the About page, as a
  comAlpine client testimonial on the homepage, `/services` and
  `/custom-software-development`, and as the face of the "Let's talk about your
  product" CTA on ten pages. The advisory relationship is not disclosed
  alongside the testimonial, so it reads as independent when it is not.
- **Industries Served** read 10+ on the homepage and 7+ on About. Both now say
  7+, the more conservative figure. Confirm which is true.
- **98% Client Satisfaction** is asserted in crawlable HTML. Make sure it can be
  backed up.
- The **technology chips** on service pages are inferred, not confirmed. Correct
  them to the real stack.
- The **VanGuardian** product description was written from the case study rather
  than supplied.
