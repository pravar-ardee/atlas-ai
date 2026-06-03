import json
import re
import logging

logger = logging.getLogger(__name__)


def parse_llm_json(
    content: str
) -> dict:

    if not content:
        raise ValueError(
            "Empty LLM response"
        )

    try:

        return json.loads(
            content
        )

    except Exception:
        pass

    try:

        cleaned = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(
            cleaned
        )

    except Exception:
        pass

    try:

        match = re.search(
            r"\{.*\}",
            content,
            re.DOTALL
        )

        if match:

            return json.loads(
                match.group()
            )

    except Exception:
        pass

    logger.error(
        "Failed to parse LLM JSON response: %s",
        content
    )

    raise ValueError(
        "Unable to parse LLM response as JSON"
    )