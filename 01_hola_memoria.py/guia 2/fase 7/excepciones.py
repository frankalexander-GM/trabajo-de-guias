class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000.0

    def solicitar_retiro(self) -> None:
        print("--- Bienvenido al Cajero ---")
        try:
            monto = float(input("Ingrese la cantidad a retirar: "))

            if monto <= 0:
                raise ValueError("No puede retirar cero o menos.")

            self.efectivo_disponible -= monto
            print(f"Retiro exitoso. Quedan {self.efectivo_disponible} en el cajero.")

        except ValueError as e:
            print(f"ERROR: Usted ingresó caracteres inválidos. {e}")

        except Exception as e:
            print(f"ERROR CRÍTICO DESCONOCIDO. Detalles: {e}")

        finally:
            print("Expulsando tarjeta... Gracias por usar nuestra red.")


mi_cajero = CajeroAutomatico()
mi_cajero.solicitar_retiro()