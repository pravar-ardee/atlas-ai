from typing import List, Optional

from pydantic import BaseModel


class UserContext(BaseModel):

    user_id: int

    role: str

    campus_id: int

    accessible_class_ids: Optional[List[int]] = []

    accessible_student_ids: Optional[List[int]] = []


class AIRequest(BaseModel):

    query: str

    context: UserContext