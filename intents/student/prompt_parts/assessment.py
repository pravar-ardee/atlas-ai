ASSESSMENT_PROMPT = """
--------------------------------------------------

assessment_summary

Used when the student asks about assessments,
tests, quizzes, exams, grades, marks,
results, performance, feedback,
teacher comments or upcoming assessments.

Examples:

- Show latest assessment
- What was my score?
- Recent tests
- Assessment results
- Upcoming assessments
- Any tests this week?
- What exams are coming up?
- What assessments are scheduled for me?
- Which assessment is next?
- Do I have any pending assessments?
- Which assessment needs attention?

Results & Marks:

- What marks did I get?
- Show my grades
- What was my latest result?
- What was my latest assessment result?
- Show my latest test result
- How many marks did I score?
- What grade did I get?
- What was my best assessment?
- What was my weakest assessment?
- Which assessment did I score highest in?
- Which assessment did I score lowest in?

Performance:

- How am I performing in assessments?
- What is my average assessment score?
- Am I improving in assessments?
- Show assessment performance
- How many assessments have been graded?
- Summarize my assessment performance
- How am I doing in tests?

Feedback:

- Show assessment feedback
- Did my teacher leave feedback?
- Any teacher comments on my assessments?
- What feedback did I receive?
- Show recent assessment reviews
- Show teacher comments on my tests
- What did my teacher say about my assessment?

Missed / Pending:

- Which assessment did I miss?
- What assessments are pending?
- What assessments have I not completed?
- Which tests require action?
- Which assessments are overdue?

==================================================
ASSESSMENT INTERPRETATION RULES
==================================================

Questions about:

- test
- tests
- quiz
- quizzes
- exam
- exams
- assessment
- assessments
- marks
- grades
- score
- scores
- result
- results
- assessment performance
- assessment feedback
- teacher comments
- teacher feedback on tests
- teacher feedback on assessments
- graded assessments
- latest result
- latest assessment
- average score
- best assessment
- weakest assessment
- highest score
- lowest score
- upcoming assessment
- upcoming test
- upcoming exam
- pending assessment

must be classified as:

assessment_summary

unless the student is explicitly asking about:

- homework
- attendance
- atlas score
- daily summary
- student report

==================================================
DISAMBIGUATION RULES
==================================================

Questions like:

"What marks did I get?"
"What score did I get?"
"What grade did I get?"

should default to:

assessment_summary

unless the query explicitly mentions:

- homework
- assignment

Examples:

"What marks did I get?"
→ assessment_summary

"What marks did I get in homework?"
→ homework_summary

"What score did I get?"
→ assessment_summary

"What homework score did I get?"
→ homework_summary

==================================================
TARGET MODULES
==================================================

assessment_summary

[
    "assessment"
]
"""