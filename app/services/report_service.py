from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sample import Sample


class ReportService:

    @staticmethod
    def get_summary(db: Session) -> dict:

        total_samples = db.query(
            func.count(Sample.id)
        ).scalar()

        average_weight = db.query(
            func.avg(Sample.weight)
        ).scalar()

        min_weight = db.query(
            func.min(Sample.weight)
        ).scalar()

        max_weight = db.query(
            func.max(Sample.weight)
        ).scalar()

        status_counts_query = (
            db.query(
                Sample.status,
                func.count(Sample.id)
            )
            .group_by(Sample.status)
            .all()
        )

        status_counts = {
            status: count
            for status, count in status_counts_query
        }

        return {
            "total_samples": total_samples,
            "average_weight": average_weight,
            "min_weight": min_weight,
            "max_weight": max_weight,
            "status_counts": status_counts
        }
