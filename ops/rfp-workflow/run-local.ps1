# Run on your Windows PC. Opens ChatGPT, Claude, MERX, Drive, and the local prompt page.
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Start-Process (Join-Path $here "open-on-pc.html")
Start-Process "https://chatgpt.com"
Start-Process "https://claude.ai"
Start-Process "https://www.merx.com"
Start-Process "https://drive.google.com/drive/folders/1OlzaMxK54cpJyfcwu8r86wBAUKfZGm5V"
Write-Host "ChatGPT writes. Claude edits. You submit. Nothing uploads to a portal from this script."
