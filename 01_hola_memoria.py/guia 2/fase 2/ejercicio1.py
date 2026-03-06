def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    descuento_salud_pension: float = salario_base * 0.08
    salario_final: float = salario_base - descuento_salud_pension + bonificacion
    return salario_final

salario1: float = calcular_salario_neto(1000000.0)           
salario2: float = calcular_salario_neto(1000000.0, 200000.0)  

print("Salario neto 1:", salario1)
print("Salario neto 2:", salario2)
