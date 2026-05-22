class ProductoCarrito:
    def __init__(self, nombre: str, peso: float, precio: float):
        self.nombre = nombre
        self.peso = float(peso)
        self.precio = float(precio)

    def __repr__(self):
        return f"ProductoCarrito(nombre={self.nombre!r}, peso={self.peso}, precio={self.precio})"


def checkout_final(productos, tarifas_envio):
    total_precio = 0.0
    total_peso = 0.0

    for producto in productos:
        total_precio += producto.precio
        total_peso += producto.peso

    if total_precio >= 100.0:
        envio = 0.0
    else:
        if total_peso <= 5.0:
            envio = tarifas_envio['ligero']
        elif total_peso <= 15.0:
            envio = tarifas_envio['medio']
        else:
            envio = tarifas_envio['pesado']

    return {
        'total_precio': round(total_precio, 2),
        'total_peso': round(total_peso, 2),
        'envio': round(envio, 2),
        'total_final': round(total_precio + envio, 2),
    }


if __name__ == '__main__':
    tarifas_envio = {
        'ligero': 5.0,
        'medio': 10.0,
        'pesado': 20.0,
    }

    carrito = [
        ProductoCarrito('Camiseta', 0.5, 25.0),
        ProductoCarrito('Zapatos', 1.2, 50.0),
        ProductoCarrito('Libro', 0.8, 20.0),
    ]

    resultado = checkout_final(carrito, tarifas_envio)
    print(f"Total precio: {resultado['total_precio']}€")
    print(f"Total peso: {resultado['total_peso']}kg")
    print(f"Costo envío: {resultado['envio']}€")
    print(f"Total final: {resultado['total_final']}€")
