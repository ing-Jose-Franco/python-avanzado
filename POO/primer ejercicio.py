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

Juan = estudiante("Juan", 20, "Informatica")
María = estudiante("María", 22, "Medicina")

Juan.mostrar_informacion()
María.mostrar_informacion()