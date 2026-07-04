# core/calendar/ — Calendar Sync (ICS feed primary)

Per ADR-002 D4: ICS feed is the primary calendar integration.

Files:
- `ics_writer.py` — generates valid RFC 5545 .ics file from Matter + Deadline + Hearing events
- `publishers.py` — abstracts where to drop the .ics file (local dir · iCloud Drive · Dropbox)

v0.2+ adds:
- EventKit native macOS integration (iCloud sync to iPhone)
- CalDAV alternative for non-Apple users

NEVER adds (intentional per ADR-002 D6):
- Direct Google Calendar API integration (PDPA/LPCR concern — sends client matter data to third party)

User pattern:
1. v0.1 writes ~/.ailawfirm-singapore/calendar.ics
2. User publishes via local HTTP / Dropbox / iCloud Drive (their choice)
3. iPhone Calendar / Google Calendar subscribes by URL
4. Refresh interval: 15min-1hr typical
5. Event SUMMARY = entity-aliasing code only (lock-screen safe). Event BODY = full matter detail.
