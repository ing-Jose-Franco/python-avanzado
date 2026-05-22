class RegistroClima:
    def __init__(self, fecha: str, temperaturas: list):
        self.fecha = fecha
        self.temperaturas = [float(t) for t in temperaturas]

    def __repr__(self):
        return f"RegistroClima(fecha={self.fecha!r}, temperaturas={self.temperaturas})"


def detectar_anomalias(registros, umbral=5.0):
    anomalias = set()

    for registro in registros:
        if not registro.temperaturas:
            continue

        total = 0.0
        for temp in registro.temperaturas:
            total += temp

        media = total / len(registro.temperaturas)

        for temp in registro.temperaturas:
            if abs(temp - media) > umbral:
                anomalias.add(registro.fecha)
                break

    return anomalias


if __name__ == '__main__':
    registros = [
        RegistroClima('2026-05-20', [18, 22, 21, 27]),
        RegistroClima('2026-05-21', [20, 19, 21, 20]),
        RegistroClima('2026-05-22', [15, 30, 14, 16]),
    ]

    resultado = detectar_anomalias(registros)
    print('Fechas con anomalías:', resultado)
