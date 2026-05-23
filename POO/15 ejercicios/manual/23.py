class Mascota:
    def __init__(self, nombre, especie, urgencia):
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(especie, str) or not especie:
            raise ValueError("La especie debe ser una cadena no vacía.")
        if not isinstance(urgencia, int) or urgencia < 1 or urgencia > 5:
            raise ValueError("La urgencia debe ser un entero entre 1 y 5.")

        self.nombre = nombre
        self.especie = especie
        self.urgencia = urgencia

    def __repr__(self):
        return f"Mascota(nombre={self.nombre!r}, especie={self.especie!r}, urgencia={self.urgencia})"


def asignar_consultorio(pacientes, consultorios):
    asignaciones = []
    consultorios_disponibles = set(consultorios)

    for mascota in sorted(pacientes, key=lambda m: m.urgencia, reverse=True):
        if not consultorios_disponibles:
            asignaciones.append((mascota, None))
            continue

        consultorio = consultorios_disponibles.pop()
        asignaciones.append((mascota, consultorio))

    return asignaciones


if __name__ == "__main__":
    pacientes = [
        Mascota("Luna", "Perro", 5),
        Mascota("Milo", "Gato", 2),
        Mascota("Nala", "Conejo", 4),
        Mascota("Coco", "Ave", 3),
    ]
    consultorios = ["A", "B", "C"]

    asignados = asignar_consultorio(pacientes, consultorios)
    for mascota, consultorio in asignados:
        if consultorio is None:
            print(f"{mascota.nombre} ({mascota.especie}) debe esperar: sin consultorio disponible.")
        else:
            print(f"{mascota.nombre} ({mascota.especie}) -> Consultorio {consultorio}")
