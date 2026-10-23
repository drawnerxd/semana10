from fastapi import APIRouter
from ..services.estudiante_service import EstudianteService
from ..schemas.estudiante import Estudiante
rutaEstudiantes = APIRouter(prefix='/estudiantes', tags=['Estudiantes'])

estudianteServicio = EstudianteService()

@rutaEstudiantes.post('/')
def guardarEstudiante(estudianteNuevo:Estudiante):
    return estudianteServicio.guardarEstudiante(estudianteNuevo)

@rutaEstudiantes.get('/')
def mostrasEstudiante():
    return estudianteServicio.mostrarEstudiante()

def actualizarEstudiante():
    pass

def eliminarEstudiante():
    pass
