from sqlalchemy.orm import Session

from app.models.sample import Sample
from app.schemas.sample import SampleCreate
from app.models.sample import SampleStatus


class SampleService:

    @staticmethod
    def create_sample(
        db: Session,
        sample_data: SampleCreate
    ) -> Sample:

        sample = Sample(
            sample_code=sample_data.sample_code,
            weight=sample_data.weight,
            operator=sample_data.operator,
            status=SampleStatus.CREATED.value
        )

        db.add(sample)
        db.commit()
        db.refresh(sample)

        return sample

    @staticmethod
    def get_all_samples(
        db: Session
    ) -> list[Sample]:

        return db.query(Sample).all()

    @staticmethod
    def get_sample_by_id(
        db: Session,
        sample_id: int
    ) -> Sample | None:

        return (
            db.query(Sample)
            .filter(Sample.id == sample_id)
            .first()
        )

    @staticmethod
    def update_status(
        db: Session,
        sample: Sample,
        status: str
    ) -> Sample:

        sample.status = status

        db.commit()
        db.refresh(sample)

        return sample
