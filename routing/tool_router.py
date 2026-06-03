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
) -> list[str]:

    return INTENT_TO_TOOLS.get(
        intent,
        []
    )