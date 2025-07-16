from fastapi import APIRouter, HTTPException, status

router = APIRouter()

# Endpoint: Criar novo paciente
@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED, tags=["Patients"])
def create_patient(patient: PatientCreate):
    # Placeholder implementation (to be replaced with DB logic)
    if not patient.name:
        raise HTTPException(status_code=400, detail="Name is required.")
    
    return {
        "id": "12345",
        "name": patient.name,
        "birthDate": patient.birthDate,
        "gender": patient.gender
    }