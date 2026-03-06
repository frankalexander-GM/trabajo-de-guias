print("--- Filtro de Seguridad ---")
edadesacceso = [15, 22, 17, 30, 14]
for edad in edadesacceso:
    if edad >= 18:
        print(f"Persona de {edad} años: Acceso PERMITIDO.")
    else:
        print(f"Persona de {edad} años: Bloqueada.")
