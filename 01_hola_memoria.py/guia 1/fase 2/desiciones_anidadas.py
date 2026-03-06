print("--- Diagnóstico de Red ---")
hayinternet = input("¿El módem tiene luces encendidas? (si/no): ")
if hayinternet == "si":
    print("Paso 1: El equipo recibe energía.")
    luzroja = input("¿Alguna de las luces es color ROJO? (si/no): ")
    if luzroja == "si":
        print("Fallo detectado: Problema en la fibra óptica. Llame a soporte.")
    else:
        print("Todo normal: Su conexión está operando al 100%.")
else:
    print("Fallo crítico: Verifique que el equipo esté conectado a la corriente.")
