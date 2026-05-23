class Estudiante:
    def __init__(self, matricula, nombre, notas):
        if not isinstance(matricula, str) or not matricula:
            raise ValueError("La matrícula debe ser una cadena no vacía.")
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(notas, list) or not all(isinstance(n, (int, float)) for n in notas):
            raise ValueError("Las notas deben ser una lista de números.")

        self.matricula = matricula
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0


def generar_actas(estudiantes, puntaje_aprobado=60):
    actas = []
    for estudiante in estudiantes:
        if not isinstance(estudiante, Estudiante):
            continue

        promedio = estudiante.promedio()
        if promedio >= puntaje_aprobado:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        actas.append({
            "matricula": estudiante.matricula,
            "nombre": estudiante.nombre,
            "promedio": promedio,
            "estado": estado,
        })

    return actas


if __name__ == "__main__":
    estudiantes = [
        Estudiante("2024001", "Ana Pérez", [75, 82, 68]),
        Estudiante("2024002", "Carlos Díaz", [55, 60, 58]),
        Estudiante("2024003", "María López", [90, 88, 94]),
    ]

    actas = generar_actas(estudiantes, puntaje_aprobado=60)
    for acta in actas:
        print(f"{acta['matricula']} - {acta['nombre']}: {acta['promedio']:.1f} -> {acta['estado']}")
