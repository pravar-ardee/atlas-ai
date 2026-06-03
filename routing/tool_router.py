from intents.student.enums import (
    StudentIntent
)


INTENT_TO_TOOLS = {

    StudentIntent.DAILY_SUMMARY: [
        "attendance_tool",
        "homework_tool",
        "assessment_tool"
    ],

    StudentIntent.ATTENDANCE_SUMMARY: [
        "attendance_tool"
    ],

    StudentIntent.HOMEWORK_SUMMARY: [
        "homework_tool"
    ],

    StudentIntent.ASSESSMENT_SUMMARY: [
        "assessment_tool"
    ],

    StudentIntent.STUDENT_PERFORMANCE: [
        "attendance_tool",
        "homework_tool",
        "assessment_tool"
    ],

    StudentIntent.STUDENT_REPORT: [
        "attendance_tool",
        "homework_tool",
        "assessment_tool"
    ]
}


def get_tools_for_intent(
    intent
):
    if intent == StudentIntent.STUDENT_PERFORMANCE:

        return [
            "atlas_tool"
        ]

    if intent == StudentIntent.DAILY_SUMMARY:

        return [
            "attendance_tool"
        ]

    if intent == StudentIntent.ATTENDANCE_SUMMARY:

        return [
            "attendance_tool"
        ]

    if intent == StudentIntent.ATLAS_SCORE_SUMMARY:

        return [
            "atlas_tool"
        ]

    return []