class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, estados=()):
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(vida, (int, float)) or vida <= 0:
            raise ValueError("La vida debe ser un número mayor que cero.")
        if not isinstance(ataque, (int, float)) or ataque < 0:
            raise ValueError("El ataque debe ser un número mayor o igual a cero.")
        if not isinstance(defensa, (int, float)) or defensa < 0:
            raise ValueError("La defensa debe ser un número mayor o igual a cero.")
        if not isinstance(estados, tuple):
            raise ValueError("Los estados deben ser una tupla.")

        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.estados = estados

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, daño):
        if daño <= 0:
            return
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0

    def __str__(self):
        return f"{self.nombre}: vida={self.vida}, ataque={self.ataque}, defensa={self.defensa}, estados={self.estados}"


def ejecutar_ronda(guerrero_a, guerrero_b):
    turno = 1
    while guerrero_a.esta_vivo() and guerrero_b.esta_vivo():
        if turno % 2 == 1:
            atacante, defensor = guerrero_a, guerrero_b
        else:
            atacante, defensor = guerrero_b, guerrero_a

        if "atontado" in atacante.estados:
            daño = 0
        else:
            ventaja = 1.0
            if "fuerte" in atacante.estados:
                ventaja += 0.25
            if "debil" in atacante.estados:
                ventaja -= 0.2

            daño_base = atacante.ataque * ventaja
            reducción = defensor.defensa * 0.5
            daño = daño_base - reducción
            if "escudo" in defensor.estados:
                daño *= 0.8
            if daño < 1:
                daño = 1

        defensor.recibir_daño(daño)
        print(f"Turno {turno}: {atacante.nombre} ataca a {defensor.nombre} y causa {daño:.1f} puntos de daño.")
        print(f"      {defensor.nombre} tiene {defensor.vida:.1f} vida restante.")

        if not defensor.esta_vivo():
            print(f"{defensor.nombre} ha caído. {atacante.nombre} gana la ronda.")
            break

        turno += 1

    return guerrero_a, guerrero_b


if __name__ == "__main__":
    heroe = Guerrero("Hércules", 120, 25, 10, estados=("fuerte",))
    enemigo = Guerrero("Orco", 100, 20, 12, estados=("escudo",))

    ejecutar_ronda(heroe, enemigo)
