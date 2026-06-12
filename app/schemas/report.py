from pydantic import BaseModel


class SummaryReportResponse(BaseModel):
    total_samples: int
    average_weight: float
    min_weight: float
    max_weight: float
    status_counts: dict[str, int]
