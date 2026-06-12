from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import field_validator

from app.models.sample import SampleStatus


class SampleCreate(BaseModel):
    sample_code: str
    weight: float
    operator: str

    @field_validator("sample_code")
    @classmethod
    def validate_sample_code(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Sample code cannot be empty")
        return value

    @field_validator("operator")
    @classmethod
    def validate_operator(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Operator cannot be empty")
        return value

    @field_validator("weight")
    @classmethod
    def validate_weight(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Weight must be greater than zero")
        return value


class SampleStatusUpdate(BaseModel):
    status: SampleStatus


class SampleResponse(BaseModel):
    id: int
    sample_code: str
    weight: float
    operator: str
    status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )