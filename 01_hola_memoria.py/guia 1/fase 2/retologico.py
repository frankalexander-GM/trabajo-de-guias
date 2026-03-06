estatura_cm = float(input("Ingresa tu estatura en cm: "))
edad = int(input("Ingresa tu edad: "))

if estatura_cm > 150 and edad > 12:
    print("Acceso PERMITIDO. Puedes subir a la montaña rusa.")
else:
    print("Acceso DENEGADO. No cumples los requisitos.")
