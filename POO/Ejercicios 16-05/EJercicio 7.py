print("Ejercicio de integracion moderada: Nomina empresarial")
print("\nSistema automatizado de pagos")

class Empleado:
    def __init__(self, nombre, salario_base):
        self._nombre = nombre
        self._salario_base = salario_base

    def get_nombre(self):
        return self._nombre

    def calcular_pago(self):
        return self._salario_base


class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, bono_proyectos):
        super().__init__(nombre, salario_base)
        self._bono_proyectos = bono_proyectos

    def calcular_pago(self):
        return self._salario_base + self._bono_proyectos


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comisiones):
        super().__init__(nombre, salario_base)
        self._comisiones = comisiones  

    def calcular_pago(self):
        return self._salario_base + self._comisiones


def procesar_nomina(lista_empleados, umbral_pago):
    print("Procesando la nómina empresarial...\n")
    

    for empleado_per in lista_empleados:
       
        pago_final = empleado_per.calcular_pago()
        
        if pago_final < umbral_pago:
            bono = pago_final * 0.10
            pago_final += bono
            print(f"{empleado_per.get_nombre()}: ${pago_final} (Incluye bono del 10% ({bono}$)")
        else:
            print(f"{empleado_per.get_nombre()}: ${pago_final}")

personal = [
    Desarrollador("Jose Franco", 1500, 300),  
    Vendedor("Alan Hernandez", 600, 150),      
    Desarrollador("Alejandro Cisnero", 800, 0),        
]
procesar_nomina(personal, umbral_pago=800)
