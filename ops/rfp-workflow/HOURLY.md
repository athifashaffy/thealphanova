# Hourly intake loop

This Cursor Cloud conversation runs the **intake** half of the RFP workflow every hour.

ChatGPT and Claude still run on Athif's PC. This loop does not log into those sites and does not submit bids.

## What each hour does

1. Read Gmail for MERX and bidsandtenders mail since the last run.
2. Re-score the live board in `pipeline.csv` / Drive sheet `01 — Pipeline tracker`.
3. Write `05 — Latest hourly intake` in Drive folder `1OlzaMxK54cpJyfcwu8r86wBAUKfZGm5V`.
4. Email athif@thealphanova.com **only on state change** (new GO/MAYBE, new vendor mail, deadline inside 24 hours, or the first run of a new day). Quiet hours otherwise.
5. Never submit. Never email a buyer.

## Timer

Name: `rfp-hourly-intake`

Recurring every 3600 seconds on this Cloud Agent conversation. Re-subscribe if `list_subscriptions` shows it expired.

To stop: tell this agent to unsubscribe `rfp-hourly-intake`.
