class Articulo:
    def __init__(self, nombre: str, categoria: str, precio: float):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)

    def __repr__(self):
        return f"Articulo(nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio})"


def procesar_carrito(articulos, descuentos):
    total = 0.0

    for articulo in articulos:
        tasa = descuentos.get(articulo.categoria, 1.0)
        total += articulo.precio * tasa

    return round(total, 2)


if __name__ == '__main__':
    descuentos = {
        'ropa': 0.9,
        'electronica': 0.8,
        'hogar': 0.95,
    }

    carrito = [
        Articulo('Camiseta', 'ropa', 20.0),
        Articulo('Auriculares', 'electronica', 50.0),
        Articulo('Taza', 'hogar', 10.0),
    ]

    total = procesar_carrito(carrito, descuentos)
    print(f"Total con descuentos: {total} €")
