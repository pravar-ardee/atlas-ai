DATE_RULES = """
==================================================
DATE RULES
==================================================

You MUST resolve all dates.

Convert all dates into ISO format.

today
→ start_date=today
→ end_date=today

yesterday
→ previous date

16th May
→ YYYY-MM-DD

Monday
→ actual Monday date

this week
→ Monday of current week to today

last week
→ Monday to Sunday of previous week

this month
→ first day of current month to today

last month
→ first day to last day of previous month

If only a day is specified:

16th
5th
23rd

Assume current month and current year.

If no date is mentioned:

start_date = null
end_date = null
"""