# CLASE PADRE
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente.")
            self.stock -= cantidad
            print(f"Venta exitosa. Stock restante de {self.nombre}: {self.stock}")
        except ValueError as e:
            print(f"ERROR: {e}")

class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento: int = dias_vencimiento

leche = ProductoPerecedero("Leche", 3500.0, 10, 5)
arroz = Producto("Arroz", 2500.0, 20)

leche.vender(3)
arroz.vender(25)
arroz.vender(5)

print(f"Días de vencimiento de la leche: {leche.dias_vencimiento}")
