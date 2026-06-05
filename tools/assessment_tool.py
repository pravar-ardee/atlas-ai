from db.session import (
    AsyncSessionLocal
)

from db.repositories.assessment_repository import (
    AssessmentRepository
)


class AssessmentTool:

    async def run(
        self,
        context,
        parsed_intent
    ):

        if not context.enrollment_id:

            return {
                "error":
                "Enrollment ID missing"
            }

        query = (
            getattr(
                parsed_intent,
                "original_query",
                ""
            )
            .lower()
            .strip()
        )

        async with AsyncSessionLocal() as db:

            repo = AssessmentRepository(
                db
            )

            upcoming = (
                await repo.get_upcoming_assessments(
                    context.enrollment_id
                )
            )

            pending = (
                await repo.get_pending_assessments(
                    context.enrollment_id
                )
            )

            latest_result = (
                await repo.get_latest_result(
                    context.enrollment_id
                )
            )

            performance = (
                await repo.get_performance_summary(
                    context.enrollment_id
                )
            )

            highest_assessment = (
                await repo.get_highest_scoring_assessment(
                    context.enrollment_id
                )
            )

            lowest_assessment = (
                await repo.get_lowest_scoring_assessment(
                    context.enrollment_id
                )
            )

            recent_feedback = (
                await repo.get_recent_feedback(
                    context.enrollment_id
                )
            )

            insights = []

            recommended_focus = []

            if len(pending) > 0:

                insights.append(
                    "There are pending assessments."
                )

            if (
                performance.get(
                    "average_percentage",
                    0
                ) < 60
            ):

                insights.append(
                    "Assessment average is below target."
                )

            if (
                performance.get(
                    "lowest_percentage",
                    0
                ) < 40
            ):

                insights.append(
                    "One assessment score is below 40%."
                )

            if lowest_assessment:

                recommended_focus.append(
                    lowest_assessment[
                        "title"
                    ]
                )

            performance_summary = {

                "average_percentage":
                    performance.get(
                        "average_percentage",
                        0
                    ),

                "best_assessment":
                    (
                        highest_assessment[
                            "title"
                        ]
                        if highest_assessment
                        else None
                    ),

                "weakest_assessment":
                    (
                        lowest_assessment[
                            "title"
                        ]
                        if lowest_assessment
                        else None
                    ),

                "pending_count":
                    len(pending),

                "focus":
                    recommended_focus,

                "insights":
                    insights
            }

            payload = {

                "module":
                    "assessment",

                "upcoming_count":
                    len(upcoming),

                "pending_count":
                    len(pending),

                "upcoming":
                    upcoming,

                "pending":
                    pending,

                "latest_result":
                    latest_result,

                "highest_assessment":
                    highest_assessment,

                "lowest_assessment":
                    lowest_assessment,

                "recent_feedback":
                    recent_feedback,

                "performance":
                    performance,

                "insights":
                    insights,

                "recommended_focus":
                    recommended_focus,

                "performance_summary":
                    performance_summary
            }

            # =====================================
            # UPCOMING ASSESSMENTS
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "upcoming",
                    "coming up",
                    "scheduled",
                    "next assessment",
                    "next test",
                    "next exam",
                    "this week"
                ]
            ):

                if upcoming:

                    first = upcoming[0]

                    payload[
                        "direct_answer"
                    ] = (
                        f"You have "
                        f"{len(upcoming)} upcoming "
                        f"assessment(s). "
                        f"The next one is "
                        f"{first['title']} on "
                        f"{first['assessment_date']}."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "You currently have no "
                        "upcoming assessments."
                    )

                return payload

            # =====================================
            # PENDING ASSESSMENTS
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "pending",
                    "not completed",
                    "unfinished",
                    "missed",
                    "require action",
                    "pending assessment",
                    "pending assessments"
                ]
            ):

                if pending:

                    first = pending[0]

                    payload[
                        "direct_answer"
                    ] = (
                        f"You have "
                        f"{len(pending)} pending "
                        f"assessment(s). "
                        f"The next pending assessment is "
                        f"{first['title']}."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "You currently have no "
                        "pending assessments."
                    )

                return payload

            # =====================================
            # HIGHEST SCORE
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "highest",
                    "best assessment",
                    "top assessment",
                    "highest score",
                    "highest scoring"
                ]
            ):

                if highest_assessment:

                    payload[
                        "direct_answer"
                    ] = (
                        f"Your highest scoring "
                        f"assessment was "
                        f"{highest_assessment['title']} "
                        f"with "
                        f"{highest_assessment['percentage']}%."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "No graded assessments "
                        "found."
                    )

                return payload

            # =====================================
            # LOWEST SCORE
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "lowest",
                    "worst assessment",
                    "lowest score",
                    "lowest scoring",
                    "needs attention"
                ]
            ):

                if lowest_assessment:

                    payload[
                        "direct_answer"
                    ] = (
                        f"Your lowest scoring "
                        f"assessment was "
                        f"{lowest_assessment['title']} "
                        f"with "
                        f"{lowest_assessment['percentage']}%."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "No graded assessments "
                        "found."
                    )

                return payload

            # =====================================
            # LATEST RESULT
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "latest result",
                    "latest assessment",
                    "latest test",
                    "what was my score",
                    "what marks did i get",
                    "show my grades",
                    "latest grade"
                ]
            ):

                if latest_result:

                    payload[
                        "direct_answer"
                    ] = (
                        f"Your latest assessment "
                        f"was "
                        f"{latest_result['title']}. "
                        f"You scored "
                        f"{latest_result['marks_obtained']}/"
                        f"{latest_result['total_marks']} "
                        f" ({latest_result['percentage']}%)."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "No assessment results "
                        "available."
                    )

                return payload

            # =====================================
            # FEEDBACK
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "feedback",
                    "teacher comment",
                    "teacher comments",
                    "teacher feedback"
                ]
            ):

                if recent_feedback:

                    latest = recent_feedback[0]

                    payload[
                        "direct_answer"
                    ] = (
                        f"Latest teacher feedback "
                        f"was on "
                        f"{latest['title']}: "
                        f"{latest['teacher_comment']}"
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "No assessment feedback "
                        "available."
                    )

                return payload

            # =====================================
            # ASSESSMENT ANALYSIS
            # =====================================

            if any(
                phrase in query
                for phrase in [
                    "performing",
                    "performance",
                    "assessment performance",
                    "assessment analysis",
                    "analyze my assessments",
                    "analyze my performance",
                    "how am i doing",
                    "average score",
                    "assessment summary",
                    "assessment review",
                    "improve my assessments",
                    "why are my scores dropping"
                ]
            ):

                payload[
                    "assessment_analysis"
                ] = True

                return payload

            return payload