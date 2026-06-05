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

from tools.announcement_tool import (
    AnnouncementTool
)

from tools.forum_tool import (
    ForumTool
)

from tools.subject_tool import (
    SubjectTool
)

from tools.topic_tool import (
    TopicTool
)

TOOL_REGISTRY = {

    "atlas_tool": AtlasTool(),

    "attendance_tool": AttendanceTool(),

    "homework_tool": HomeworkTool(),

    "assessment_tool": AssessmentTool(),

    "announcement_tool": AnnouncementTool(),
    
    "forum_tool": ForumTool(),

    "subject_tool": SubjectTool(),

    "topic_tool": TopicTool()
}