class Cuenta:
    def __init__(self, numero: str, titular: str, saldo: float):
        self.numero = numero
        self.titular = titular
        self.saldo = float(saldo)

    def __repr__(self):
        return f"Cuenta(numero={self.numero!r}, titular={self.titular!r}, saldo={self.saldo:.2f})"


def ejecutar_transferencia(origen_num, destino_num, monto, cuentas, historial):
    if origen_num not in cuentas:
        return f"Error: la cuenta origen {origen_num} no existe."

    if destino_num not in cuentas:
        return f"Error: la cuenta destino {destino_num} no existe."

    if monto <= 0:
        return "Error: el monto debe ser mayor que cero."

    origen = cuentas[origen_num]
    destino = cuentas[destino_num]

    if origen.saldo < monto:
        return f"Error: saldo insuficiente en la cuenta {origen_num}."

    origen.saldo -= monto
    destino.saldo += monto

    registro = f"Transferencia {monto:.2f}€ de {origen_num} a {destino_num}"
    historial.append(registro)
    return f"Transferencia realizada: {registro}."


if __name__ == '__main__':
    cuentas = {
        '001': Cuenta('001', 'Ana Pérez', 1500.0),
        '002': Cuenta('002', 'Luis Gómez', 800.0),
        '003': Cuenta('003', 'María Ruiz', 2500.0),
    }

    historial = []

    print(ejecutar_transferencia('001', '002', 300.0, cuentas, historial))
    print(ejecutar_transferencia('002', '003', 1000.0, cuentas, historial))
    print(ejecutar_transferencia('003', '001', 500.0, cuentas, historial))
    print(ejecutar_transferencia('004', '001', 100.0, cuentas, historial))

    print('\nSaldos finales:')
    for cuenta in cuentas.values():
        print(f"{cuenta.numero} - {cuenta.titular}: {cuenta.saldo:.2f}€")

    print('\nHistorial de transferencias:')
    for evento in historial:
        print(evento)
