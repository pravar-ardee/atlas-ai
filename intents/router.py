from intents.student.parser import (
    parse_student_intent
)

# from intents.parent.parser import (
#     parse_parent_intent
# )

# from intents.teacher.parser import (
#     parse_teacher_intent
# )


async def parse_intent(
    query: str,
    role: str
):

    if role == "student":

        return await parse_student_intent(
            query
        )

    # if role == "parent":

    #     return await parse_parent_intent(
    #         query
    #     )

    # if role == "teacher":

    #     return await parse_teacher_intent(
    #         query
    #     )

    raise ValueError(
        f"Unsupported role: {role}"
    )