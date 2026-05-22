class Evento:
    def __init__(self, nombre: str, capacidad: int):
        self.nombre = nombre
        self.capacidad = int(capacidad)
        self.invitados = {}

    def __repr__(self):
        return f"Evento(nombre={self.nombre!r}, capacidad={self.capacidad}, invitados={len(self.invitados)})"


VIPS = {'Ana', 'Luis', 'María'}


def ingresar_asistente(evento, nombre):
    if nombre in evento.invitados:
        return f"{nombre} ya está dentro del evento."

    if len(evento.invitados) < evento.capacidad:
        status = 'VIP' if nombre in VIPS else 'Regular'
        evento.invitados[nombre] = status
        return f"Ingreso aceptado: {nombre} ({status})."

    if nombre in VIPS:
        return f"Cupo lleno, pero {nombre} tiene acceso prioritario en lista de espera."

    return f"Cupo lleno. No puede ingresar {nombre}."


if __name__ == '__main__':
    evento = Evento('Fiesta VIP', 3)

    print(ingresar_asistente(evento, 'Ana'))
    print(ingresar_asistente(evento, 'Pedro'))
    print(ingresar_asistente(evento, 'Luis'))
    print(ingresar_asistente(evento, 'Marta'))
    print(ingresar_asistente(evento, 'María'))

    print('\nInvitados:')
    for nombre, estado in evento.invitados.items():
        print(f"- {nombre}: {estado}")
