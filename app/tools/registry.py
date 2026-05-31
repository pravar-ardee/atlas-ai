from app.tools.attendance_tool import AttendanceTool
from app.tools.homework_tool import HomeworkTool
from app.tools.assessment_tool import AssessmentTool


TOOL_REGISTRY = {

    "attendance_tool": AttendanceTool(),

    "homework_tool": HomeworkTool(),

    "assessment_tool": AssessmentTool(),
}