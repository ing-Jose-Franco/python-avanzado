class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self) -> str:
        return f"{self.marca} {self.modelo}"


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def descripcion(self):
        base = super().descripcion()
        return f"{base} - Puertas: {self.numero_puertas}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_manillar):
        super().__init__(marca, modelo)
        self.tipo_manillar = tipo_manillar

    def descripcion(self):
        base = super().descripcion()
        return f"{base} - Manillar: {self.tipo_manillar}"


auto = Coche("Ford", "Mustang", 2)
moto = Motocicleta("Honda", "CBR", "Deportivo")

print(auto.descripcion())
print(moto.descripcion())