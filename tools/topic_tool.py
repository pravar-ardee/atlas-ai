from db.session import (
    AsyncSessionLocal
)

from db.repositories.topic_repository import (
    TopicRepository
)


class TopicTool:

    async def run(
        self,
        context,
        parsed_intent
    ):

        query = (
            getattr(
                parsed_intent,
                "original_query",
                ""
            )
            .lower()
        )

        async with AsyncSessionLocal() as db:

            repo = TopicRepository(
                db
            )

            completed = (
                await repo.get_completed_topics(
                    context.enrollment_id
                )
            )

            pending = (
                await repo.get_pending_topics(
                    context.enrollment_id,
                    context.academic_class_id
                )
            )

            assessment_topics = (
                await repo.get_assessment_topics(
                    context.enrollment_id
                )
            )

            payload = {

                "module":
                    "topic",

                "completed_count":
                    len(completed),

                "pending_count":
                    len(pending),

                "completed_topics":
                    completed,

                "pending_topics":
                    pending,

                "assessment_topics":
                    assessment_topics
            }

            if "completed" in query:

                payload[
                    "direct_answer"
                ] = (
                    f"You have completed "
                    f"{len(completed)} topic(s)."
                )

                return payload

            if any(
                phrase in query
                for phrase in [
                    "pending",
                    "left",
                    "not completed"
                ]
            ):

                payload[
                    "direct_answer"
                ] = (
                    f"You have "
                    f"{len(pending)} pending "
                    f"topic(s)."
                )

                return payload

            if any(
                phrase in query
                for phrase in [
                    "study next",
                    "revise",
                    "assessment topics"
                ]
            ):

                if assessment_topics:

                    payload[
                        "direct_answer"
                    ] = (
                        f"There are "
                        f"{len(assessment_topics)} "
                        f"assessment-related topics "
                        f"available for review."
                    )

                else:

                    payload[
                        "direct_answer"
                    ] = (
                        "No assessment topics "
                        "available."
                    )

                return payload

            payload[
                "topic_analysis"
            ] = True

            return payload