class Equipo:
    def __init__(self, nombre, puntos):
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre del equipo debe ser una cadena no vacía.")
        if not isinstance(puntos, (int, float)) or puntos < 0:
            raise ValueError("Los puntos deben ser un número mayor o igual a 0.")

        self.nombre = nombre
        self.puntos = puntos

    def __repr__(self):
        return f"Equipo(nombre={self.nombre!r}, puntos={self.puntos})"


def generar_emparejamientos(equipos):
    equipos_ordenados = sorted(equipos, key=lambda e: e.puntos, reverse=True)
    emparejamientos = []

    while len(equipos_ordenados) >= 2:
        equipo_alto = equipos_ordenados[0]
        equipo_bajo = equipos_ordenados[-1]

        if equipo_alto.puntos >= equipo_bajo.puntos:
            encuentro = {
                "primero": equipo_alto.nombre,
                "segundo": equipo_bajo.nombre,
                "favorito": equipo_alto.nombre,
            }
        else:
            encuentro = {
                "primero": equipo_alto.nombre,
                "segundo": equipo_bajo.nombre,
                "favorito": equipo_bajo.nombre,
            }

        emparejamientos.append(encuentro)
        equipos_ordenados = equipos_ordenados[1:-1]

    return emparejamientos


if __name__ == "__main__":
    equipos = [
        Equipo("Pixel Warriors", 82),
        Equipo("Cyber Ninjas", 76),
        Equipo("Arcade Rangers", 69),
        Equipo("Storm Breakers", 58),
    ]

    llaves = generar_emparejamientos(equipos)
    for llave in llaves:
        print(f"{llave['primero']} vs {llave['segundo']} - favorito: {llave['favorito']}")
