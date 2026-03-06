edad_usuario = int(input("Por favor, ingresa tu edad en números: "))
print("Evaluando permisos de acceso...")
if edad_usuario >= 18:
    print("Acceso concedido: Eres mayor de edad.")
elif edad_usuario >= 13:
    print("Acceso restringido: Eres adolescente, necesitas permiso de un tutor")
else:
    print("Acceso denegado: Eres menor de edad.")
print("Gracias por usar el sistema.")
