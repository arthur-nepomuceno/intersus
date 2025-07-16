from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PatientCreate(BaseModel):
    name: str = Field(..., example="Maria da Silva")
    birthDate: date = Field(..., example="1980-05-12")
    gender: Optional[str] = Field(None, example="female")

class PatientResponse(PatientCreate):
    id: str = Field(..., example="12345")