import logging

from llm.client import (
    chat_completion
)

from intents.student.schemas import (
    ParsedStudentIntent
)

from intents.student.prompts import (
    get_student_intent_prompt
)

from intents.base.parser import (
    parse_llm_json
)

from intents.base.fallbacks import (
    build_fallback_student_intent
)

logger = logging.getLogger(__name__)


async def parse_student_intent(
    query: str
) -> ParsedStudentIntent:

    response = await chat_completion(
        messages=[
            {
                "role": "system",
                "content": get_student_intent_prompt()
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    content = response["message"]["content"]

    logger.info(
        "Intent parser response: %s",
        content
    )

    try:

        parsed = parse_llm_json(
            content
        )

        parsed["original_query"] = query

        return ParsedStudentIntent(
            **parsed
        )

    except Exception:

        fallback = (
            build_fallback_student_intent()
        )

        fallback["original_query"] = query

        return ParsedStudentIntent(
            **fallback
        )