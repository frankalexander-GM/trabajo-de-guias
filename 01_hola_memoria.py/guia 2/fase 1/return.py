def calcular_iva(precio_base: float) -> float:
    iva: float = precio_base * 0.19
    precio_final: float = precio_base + iva
    return precio_final


factura1: float = calcular_iva(10000.0)
factura2: float = calcular_iva(50000.0)

print("Total factura 1:", factura1)
print("Total factura 2:", factura2)