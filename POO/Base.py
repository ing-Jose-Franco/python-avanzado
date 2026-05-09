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

#Creando un objeto de la clase Humano
gringo = Humano("marrones", "negro", "clara", 1.75, 70, "masculino")
chino = Humano("marrones", "negro", "amarilla", 1.65, 60, "masculino")

#Accediendo a los atributos del objeto
gringo.hablar()
chino.hablar()