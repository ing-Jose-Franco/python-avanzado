class Humano:

    #Atributos
    def __init__(self, ojos, cabello, piel, altura, peso, genero="desconocido"):

        #atributos de instancia
        self.ojos = ojos
        self.cabello = cabello
        self.piel = piel
        self.altura = altura
        self.peso = peso
        self.genero = genero   

    def hablar(self):
        print("Hola, soy un humano y puedo hablar")

class Trabajador(Humano):
    def __init__(self, ojos, cabello, piel, altura, peso, profesion, genero="desconocido"):
        super().__init__(ojos, cabello, piel, altura, peso, genero)
        self.profesion = profesion
    
    def trabajar(self):
        print(f"Hola, soy un {self.profesion} y estoy trabajando")

arquitecto = Trabajador("marrones", "negro", "clara", 1.75, 70, "arquitecto", "masculino")
arquitecto.hablar()
arquitecto.trabajar()