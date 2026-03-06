totalahorrado = 0
for mes in range(1, 4):
    consignacion = int(input(f"¿Cuánto dinero vas a ahorrar en el mes {mes}? "))
    totalahorrado = totalahorrado + consignacion
print(f"¡Ahorro completado! Tienes un total de {totalahorrado}")
