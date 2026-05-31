from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from app.schemas.ai import AIRequest

from app.core.security import (
    verify_internal_api_key
)

from app.planner.intent_parser import (
    parse_intent
)

from app.planner.tool_router import (
    get_tools_for_intent
)

from app.tools.registry import (
    TOOL_REGISTRY
)

from app.llm.summarizer import (
    summarize_response
)

router = APIRouter()


@router.post("/query")
async def ai_query(
    payload: AIRequest,
    _: str = Depends(
        verify_internal_api_key
    )
):

    try:

        parsed_intent = await parse_intent(
            query=payload.query
        )

        tools_to_run = get_tools_for_intent(
            intent=parsed_intent["intent"]
        )

        results = {}

        for tool_name in tools_to_run:

            tool = TOOL_REGISTRY.get(tool_name)

            if not tool:
                continue

            result = await tool.run(
                context=payload.context,
                parsed_intent=parsed_intent
            )

            results[tool_name] = result

        summary = await summarize_response(
            query=payload.query,
            data=results,
            context=payload.context
        )

        return {
            "success": True,
            "intent": parsed_intent,
            "data": results,
            "summary": summary
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )