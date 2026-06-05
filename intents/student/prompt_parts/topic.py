TOPIC_PROMPT = """
--------------------------------------------------

topic_summary

Used when the student asks about:

- topics
- completed topics
- pending topics
- topic progress
- topic completion
- topic overview
- assessment topics
- revision topics
- study topics

Examples:

- What topics have I completed?
- Show completed topics.
- Which topics are pending?
- What topics are left?
- Show topic progress.
- Topic summary.
- Topic overview.
- What topics should I study next?
- What topics are coming in assessments?
- What should I revise before my next test?

==================================================
CLASSIFICATION RULES
==================================================

Questions mentioning:

- topic
- topics
- completed topics
- pending topics
- topic progress
- topic completion
- topic summary
- topic overview
- study topics
- revision topics
- assessment topics

must be classified as:

topic_summary

==================================================
TARGET MODULES
==================================================

topic_summary

[
    "topic"
]
"""