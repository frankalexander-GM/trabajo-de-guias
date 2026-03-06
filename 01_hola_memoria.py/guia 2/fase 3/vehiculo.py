class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.anio: int = anio


carro1 = Vehiculo("Toyota", "Corolla", 2020)
carro2 = Vehiculo("Chevrolet", "Onix", 2023)

print(f"Vehículo 1: {carro1.marca} {carro1.modelo} ({carro1.anio})")
print(f"Vehículo 2: {carro2.marca} {carro2.modelo} ({carro2.anio})")
