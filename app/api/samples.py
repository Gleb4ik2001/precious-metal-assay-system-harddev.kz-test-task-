from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.sample import (
    SampleCreate,
    SampleResponse,
    SampleStatusUpdate
)

from app.services.sample_service import SampleService


router = APIRouter(
    prefix="/samples",
    tags=["Samples"]
)


@router.post(
    "",
    response_model=SampleResponse,
    status_code=201
)
def create_sample(
    sample_data: SampleCreate,
    db: Session = Depends(get_db)
):

    return SampleService.create_sample(
        db=db,
        sample_data=sample_data
    )


@router.get(
    "",
    response_model=list[SampleResponse]
)
def get_samples(
    db: Session = Depends(get_db)
):

    return SampleService.get_all_samples(db)


@router.get(
    "/{sample_id}",
    response_model=SampleResponse
)
def get_sample(
    sample_id: int,
    db: Session = Depends(get_db)
):

    sample = SampleService.get_sample_by_id(
        db,
        sample_id
    )

    if sample is None:
        raise HTTPException(
            status_code=404,
            detail="Sample not found"
        )

    return sample


@router.patch(
    "/{sample_id}/status",
    response_model=SampleResponse
)
def update_status(
    sample_id: int,
    status_data: SampleStatusUpdate,
    db: Session = Depends(get_db)
):

    sample = SampleService.get_sample_by_id(
        db,
        sample_id
    )

    if sample is None:
        raise HTTPException(
            status_code=404,
            detail="Sample not found"
        )

    return SampleService.update_status(
        db=db,
        sample=sample,
        status=status_data.status.value
    )