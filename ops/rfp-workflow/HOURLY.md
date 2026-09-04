# Hourly intake loop

This Cursor Cloud conversation runs the **intake** half of the RFP workflow every hour.

ChatGPT and Claude still run on Athif's PC. This loop does not log into those sites and does not submit bids.

## What each hour does

1. Read Gmail for MERX and bidsandtenders mail since the last run.
2. Re-score the live board in `pipeline.csv` / Drive sheet `01 — Pipeline tracker`.
3. Write `05 — Latest hourly intake` in Drive folder `1OlzaMxK54cpJyfcwu8r86wBAUKfZGm5V`.
4. Compare against Drive file `06 — last-run.json`. Email athif@thealphanova.com only on a real delta (see below). Quiet hours: Drive log only.
5. Never submit. Never email a buyer. Do not re-alert the same deadline every hour.

## Email rules

Send mail only if:

- new GO / MAYBE, or a watch item promoted
- new MERX or bidsandtenders vendor mail (timestamp newer than `last_vendor_mail`)
- a deadline that just entered the 24-hour window and is **not** already in `alerted_deadlines`
- first run of a new calendar day in America/Toronto (once per `last_email_et_date`)

Template: `ops/rfp-workflow/last-run.example.json`. Live copy is Drive `06 — last-run.json`. Do not commit a new git snapshot every hour.

## Timer

Name: `rfp-hourly-intake`

Recurring every 3600 seconds on this Cloud Agent conversation. Expires 2026-09-11 unless renewed. Re-subscribe if `list_subscriptions` shows it missing.

Wake prompt: `ops/rfp-workflow/prompts/hourly-wake.md`.

To stop: tell this agent to unsubscribe `rfp-hourly-intake`.
