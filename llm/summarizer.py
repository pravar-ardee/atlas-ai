import json
import logging

from intents.student.enums import (
    StudentIntent
)

from llm.client import (
    chat_completion
)

logger = logging.getLogger(__name__)


def build_prompt(
    query: str,
    data: dict,
    intent
):

    common = f"""
USER QUERY:

{query}

DATA:

{json.dumps(data, indent=2, default=str)}

==================================================
RULES
==================================================

Use ONLY the provided data.

Never invent information.

Never assume information.

Speak directly to the student.

Use actual metrics from the data.

If sufficient information is not available,
say so.

Do not mention:

- APIs
- databases
- repositories
- backend systems
- technical implementation details

Maximum 150 words.

Be concise.
"""

    # =====================================
    # ASSESSMENT
    # =====================================

    if intent == StudentIntent.ASSESSMENT_SUMMARY:

        return f"""
You are Atlas AI.

You are analyzing assessment data only.

Use ONLY assessment information.

Never mention:

- Atlas Score
- Academic Pillar
- Growth Pillar
- Initiative Pillar
- Attendance
- Homework

unless explicitly present in assessment data.

Focus on:

- performance
- highest_assessment
- lowest_assessment
- recent_feedback
- insights
- recommended_focus

Provide:

1. Assessment performance
2. Strengths
3. Areas needing improvement
4. Recommended focus

{common}
"""

    # =====================================
    # ATLAS SCORE
    # =====================================

    if intent == StudentIntent.ATLAS_SCORE_SUMMARY:

        return f"""
You are Atlas AI.

You are analyzing Atlas Intelligence only.

Use ONLY Atlas information.

Never reference:

- assessments
- homework
- attendance

unless explicitly provided.

Use:

- atlas_score
- strongest_actionable_pillar
- weakest_actionable_pillar
- insights
- recommended_focus

Do not calculate pillars.

Use values already provided.

{common}
"""

    # =====================================
    # HOMEWORK
    # =====================================

    if intent == StudentIntent.HOMEWORK_SUMMARY:

        return f"""
You are Atlas AI.

You are analyzing homework data only.

Never discuss:

- Atlas Score
- Attendance
- Assessments

Focus on:

- pending homework
- overdue homework
- due today
- due tomorrow
- teacher feedback

Keep recommendations specific.

{common}
"""

    # =====================================
    # ATTENDANCE
    # =====================================

    if intent == StudentIntent.ATTENDANCE_SUMMARY:

        return f"""
You are Atlas AI.

You are analyzing attendance only.

Never discuss:

- Atlas Score
- Assessments
- Homework

Use only attendance metrics provided.

Explain attendance performance
using actual values.

{common}
"""

    # =====================================
    # PERFORMANCE
    # =====================================

    if intent == StudentIntent.STUDENT_PERFORMANCE:

        return f"""
You are Atlas AI.

Provide an overall student performance analysis.

You may use:

- Atlas Intelligence
- Homework
- Assessments
- Attendance

Use only supplied data.

Do not invent metrics.

Identify:

1. Strengths
2. Weak areas
3. Recommended focus

Use insights if available.

{common}
"""

    # =====================================
    # DAILY SUMMARY
    # =====================================

    if intent == StudentIntent.DAILY_SUMMARY:

        return f"""
You are Atlas AI.

Provide a concise daily summary.

Include:

- attendance
- homework
- assessments
- atlas insights

Use only supplied data.

Highlight any actions needed.

{common}
"""

    # =====================================
    # STUDENT REPORT
    # =====================================

    if intent == StudentIntent.STUDENT_REPORT:

        return f"""
You are Atlas AI.

Provide a complete student report.

Use all available information.

Summarize:

- attendance
- homework
- assessments
- atlas performance

Provide:

1. Strengths
2. Areas of concern
3. Recommended next steps

{common}
"""

    return common


async def summarize_response(
    query: str,
    data: dict,
    context,
    intent
):

    prompt = build_prompt(
        query=query,
        data=data,
        intent=intent
    )

    response = await chat_completion(
        [
            {
                "role": "system",
                "content": (
                    "You are Atlas AI, a student "
                    "performance analytics assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    logger.info(
        "Summarizer response: %s",
        response
    )

    return response["message"]["content"]