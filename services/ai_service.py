import logging

from intents.router import (
    parse_intent
)

from routing.tool_router import (
    get_tools_for_intent
)

from tools.registry import (
    TOOL_REGISTRY
)

from llm.summarizer import (
    summarize_response
)

from services.date_service import (
    DateService
)

from cache.pending_action_cache import (
    PendingActionCache
)

logger = logging.getLogger(__name__)


class AIService:

    async def answer(
        self,
        query: str,
        context
    ):

        parsed_intent = await parse_intent(
            query=query,
            role=context.role
        )

        parsed_intent = (
            DateService.validate(
                parsed_intent
            )
        )

        logger.info(
            "Parsed Intent: %s",
            parsed_intent.model_dump()
        )

        tools_to_run = get_tools_for_intent(
            intent=parsed_intent.intent
        )

        logger.info(
            "Selected Tools: %s",
            tools_to_run
        )

        results = {}

        for tool_name in tools_to_run:

            tool = TOOL_REGISTRY.get(
                tool_name
            )

            if tool is None:
                continue

            result = await tool.run(
                context=context,
                parsed_intent=parsed_intent
            )

            results[tool_name] = result

            print(result)

        # =====================================
        # ACTION REQUIRED SHORT CIRCUIT
        # =====================================

        for tool_result in results.values():

            if (
                isinstance(tool_result, dict)
                and
                tool_result.get(
                    "action_required"
                )
            ):

                await PendingActionCache.save(

                    user_id=context.user_id,

                    action_type=
                        tool_result.get(
                            "action_type"
                        ),

                    payload=
                        tool_result.get(
                            "payload",
                            {}
                        )
                )

                logger.info(
                    "Pending action stored: %s",
                    tool_result.get(
                        "action_type"
                    )
                )

                return {

                    "success": True,

                    "query":
                        query,

                    "intent":
                        parsed_intent.model_dump(),

                    "data":
                        results,

                    "summary":
                        tool_result.get(
                            "confirmation_message"
                        ),

                    "action_required":
                        True,

                    "confirmation_required":
                        tool_result.get(
                            "confirmation_required",
                            False
                        ),

                    "action_type":
                        tool_result.get(
                            "action_type"
                        )
                }

        # =====================================
        # DIRECT ANSWER SHORT CIRCUIT
        # =====================================

        direct_answer = None

        for tool_result in results.values():

            if not isinstance(
                tool_result,
                dict
            ):
                continue

            answer = tool_result.get(
                "direct_answer"
            )

            if answer:

                direct_answer = answer
                break

        # =====================================
        # SKIP LLM FOR DETERMINISTIC ANSWERS
        # =====================================

        if direct_answer:

            logger.info(
                "Using direct answer: %s",
                direct_answer
            )

            summary = direct_answer

        else:

            summary = await summarize_response(
                query=query,
                data=results,
                context=context,
                intent=parsed_intent.intent
            )

        return {

            "success": True,

            "query":
                query,

            "intent":
                parsed_intent.model_dump(),

            "data":
                results,

            "summary":
                summary
        }