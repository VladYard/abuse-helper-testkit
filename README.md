# abuse-helper-testkit

SYNTHETIC INERT TEST FIXTURE for the abuse-helper tool.

This is NOT a phishing page. Nothing here collects data, nothing executes.
All indicators (phone number, tunnels, bot token) are FAKE and exist only
to test indicator-extraction regexes.

DO NOT REPORT this repository or its Pages URL to any abuse service.
DO NOT submit it to Safe Browsing, Netcraft, VirusTotal or similar.

Files:
- index.html — inert labeled page (brand keyword for classifier test)
- script.js — inert constants: fake tunnels, fake bot token, t.me placeholder
- server.py — inert sample: fake token, /login test command, regex traps

Related tool: abuse-helper (private repo).
