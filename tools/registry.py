from tools.attendance_tool import (
    AttendanceTool
)
from tools.atlas_tool import (
    AtlasTool
)
from tools.homework_tool import (
    HomeworkTool
)
from tools.assessment_tool import (
    AssessmentTool
)

TOOL_REGISTRY = {

    "atlas_tool": AtlasTool(),

    "attendance_tool": AttendanceTool(),

    "homework_tool": HomeworkTool(),

    "assessment_tool": AssessmentTool(),
}