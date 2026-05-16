class PagoTarjeta:
    def procesarpago(self, monto):
        print(f"Procesando pago con tarjeta de {monto}")

class PagoCriptomoneda:
    def procesarpago(self, monto):
        print(f"Procesando pago con criptomoneda de {monto}")

def ejecutartransaccion(objeto_pago, monto):
    objeto_pago.procesar_pago(monto)

tarjeta = PagoTarjeta()
cripto = PagoCriptomoneda()

ejecutartransaccion(tarjeta, 100)
ejecutartransaccion(cripto, 0.05)