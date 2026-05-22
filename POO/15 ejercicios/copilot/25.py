class Candidato:
    def __init__(self, nombre: str, partido: str):
        self.nombre = nombre
        self.partido = partido

    def __repr__(self):
        return f"Candidato(nombre={self.nombre!r}, partido={self.partido!r})"


def escrutar_votos(votos):
    conteo = {}
    for voto in votos:
        if voto in conteo:
            conteo[voto] += 1
        else:
            conteo[voto] = 1

    ganador = None
    max_votos = 0
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato

    return ganador


if __name__ == '__main__':
    candidatos = (
        Candidato('Ana', 'Verde'),
        Candidato('Luis', 'Azul'),
        Candidato('Marta', 'Rojo'),
    )

    votos = (
        'Ana', 'Luis', 'Ana', 'Marta', 'Ana', 'Luis', 'Marta', 'Luis', 'Luis'
    )

    ganador = escrutar_votos(votos)
    print(f"Ganador: {ganador}")
