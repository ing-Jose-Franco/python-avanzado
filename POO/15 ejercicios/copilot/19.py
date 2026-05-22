class Empleado:
    def __init__(self, nombre: str, bruto: float, contrato: str):
        self.nombre = nombre
        self.bruto = float(bruto)
        self.contrato = contrato.lower()

    def __repr__(self):
        return f"Empleado(nombre={self.nombre!r}, bruto={self.bruto}, contrato={self.contrato!r})"


def liquidar_nomina(empleados, impuestos):
    resultados = []
    for empleado in empleados:
        deducciones = {nombre: empleado.bruto * tasa for nombre, tasa in impuestos.items()}
        total_deducciones = sum(deducciones.values())
        neto = empleado.bruto - total_deducciones

        bono = 0.0
        if empleado.contrato == 'indefinido':
            bono += 150.0
        if empleado.bruto >= 3000:
            bono += 200.0

        neto += bono

        resultados.append({
            'nombre': empleado.nombre,
            'bruto': empleado.bruto,
            'deducciones': deducciones,
            'bono': bono,
            'neto': round(neto, 2),
        })

    return resultados


if __name__ == '__main__':
    impuestos = {
        'IRPF': 0.15,
        'Seguridad Social': 0.06,
        'Fondo de Garantía': 0.01,
    }

    plantilla = [
        Empleado('Ana', 2800, 'indefinido'),
        Empleado('Luis', 2200, 'temporal'),
        Empleado('María', 3300, 'indefinido'),
        Empleado('Pablo', 1800, 'temporal'),
    ]

    nomina = liquidar_nomina(plantilla, impuestos)
    for empleado in nomina:
        print(f"{empleado['nombre']}: bruto={empleado['bruto']} €, "
              f"deducciones={sum(empleado['deducciones'].values()):.2f} €, "
              f"bono={empleado['bono']:.2f} €, neto={empleado['neto']:.2f} €")
