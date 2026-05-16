class CuentaBancaria:
    def _init_(self):
        self.__saldo = 0.0

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero")
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro")
        self.__saldo -= monto

    def obtener_saldo(self) -> float:
        return self.__saldo