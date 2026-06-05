from sqlalchemy import text


class AssessmentRepository:

    def __init__(self, db):

        self.db = db

    # =====================================================
    # UPCOMING ASSESSMENTS
    # =====================================================

    async def get_upcoming_assessments(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.assessment_date,
                a.total_marks,
                a.type

            FROM students_assessmentstudentmap asm

            INNER JOIN students_assessment a
                ON a.id = asm.assessment_id

            WHERE asm.enrollment_id = :enrollment_id

            AND a.assessment_date >= CURRENT_DATE

            ORDER BY a.assessment_date ASC

            LIMIT 20
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        rows = result.mappings().all()

        return [
            dict(row)
            for row in rows
        ]

    # =====================================================
    # PENDING ASSESSMENTS
    # =====================================================

    async def get_pending_assessments(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.assessment_date,
                a.total_marks

            FROM students_assessmentstudentmap asm

            INNER JOIN students_assessment a
                ON a.id = asm.assessment_id

            LEFT JOIN students_assessmentstudentrecord r
                ON r.assessment_id = a.id
                AND r.enrollment_id = asm.enrollment_id

            WHERE asm.enrollment_id = :enrollment_id

            AND a.assessment_date >= CURRENT_DATE

            AND (
                r.id IS NULL
                OR r.status IN (1, 2)
            )

            ORDER BY a.assessment_date ASC
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        rows = result.mappings().all()

        return [
            dict(row)
            for row in rows
        ]

    # =====================================================
    # LATEST RESULT
    # =====================================================

    async def get_latest_result(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.total_marks,
                a.assessment_date,
                a.type,

                r.marks_obtained,
                r.grade,
                r.teacher_comment,
                r.graded_at

            FROM students_assessmentstudentrecord r

            INNER JOIN students_assessment a
                ON a.id = r.assessment_id

            WHERE r.enrollment_id = :enrollment_id

            AND r.status = 3

            ORDER BY r.graded_at DESC

            LIMIT 1
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        row = result.mappings().first()

        if not row:
            return None

        row = dict(row)

        total_marks = (
            row.get("total_marks")
            or 0
        )

        obtained = (
            row.get("marks_obtained")
            or 0
        )

        percentage = 0

        if total_marks:

            percentage = round(
                (
                    obtained
                    /
                    total_marks
                ) * 100,
                2
            )

        row["percentage"] = percentage

        return row

    # =====================================================
    # PERFORMANCE SUMMARY
    # =====================================================

    async def get_performance_summary(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                COUNT(*) AS graded_count,

                AVG(
                    CASE
                        WHEN a.total_marks > 0
                        THEN (
                            r.marks_obtained
                            /
                            a.total_marks
                        ) * 100
                    END
                ) AS average_percentage,

                MAX(
                    CASE
                        WHEN a.total_marks > 0
                        THEN (
                            r.marks_obtained
                            /
                            a.total_marks
                        ) * 100
                    END
                ) AS highest_percentage,

                MIN(
                    CASE
                        WHEN a.total_marks > 0
                        THEN (
                            r.marks_obtained
                            /
                            a.total_marks
                        ) * 100
                    END
                ) AS lowest_percentage

            FROM students_assessmentstudentrecord r

            INNER JOIN students_assessment a
                ON a.id = r.assessment_id

            WHERE r.enrollment_id = :enrollment_id

            AND r.status = 3
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        row = result.mappings().first()

        if not row:

            return {
                "graded_count": 0,
                "average_percentage": 0,
                "highest_percentage": 0,
                "lowest_percentage": 0
            }

        return {

            "graded_count":
                row["graded_count"] or 0,

            "average_percentage":
                round(
                    row["average_percentage"] or 0,
                    2
                ),

            "highest_percentage":
                round(
                    row["highest_percentage"] or 0,
                    2
                ),

            "lowest_percentage":
                round(
                    row["lowest_percentage"] or 0,
                    2
                )
        }

    # =====================================================
    # HIGHEST SCORING ASSESSMENT
    # =====================================================

    async def get_highest_scoring_assessment(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.total_marks,
                a.assessment_date,
                a.type,

                r.marks_obtained,
                r.grade,
                r.teacher_comment,
                r.graded_at

            FROM students_assessmentstudentrecord r

            INNER JOIN students_assessment a
                ON a.id = r.assessment_id

            WHERE r.enrollment_id = :enrollment_id

            AND r.status = 3

            AND a.total_marks > 0

            ORDER BY
                (
                    r.marks_obtained
                    /
                    a.total_marks
                ) DESC

            LIMIT 1
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        row = result.mappings().first()

        if not row:
            return None

        row = dict(row)

        row["percentage"] = round(
            (
                row["marks_obtained"]
                /
                row["total_marks"]
            ) * 100,
            2
        )

        return row

    # =====================================================
    # LOWEST SCORING ASSESSMENT
    # =====================================================

    async def get_lowest_scoring_assessment(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.total_marks,
                a.assessment_date,
                a.type,

                r.marks_obtained,
                r.grade,
                r.teacher_comment,
                r.graded_at

            FROM students_assessmentstudentrecord r

            INNER JOIN students_assessment a
                ON a.id = r.assessment_id

            WHERE r.enrollment_id = :enrollment_id

            AND r.status = 3

            AND a.total_marks > 0

            ORDER BY
                (
                    r.marks_obtained
                    /
                    a.total_marks
                ) ASC

            LIMIT 1
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        row = result.mappings().first()

        if not row:
            return None

        row = dict(row)

        row["percentage"] = round(
            (
                row["marks_obtained"]
                /
                row["total_marks"]
            ) * 100,
            2
        )

        return row

    # =====================================================
    # RECENT FEEDBACK
    # =====================================================

    async def get_recent_feedback(
        self,
        enrollment_id: int
    ):

        query = text("""
            SELECT

                a.id,
                a.title,
                a.assessment_date,

                r.teacher_comment,
                r.marks_obtained,
                r.grade,
                r.graded_at

            FROM students_assessmentstudentrecord r

            INNER JOIN students_assessment a
                ON a.id = r.assessment_id

            WHERE r.enrollment_id = :enrollment_id

            AND r.teacher_comment IS NOT NULL

            AND TRIM(r.teacher_comment) <> ''

            ORDER BY r.graded_at DESC

            LIMIT 5
        """)

        result = await self.db.execute(
            query,
            {
                "enrollment_id": enrollment_id
            }
        )

        rows = result.mappings().all()

        return [
            dict(row)
            for row in rows
        ]