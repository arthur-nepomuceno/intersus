from fastapi import FastAPI
from .routes import router as patient_router

# Conexão com a API
app = FastAPI(
    title = "InterSUS API",
    description =  "FHIR-based healthcare API for interoperable patient records in Brazil.",
    version="0.1.0"
)

# Registra as rotas da API de pacientes
app.include_router(patient_router, prefix="/patients", tags=["Patients"])

# Endpoint de verificação de funcionamento da API
@app.get("/", tags=["Health Check"])
def read_root():
    return {"message": "InterSUS API is running."}