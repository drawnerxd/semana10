from ..schemas.estudiante import Estudiante
class EstudianteService:
    def __init__(self):
        self.__listaEstudiantes: list[Estudiante] = []

    def guardarEstudiante(self, estudianteNuevo: Estudiante):
        self.__listaEstudiantes.append(estudianteNuevo)
        return estudianteNuevo

    def mostrarEstudiante(self):
        return self.__listaEstudiantes

    def actualizarEstudiante(self):
        pass

    def eliminarEstudiante(self):
        pass