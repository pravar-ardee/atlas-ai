from app.llm.client import chat_completion


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

    response = await chat_completion([
        {
            "role": "system",
            "content": "You are an ERP analytics assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ])

    return response["choices"][0]["message"]["content"]