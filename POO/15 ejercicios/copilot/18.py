class Vuelo:
    def __init__(self, numero: str, asientos: set):
        self.numero = numero
        self.asientos = set(asientos)

    def __repr__(self):
        return f"Vuelo(numero={self.numero!r}, asientos={sorted(self.asientos)})"


def reservar_asiento(vuelo, solicitudes):
    tarifa_base = 100.0
    total = 0.0
    for asiento, clase in solicitudes:
        if asiento in vuelo.asientos:
            vuelo.asientos.remove(asiento)
            if clase == 'negocios':
                total += tarifa_base * 1.5
            else:
                total += tarifa_base
        else:
            print(f"Asiento {asiento} no disponible.")
    return round(total, 2)


if __name__ == '__main__':
    vuelo = Vuelo('AB123', {'1A', '1B', '2A', '2B', '3A', '3B'})
    solicitudes = (
        ('1A', 'negocios'),
        ('2B', 'economica'),
        ('3A', 'economica'),
    )

    total = reservar_asiento(vuelo, solicitudes)
    print(f"Total tarifa: {total} €")
    print(f"Asientos restantes: {vuelo.asientos}")
