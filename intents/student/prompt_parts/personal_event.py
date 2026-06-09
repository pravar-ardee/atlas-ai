PERSONAL_EVENT_PROMPT = """
--------------------------------------------------

personal_event_summary

Used when the student asks about:

- calendar
- schedule
- events
- reminders
- upcoming events
- personal events

Examples:

- What events do I have today?
- Show my calendar.
- What is scheduled tomorrow?
- Any reminders this week?
- Show my upcoming events.

==================================================

personal_event_create

Used when the student wants to create:

- reminder
- study session
- personal event
- exam reminder
- activity

Examples:

- Remind me to study maths tomorrow.
- Create a revision session for Friday.
- Add a football practice event.
- Set a reminder for my chemistry exam.

IMPORTANT:

Never create immediately.

Always classify as:

personal_event_create

Event creation requires confirmation.
"""