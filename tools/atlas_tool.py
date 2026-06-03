from intents.student.enums import (
    StudentIntent
)

from db.session import (
    AsyncSessionLocal
)

from db.repositories.atlas_repository import (
    AtlasRepository
)


class AtlasTool:

    IMPLEMENTED_METRICS = {

        "academic": [
            "subject_grade_score",
            "homework_quality_score",
            "exam_readiness_score"
        ],

        "growth": [
            "attendance_score",
            "consistency_score",
            "conduct_score"
        ],

        "initiative": [
            "contribution_score"
        ]
    }

    async def run(
        self,
        context,
        parsed_intent
    ):

        if not context.enrollment_id:

            return {
                "error": "Enrollment ID missing"
            }

        async with AsyncSessionLocal() as db:

            repo = AtlasRepository(
                db
            )

            score = await repo.get_display_score(
                context.enrollment_id
            )

            pillars = await repo.get_live_pillars(
                context.enrollment_id
            )

            if not pillars:

                return {
                    "error": "No atlas data found"
                }

            academic = pillars.get(
                "academic",
                {}
            )

            growth = pillars.get(
                "growth",
                {}
            )

            initiative = pillars.get(
                "initiative",
                {}
            )

            academic_score = (
                academic.get(
                    "score",
                    0
                )
            )

            growth_score = (
                growth.get(
                    "score",
                    0
                )
            )

            initiative_score = (
                initiative.get(
                    "score",
                    0
                )
            )

            # =====================================
            # OVERALL PILLARS
            # =====================================

            all_pillar_scores = {

                "academic":
                    academic_score,

                "growth":
                    growth_score,

                "initiative":
                    initiative_score
            }

            strongest_pillar = max(
                all_pillar_scores,
                key=all_pillar_scores.get
            )

            # =====================================
            # ACTIONABLE PILLARS
            # =====================================

            actionable_pillars = {

                "academic":
                    academic_score,

                "growth":
                    growth_score
            }

            strongest_actionable_pillar = max(
                actionable_pillars,
                key=actionable_pillars.get
            )

            weakest_actionable_pillar = min(
                actionable_pillars,
                key=actionable_pillars.get
            )

            # =====================================
            # INSIGHTS
            # =====================================

            insights = []

            recommended_focus = []

            if (
                academic.get(
                    "homework_quality_score",
                    0
                )
                <
                academic.get(
                    "subject_grade_score",
                    0
                )
            ):

                insights.append(
                    "Homework quality is lower than subject grades."
                )

                recommended_focus.append(
                    "homework_quality_score"
                )

            if (
                growth.get(
                    "attendance_score",
                    0
                )
                == 0
            ):

                insights.append(
                    "Attendance score is currently 0."
                )

                recommended_focus.append(
                    "attendance_score"
                )

            if (
                growth.get(
                    "consistency_score",
                    0
                )
                < 70
            ):

                insights.append(
                    "Consistency score is below target."
                )

                recommended_focus.append(
                    "consistency_score"
                )

            if (
                growth.get(
                    "conduct_score",
                    0
                )
                < 80
            ):

                insights.append(
                    "Conduct score has room for improvement."
                )

                recommended_focus.append(
                    "conduct_score"
                )

            payload = {

                "atlas_score":
                    score,

                "pillars":
                    pillars,

                "strongest_pillar":
                    strongest_pillar,

                "strongest_actionable_pillar":
                    strongest_actionable_pillar,

                "weakest_actionable_pillar":
                    weakest_actionable_pillar,

                "implemented_metrics":
                    self.IMPLEMENTED_METRICS,

                "insights":
                    insights,

                "recommended_focus":
                    recommended_focus,

                "performance_summary": {

                    "strongest":
                        strongest_actionable_pillar,

                    "weakest":
                        weakest_actionable_pillar,

                    "focus":
                        recommended_focus,

                    "insights":
                        insights,

                    "message": (
                        f"{weakest_actionable_pillar} "
                        "is currently the weakest "
                        "actionable pillar."
                    )
                }
            }

            query = (
                parsed_intent.original_query or ""
            ).lower()

            if (
                "weakest pillar" in query
                or
                "which pillar is weakest" in query
            ):

                payload["direct_answer"] = (
                    f"{weakest_actionable_pillar} "
                    "is currently the weakest "
                    "actionable pillar."
                )

            if (
                "strongest pillar" in query
                or
                "which pillar is strongest" in query
            ):

                payload["direct_answer"] = (
                    f"{strongest_actionable_pillar} "
                    "is currently the strongest "
                    "actionable pillar."
                )

            # =====================================
            # PERFORMANCE ANALYSIS
            # =====================================

            if (
                parsed_intent.intent
                ==
                StudentIntent.STUDENT_PERFORMANCE
            ):

                payload[
                    "performance_analysis"
                ] = True

                return payload

            # =====================================
            # ATLAS SCORE CALIBRATION
            # =====================================

            if score is None:

                payload["atlas_score"] = {

                    "status":
                        "calibrating",

                    "message": (
                        "Atlas Score is currently "
                        "calibrating. Your first "
                        "weekly Atlas Score will "
                        "be available next week."
                    )
                }

            return payload