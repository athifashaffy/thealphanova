#!/bin/sh
# The Alpha Nova uptime monitor.
#
# Runs every 15 minutes from cron. Two jobs:
#   1. Alert the moment a site starts failing, and again when it recovers.
#      Only state CHANGES send mail, so a long outage is one email, not 96.
#   2. Send a status summary once a day at 09:00.
#
# Deliberately checks HTTP status only, not page content. The host puts a
# JavaScript challenge in front of the site under load, which returns 200
# with a "One moment, please..." body. Matching on body text would fire
# false DOWN alerts every time that kicks in. A real outage shows up as a
# 5xx or a connection failure, which is exactly what took the site down in
# August, and that is what this catches.
#
# Every run appends one line to site-monitor.log, including whether the mail
# actually handed off successfully. Without that there is no way to tell a
# working monitor from a silent one.

# Recipient lives in .env, not here: this script is tracked in a PUBLIC
# repository and a personal address in git is a gift to scrapers.
ENV_FILE="/home/thealpha/public_html/.env"
TO=$(sed -n 's/^MONITOR_EMAIL=//p' "$ENV_FILE" 2>/dev/null | head -1 | tr -d '[:space:]')
[ -z "$TO" ] && TO="info@thealphanova.com"
FROM="The Alpha Nova Monitor <info@thealphanova.com>"
STATE="/home/thealpha/.site-monitor.state"
LOG="/home/thealpha/site-monitor.log"
UA="Mozilla/5.0 (compatible; AlphaNovaMonitor/1.0)"

TARGETS="https://thealphanova.com/ https://thealphanova.com/services https://labs.thealphanova.com/"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*" >> "$LOG"; }

# Hand off to whichever mailer this account actually has.
send_mail() {
    _subject="$1"
    _body="$2"
    _msg="To: $TO
From: $FROM
Subject: $_subject
Content-Type: text/plain; charset=UTF-8

$_body

--
Checked $(date '+%Y-%m-%d %H:%M:%S %Z') on the cPanel server.
Script: /home/thealpha/site-monitor.sh   Log: /home/thealpha/site-monitor.log"

    if [ -x /usr/sbin/sendmail ]; then
        echo "$_msg" | /usr/sbin/sendmail -t
        log "mail via /usr/sbin/sendmail rc=$? subject=\"$_subject\""
    elif command -v sendmail >/dev/null 2>&1; then
        echo "$_msg" | sendmail -t
        log "mail via sendmail(PATH) rc=$? subject=\"$_subject\""
    elif command -v mail >/dev/null 2>&1; then
        echo "$_body" | mail -s "$_subject" "$TO"
        log "mail via mail(1) rc=$? subject=\"$_subject\""
    else
        log "MAIL FAILED: no sendmail or mail binary found"
        return 1
    fi
    return 0
}

REPORT=""
FAILING=""
SUMMARY=""
for url in $TARGETS; do
    code=$(curl -s -o /dev/null -m 25 -w '%{http_code}' -A "$UA" "$url" 2>/dev/null)
    [ -z "$code" ] && code="000"
    case "$code" in
        2*|3*) status="UP  " ;;
        *)     status="DOWN"; FAILING="$FAILING $url($code)" ;;
    esac
    REPORT="$REPORT
  $status  $code  $url"
    SUMMARY="$SUMMARY $code"
done

if [ -n "$FAILING" ]; then NOW="down"; else NOW="up"; fi

PREV="unknown"
[ -f "$STATE" ] && PREV=$(cat "$STATE")
echo "$NOW" > "$STATE"

log "check state=$NOW prev=$PREV codes:$SUMMARY"

# 1. State change -> alert immediately
if [ "$NOW" != "$PREV" ] && [ "$PREV" != "unknown" ]; then
    if [ "$NOW" = "down" ]; then
        send_mail "[DOWN] thealphanova.com is not responding" \
"One or more Alpha Nova URLs started failing.

Failing:$FAILING
$REPORT"
    else
        send_mail "[RECOVERED] thealphanova.com is back up" \
"All monitored URLs are responding again.
$REPORT"
    fi
    # keep the log from growing without bound
    tail -n 500 "$LOG" > "$LOG.tmp" 2>/dev/null && mv "$LOG.tmp" "$LOG"
    exit 0
fi

# 2. Daily summary, timed for the morning in Ontario.
# The server clock is IST (+0530), 9.5h ahead of Eastern, so 18:30 here is
# 09:00 EDT. It drifts to 08:00 for you when Eastern goes back to EST in
# November; change DAILY_AT to 19:30 then if that matters.
DAILY_AT="18:30"
if [ "$(date '+%H:%M')" = "$DAILY_AT" ]; then
    if [ "$NOW" = "up" ]; then
        send_mail "Alpha Nova daily status: all up" "All monitored URLs responding.
$REPORT"
    else
        send_mail "[DOWN] Alpha Nova daily status: problems detected" \
"Still failing:$FAILING
$REPORT"
    fi
fi

tail -n 500 "$LOG" > "$LOG.tmp" 2>/dev/null && mv "$LOG.tmp" "$LOG"
