import httpx

from app.core.config import settings


async def chat_completion(
    messages
):

    payload = {
        "model": "Qwen/Qwen2.5-14B-Instruct",
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": 400
    }

    async with httpx.AsyncClient(
        timeout=120
    ) as client:

        response = await client.post(
            f"{settings.VLLM_BASE_URL}/chat/completions",
            json=payload
        )

        response.raise_for_status()

        return response.json()