def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

edad_usuario: int = 17

if es_mayor_de_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
