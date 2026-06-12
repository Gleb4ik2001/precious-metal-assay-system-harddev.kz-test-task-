from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.report import SummaryReportResponse
from app.services.report_service import ReportService


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/summary",
    response_model=SummaryReportResponse
)
def get_summary_report(
    db: Session = Depends(get_db)
):
    return ReportService.get_summary(db)