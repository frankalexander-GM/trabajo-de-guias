tiene_licencia = input("¿Tienes licencia de conducir? (si/no): ")
esta_sobrio = input("¿Has bebido alcohol hoy? (si/no): ")
if tiene_licencia == "si" and esta_sobrio == "no":
    print("Puedes conducir el vehículo.")
else:
    print("Entregue las llaves. No puede conducir.")