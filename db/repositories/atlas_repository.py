from datetime import date
from datetime import timedelta

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


class AtlasRepository:

    def __init__(
        self,
        db: AsyncSession
    ):
        self.db = db

    async def get_display_score(
        self,
        enrollment_id: int
    ):

        today = date.today()

        current_week_monday = (
            today -
            timedelta(
                days=today.weekday()
            )
        )

        previous_week_monday = (
            current_week_monday -
            timedelta(days=7)
        )

        atlas_query = text(
            """
            SELECT *

            FROM analytics_student_daily_atlas_score

            WHERE enrollment_id = :enrollment_id

            AND snapshot_date < :current_week_monday

            ORDER BY snapshot_date DESC

            LIMIT 1
            """
        )

        previous_query = text(
            """
            SELECT *

            FROM analytics_student_daily_atlas_score

            WHERE enrollment_id = :enrollment_id

            AND snapshot_date < :previous_week_monday

            ORDER BY snapshot_date DESC

            LIMIT 1
            """
        )

        atlas_result = await self.db.execute(
            atlas_query,
            {
                "enrollment_id": enrollment_id,
                "current_week_monday":
                    current_week_monday
            }
        )

        previous_result = await self.db.execute(
            previous_query,
            {
                "enrollment_id": enrollment_id,
                "previous_week_monday":
                    previous_week_monday
            }
        )

        current_snapshot = (
            atlas_result
            .mappings()
            .first()
        )

        previous_snapshot = (
            previous_result
            .mappings()
            .first()
        )

        if not current_snapshot:
            return None

        current_score = float(
            current_snapshot["atlas_score"]
        )

        previous_score = (
            float(
                previous_snapshot["atlas_score"]
            )
            if previous_snapshot
            else 0
        )

        change = round(
            current_score -
            previous_score,
            2
        )

        return {

            "score":
                current_score,

            "band":
                current_snapshot["band"],

            "change":
                change,

            "change_type":
                (
                    "increase"
                    if change > 0
                    else "decrease"
                    if change < 0
                    else "same"
                ),

            "snapshot_date":
                current_snapshot[
                    "snapshot_date"
                ]
        }

    async def get_live_pillars(
        self,
        enrollment_id: int
    ):

        query = text(
            """
            SELECT *

            FROM analytics_student_daily_atlas_score

            WHERE enrollment_id = :enrollment_id

            ORDER BY snapshot_date DESC

            LIMIT 1
            """
        )

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        latest = (
            result
            .mappings()
            .first()
        )

        if not latest:
            return None

        return {

            "academic": {

                "score":
                    float(
                        latest[
                            "academic_score"
                        ]
                    ),

                "subject_grade_score":
                    latest[
                        "subject_grade_score"
                    ],

                "homework_quality_score":
                    latest[
                        "homework_quality_score"
                    ],

                "exam_readiness_score":
                    latest[
                        "exam_readiness_score"
                    ]
            },

            "growth": {

                "score":
                    float(
                        latest[
                            "growth_score"
                        ]
                    ),

                "attendance_score":
                    latest[
                        "attendance_score"
                    ],

                "consistency_score":
                    latest[
                        "consistency_score"
                    ],

                "conduct_score":
                    latest[
                        "conduct_score"
                    ]
            },

            "initiative": {

                "score":
                    float(
                        latest[
                            "initiative_score"
                        ]
                    ),

                "curiosity_score":
                    latest[
                        "curiosity_score"
                    ],

                "preparation_score":
                    latest[
                        "preparation_score"
                    ],

                "contribution_score":
                    latest[
                        "contribution_score"
                    ],

                "extracurricular_score":
                    latest[
                        "extracurricular_score"
                    ]
            }
        }