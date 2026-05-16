#Ejercicio 10 Rpg

from abc import ABC, abstractmethod
import random

def probabilidad_critico(funcion):

    def wrapper(self, objetivo):

        dano = funcion(self, objetivo)

        if random.randint(1, 5) == 1:
            dano *= 2
            print("Golpe critico")

        objetivo.recibir_dano(dano)

    return wrapper


class PersonajeBase(ABC):

    def __init__(self, nombre, vida, ataque):
        self._nombre = nombre
        self._vida = vida
        self._ataque = ataque

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def recibir_dano(self, dano):
        pass


class Guerrero(PersonajeBase):

    @probabilidad_critico
    def atacar(self, objetivo):
        return self._ataque

    def recibir_dano(self, dano):
        self._vida -= dano


class Mago(PersonajeBase):

    @probabilidad_critico
    def atacar(self, objetivo):
        return self._ataque + 5

    def recibir_dano(self, dano):
        self._vida -= dano


class FabricaPersonajes:

    @staticmethod
    def crear(tipo):

        if tipo == "guerrero":
            return Guerrero("Guerrero", 100, 20)

        elif tipo == "mago":
            return Mago("Mago", 80, 25)


p1 = FabricaPersonajes.crear("guerrero")
p2 = FabricaPersonajes.crear("mago")

turno = 0
while p1._vida > 0 and p2._vida > 0:

    turno += 1

    if turno % 2 != 0:
        p1.atacar(p2)
        print("Vida del mago:", p2._vida)
    else:
        p2.atacar(p1)
        print("Vida del guerrero:", p1._vida)


if p1._vida > 0:
    print("Gana el guerrero")
else:
    print("Gana el mago")