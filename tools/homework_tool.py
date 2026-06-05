from db.session import (
    AsyncSessionLocal
)

from db.repositories.homework_repository import (
    HomeworkRepository
)


class HomeworkTool:

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

        async with AsyncSessionLocal() as db:

            repo = HomeworkRepository(
                db
            )

            pending = (
                await repo.get_pending_homework(
                    context.enrollment_id
                )
            )

            overdue = (
                await repo.get_overdue_homework(
                    context.enrollment_id
                )
            )

            due_today = (
                await repo.get_due_today(
                    context.enrollment_id
                )
            )

            due_tomorrow = (
                await repo.get_due_tomorrow(
                    context.enrollment_id
                )
            )

            feedback = (
                await repo.get_recent_feedback(
                    context.enrollment_id
                )
            )

            return {

                "pending_count":
                    len(pending),

                "overdue_count":
                    len(overdue),

                "pending":
                    pending,

                "overdue":
                    overdue,

                "due_today":
                    due_today,

                "due_tomorrow":
                    due_tomorrow,

                "recent_feedback":
                    feedback
            }