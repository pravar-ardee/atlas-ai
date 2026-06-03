from enum import Enum


class StudentIntent(str, Enum):

    DAILY_SUMMARY = "daily_summary"

    ATTENDANCE_SUMMARY = "attendance_summary"

    HOMEWORK_SUMMARY = "homework_summary"

    ASSESSMENT_SUMMARY = "assessment_summary"

    STUDENT_PERFORMANCE = "student_performance"

    STUDENT_REPORT = "student_report"