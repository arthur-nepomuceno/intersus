import uuid
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .schemas import PatientCreate, PatientResponse
from .models import Patient
from .db import SessionLocal

router = APIRouter()

# Dependência para obter uma sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint: Criar novo paciente
@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED, tags=["Patients"])
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
   new_patient = Patient(
      id=str(uuid.uuid4()),
      name=patient.name,
      birthDate=patient.birthDate,
      gender=patient.gender
   )
   
   db.add(new_patient)
   db.commit()
   db.refresh(new_patient)
   return new_patient