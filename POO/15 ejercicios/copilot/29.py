class Paquete:
    def __init__(self, id: str, volumen: float, fragil: bool):
        self.id = id
        self.volumen = float(volumen)
        self.fragil = fragil

    def __repr__(self):
        return f"Paquete(id={self.id!r}, volumen={self.volumen}, fragil={self.fragil})"


def cargar_camiones(paquetes, volumen_maximo):
    camiones = []
    fragiles_por_camion = []
    volumen_actual = 0.0
    camion_actual = []

    for paquete in paquetes:
        if volumen_actual + paquete.volumen > volumen_maximo:
            camiones.append(camion_actual)
            fragiles_por_camion.append([p.id for p in camion_actual if p.fragil])
            camion_actual = []
            volumen_actual = 0.0

        camion_actual.append(paquete)
        volumen_actual += paquete.volumen

    if camion_actual:
        camiones.append(camion_actual)
        fragiles_por_camion.append([p.id for p in camion_actual if p.fragil])

    return camiones, fragiles_por_camion


if __name__ == '__main__':
    paquetes = [
        Paquete('A1', 2.5, False),
        Paquete('B2', 1.2, True),
        Paquete('C3', 3.0, False),
        Paquete('D4', 0.8, True),
        Paquete('E5', 2.1, False),
    ]

    camiones, fragiles = cargar_camiones(paquetes, volumen_maximo=5.0)

    for idx, camion in enumerate(camiones, start=1):
        ids = [p.id for p in camion]
        print(f"Camión {idx}: {ids} - frágiles: {fragiles[idx-1]}")
