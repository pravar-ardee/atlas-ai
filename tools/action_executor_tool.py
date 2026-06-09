import logging

from db.session import (
    AsyncSessionLocal
)

from cache.pending_action_cache import (
    PendingActionCache
)

from db.repositories.personal_event_repository import (
    PersonalEventRepository
)

from services.event_mapper import (
    EVENT_TYPE_MAP
)

logger = logging.getLogger(__name__)


class ActionExecutorTool:

    async def run(
        self,
        context,
        parsed_intent
    ):

        pending_action = (
            await PendingActionCache.get(
                context.user_id
            )
        )

        if not pending_action:

            return {

                "module":
                    "action",

                "direct_answer":
                    (
                        "There is no pending "
                        "action to confirm."
                    )
            }

        logger.info(
            "Pending action found: %s",
            pending_action
        )

        action_type = (
            pending_action.get(
                "action_type"
            )
        )

        payload = (
            pending_action.get(
                "payload",
                {}
            )
        )

        # =====================================
        # CREATE PERSONAL EVENT
        # =====================================

        if (
            action_type
            ==
            "create_personal_event"
        ):

            async with AsyncSessionLocal() as db:

                repo = (
                    PersonalEventRepository(
                        db
                    )
                )

                event = (
                    await repo.create_event(

                        student_id=
                            context.student_id,

                        title=
                            payload.get(
                                "title"
                            ),

                        event_type=
                            EVENT_TYPE_MAP.get(
                                payload.get(
                                    "event_type",
                                    "PERSONAL"
                                ),
                                1
                            ),

                        start_datetime=
                            payload.get(
                                "start_datetime"
                            ),

                        end_datetime=
                            payload.get(
                                "end_datetime"
                            ),

                        description=
                            payload.get(
                                "description"
                            )
                    )
                )

            await PendingActionCache.delete(
                context.user_id
            )

            logger.info(
                "Personal event created: %s",
                event
            )

            return {

                "module":
                    "action",

                "action_completed":
                    True,

                "action_type":
                    "create_personal_event",

                "event_id":
                    event["id"],

                "direct_answer":
                    (
                        f"Your event "
                        f"'{payload.get('title')}' "
                        f"has been created."
                    )
            }

        # =====================================
        # UNKNOWN ACTION
        # =====================================

        return {

            "module":
                "action",

            "direct_answer":
                (
                    "Unsupported action."
                )
        }