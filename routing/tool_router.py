from intents.student.enums import (
    StudentIntent
)


def get_tools_for_intent(
    intent
):

    # =====================================
    # DAILY SUMMARY
    # =====================================

    if (
        intent
        ==
        StudentIntent.DAILY_SUMMARY
    ):

        return [

            "attendance_tool",

            "homework_tool",

            "assessment_tool",

            "announcement_tool",

            "atlas_tool"
        ]

    # =====================================
    # ATTENDANCE
    # =====================================

    if (
        intent
        ==
        StudentIntent.ATTENDANCE_SUMMARY
    ):

        return [
            "attendance_tool"
        ]

    # =====================================
    # HOMEWORK
    # =====================================

    if (
        intent
        ==
        StudentIntent.HOMEWORK_SUMMARY
    ):

        return [
            "homework_tool"
        ]

    # =====================================
    # ASSESSMENTS
    # =====================================

    if (
        intent
        ==
        StudentIntent.ASSESSMENT_SUMMARY
    ):

        return [
            "assessment_tool"
        ]

    # =====================================
    # ATLAS SCORE
    # =====================================

    if (
        intent
        ==
        StudentIntent.ATLAS_SCORE_SUMMARY
    ):

        return [
            "atlas_tool"
        ]

    # =====================================
    # PERFORMANCE
    # =====================================

    if (
        intent
        ==
        StudentIntent.STUDENT_PERFORMANCE
    ):

        return [
            "student_performance_tool"
        ]

    # =====================================
    # REPORT
    # =====================================

    if (
        intent
        ==
        StudentIntent.STUDENT_REPORT
    ):

        return [

            "atlas_tool",

            "attendance_tool",

            "homework_tool",

            "assessment_tool"
        ]
    
    if (
        intent
        ==
        StudentIntent.ANNOUNCEMENT_SUMMARY
    ):

        return [
            "announcement_tool"
        ]
    
    if (
        intent
        ==
        StudentIntent.FORUM_SUMMARY
    ):

        return [
            "forum_tool"
        ]
    
    if (
        intent
        ==
        StudentIntent.SUBJECT_SUMMARY
    ):

        return [
            "subject_tool"
        ]

    if (
        intent
        ==
        StudentIntent.TOPIC_SUMMARY
    ):

        return [
            "topic_tool"
        ]
    
    return []

