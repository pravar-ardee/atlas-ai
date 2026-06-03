from datetime import date

from pydantic import (
    BaseModel,
    Field
)

from intents.student.enums import (
    StudentIntent
)


class ParsedStudentIntent(BaseModel):

    intent: StudentIntent

    start_date: date | None = None

    end_date: date | None = None

    target_modules: list[str]

    confidence: float = Field(
        ge=0.0,
        le=1.0
    )

    original_query: str | None = None