SUBJECT_PROMPT = """
--------------------------------------------------

subject_summary

Used when the student asks about:

- subjects
- strongest subject
- weakest subject
- best subject
- worst subject
- subject performance
- subject comparison
- subject grades
- subject scores
- subject strengths
- subject weaknesses
- subject improvement
- subject analysis
- subject insights

==================================================
EXAMPLES
==================================================

Direct Subject Questions:

- What is my strongest subject?
- What is my weakest subject?
- Best subject
- Worst subject
- Highest scoring subject
- Lowest scoring subject
- Which subject needs attention?
- What subject should I focus on?
- Which subject is affecting my grades?

Performance Questions:

- Show subject performance
- Subject performance
- My subject performance
- View subject performance
- Display subject performance
- Analyze my subject performance
- Review my subject performance
- How am I doing across subjects?
- How strong are my subjects?
- How am I performing in my subjects?
- Compare my subjects
- Compare subject scores
- Subject summary
- Subject overview

Improvement Questions:

- What should I improve in subjects?
- How can I improve my weakest subject?
- How can I improve my subject performance?
- What subject should I focus on next?
- What are my subject weaknesses?
- What are my subject strengths?

Reasoning Questions:

- Why is my weakest subject weak?
- Why is Maths weak?
- Why am I struggling in Maths?
- Explain my weakest subject.
- Explain my subject performance.
- What insights do you have about my subjects?
- Analyze my subject results.

==================================================
CLASSIFICATION RULES
==================================================

Questions mentioning:

- subject
- subjects
- strongest subject
- weakest subject
- best subject
- worst subject
- highest scoring subject
- lowest scoring subject
- subject performance
- show subject performance
- my subject performance
- analyze my subject performance
- review my subject performance
- compare my subjects
- subject comparison
- subject analysis
- subject insights
- subject strengths
- subject weaknesses
- subject improvement
- improve my weakest subject
- improve my subjects
- how am i doing across subjects
- how am i performing in subjects
- why is my weakest subject weak
- why is maths weak
- explain my weakest subject
- explain my subject performance
- what subject should i focus on
- which subject needs attention
- strongest subject
- weakest subject

must be classified as:

subject_summary

==================================================
DISAMBIGUATION RULES
==================================================

If a query contains:

- subject
- subjects

and does not explicitly mention:

- homework
- attendance
- atlas score
- announcements
- forums

then classify as:

subject_summary

Examples:

"Show subject performance"
→ subject_summary

"Analyze my subject performance"
→ subject_summary

"How am I doing across subjects?"
→ subject_summary

"What subject should I focus on?"
→ subject_summary

"Why is my weakest subject weak?"
→ subject_summary

==================================================
TARGET MODULES
==================================================

subject_summary

[
    "subject"
]
"""