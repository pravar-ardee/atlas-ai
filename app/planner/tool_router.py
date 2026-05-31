def get_tools_for_intent(
    intent: str
):

    mapping = {

        "attendance_summary": [
            "attendance_tool"
        ],

        "homework_summary": [
            "homework_tool"
        ],

        "student_performance": [
            "assessment_tool",
            "attendance_tool"
        ],

        "general_summary": [
            "attendance_tool",
            "homework_tool"
        ]
    }

    return mapping.get(intent, [])