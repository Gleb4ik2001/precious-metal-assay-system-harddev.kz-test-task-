from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base


class SampleStatus(str, Enum):
    CREATED = "created"
    MEASURED = "measured"
    APPROVED = "approved"
    REJECTED = "rejected"


class Sample(Base):
    __tablename__ = "samples"

    id: Mapped[int] = mapped_column(primary_key=True)

    sample_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    weight: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    operator: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default=SampleStatus.CREATED.value
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
