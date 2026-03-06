
concesionario = []
for i in range(3):
    print(f"\n--- Registro de vehículo {i + 1} ---")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = int(input("Precio: "))

    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio
    }
    
    concesionario.append(vehiculo)

print("\n--- INFORME DE VEHÍCULOS REGISTRADOS ---")
for carro in concesionario:
    print(f"Vehículo registrado: Marca {carro['marca']}, Modelo {carro['modelo']}, Precio {carro['precio']}")
