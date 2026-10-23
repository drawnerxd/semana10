from fastapi import FastAPI
from .apis.estudiante_api import rutaEstudiantes

app = FastAPI()

app.include_router(rutaEstudiantes, prefix='/api')