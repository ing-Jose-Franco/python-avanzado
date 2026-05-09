class estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print("<<<Información del estudiante>>>")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera} \n")

class estudiante_universitario(estudiante):
    def __init__(self, nombre, edad, carrera, materia):
        super().__init__(nombre, edad, carrera)

        self.materia = materia

    def mostrar_materia(self):
        print(f"Materia: {self.materia} \n")

class estudiante_secundaria(estudiante):
    def __init__(self, nombre, edad, carrera, calificacion):
        super().__init__(nombre, edad, carrera)
        self.calificacion = calificacion

    def mostrar_calificacion(self):
        print(f"Calificación: {self.calificacion} \n")

    
Juan = estudiante_universitario("Juan", 20, "Informatica", "Programación")
María = estudiante_secundaria("María", 22, "Medicina", 9.5)

Juan.mostrar_informacion()
Juan.mostrar_materia()
María.mostrar_informacion()
María.mostrar_calificacion()