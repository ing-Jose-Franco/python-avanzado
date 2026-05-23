class Videojuego:
    def __init__(self, titulo, plataforma, horas):
        if not isinstance(titulo, str) or not titulo:
            raise ValueError("El título debe ser una cadena no vacía.")
        if not isinstance(plataforma, str) or not plataforma:
            raise ValueError("La plataforma debe ser una cadena no vacía.")
        if not isinstance(horas, (int, float)) or horas < 0:
            raise ValueError("Las horas deben ser un número mayor o igual a 0.")

        self.titulo = titulo
        self.plataforma = plataforma
        self.horas = horas

    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) - {self.horas} horas"


def obtener_favoritos(videojuegos, minimo_horas=20):
    favoritos = []
    for juego in videojuegos:
        if not isinstance(juego, dict):
            continue
        if "titulo" not in juego or "plataforma" not in juego or "horas" not in juego:
            continue
        if not isinstance(juego["horas"], (int, float)):
            continue

        if juego["horas"] > minimo_horas:
            favorito = Videojuego(juego["titulo"], juego["plataforma"], juego["horas"])
            favoritos.append(favorito)

    return favoritos


if __name__ == "__main__":
    videojuegos = [
        {"titulo": "The Legend of Zelda: Breath of the Wild", "plataforma": "Switch", "horas": 160},
        {"titulo": "Spider-Man: Miles Morales", "plataforma": "PS5", "horas": 25},
        {"titulo": "Hollow Knight", "plataforma": "PC", "horas": 45},
        {"titulo": "Among Us", "plataforma": "PC", "horas": 8},
        {"titulo": "Stardew Valley", "plataforma": "Switch", "horas": 85},
    ]

    favoritos = obtener_favoritos(videojuegos, minimo_horas=30)
    print("Videojuegos favoritos:")
    for favorito in favoritos:
        print(favorito)
