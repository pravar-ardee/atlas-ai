PERFORMANCE_PROMPT = """
--------------------------------------------------

student_performance

Used when the student asks for:

- overall performance
- academic performance
- strengths
- weaknesses
- improvement advice
- academic risk
- readiness
- recommendations
- performance decline
- focus areas

Examples:

- How am I doing overall?
- Why is my performance declining?
- What should I focus on next?
- What are my strengths?
- What are my weaknesses?
- What concerns do you see?
- Am I at risk academically?
- How prepared am I?
- Review my academic performance.
- Give me a performance overview.
- What is preventing me from improving?
- How can I improve my Atlas score?

==================================================
CLASSIFICATION RULES
==================================================

Questions that require combining
multiple student systems such as:

- attendance
- homework
- assessments
- subjects
- atlas

must be classified as:

student_performance

==================================================
TARGET MODULES
==================================================

student_performance

[
    "student_performance"
]
"""