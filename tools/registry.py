from tools.attendance_tool import (
    AttendanceTool
)
from tools.atlas_tool import (
    AtlasTool
)
TOOL_REGISTRY = {

     "atlas_tool": AtlasTool(),

    "attendance_tool": AttendanceTool()

}