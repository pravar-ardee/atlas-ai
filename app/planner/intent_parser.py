async def parse_intent(
    query: str
):

    query = query.lower()

    if "attendance" in query:

        return {
            "intent": "attendance_summary"
        }

    if "homework" in query:

        return {
            "intent": "homework_summary"
        }

    if "performance" in query:

        return {
            "intent": "student_performance"
        }

    return {
        "intent": "general_summary"
    }