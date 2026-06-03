import logging

from llm.client import chat_completion

logger = logging.getLogger(__name__)


async def summarize_response(
    query: str,
    data: dict,
    context
):

    prompt = f"""
You are an ERP analytics assistant.

USER QUERY:
{query}

ANALYTICS DATA:
{data}

Generate a concise response.
"""

    response = await chat_completion(
        [
            {
                "role": "system",
                "content": "You are an ERP analytics assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    logger.info(
        "Summarizer response: %s",
        response
    )

    return response["message"]["content"]