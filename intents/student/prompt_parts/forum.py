FORUM_PROMPT = """
--------------------------------------------------

forum_summary

Used when the student asks about:

- forums
- clubs
- communities
- activities
- memberships
- joined forums
- joined clubs
- forum announcements
- forum updates
- forum notices
- club announcements
- club updates
- community announcements
- community updates

Examples:

- My forums
- Which forums am I in?
- Which forums am I belong to?
- Show my forums
- Show my joined forums
- Show my memberships

- What clubs am I part of?
- Show my clubs
- My clubs
- Joined clubs
- Club memberships

- Forum announcements
- Forum updates
- Forum notices
- Forum announcement
- Latest forum announcement
- Recent forum announcements

- Club announcements
- Club updates
- Any club updates?
- Recent club notices

- Community announcements
- Community updates

==================================================
CRITICAL CLASSIFICATION RULES
==================================================

If the query contains ANY of:

- forum announcement
- forum announcements
- latest forum announcement
- recent forum announcements
- forum update
- forum updates
- forum notice
- forum notices
- club announcement
- club announcements
- club update
- club updates
- community announcement
- community announcements

You MUST classify as:

forum_summary

NEVER classify these as:

announcement_summary

School announcements and forum announcements
are separate concepts.

Examples:

"Forum announcements"
→ forum_summary

"Latest forum announcement"
→ forum_summary

"Forum notices"
→ forum_summary

"Recent forum announcements"
→ forum_summary

"Club updates"
→ forum_summary

"Community announcements"
→ forum_summary

Only school-wide announcements,
class announcements,
campus notices,
or general notices should become:

announcement_summary

==================================================
TARGET MODULES
==================================================

forum_summary

[
    "forum"
]
"""