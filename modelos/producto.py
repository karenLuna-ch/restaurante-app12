class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self._codigo = codigo
        self._nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = valor

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if cantidad > self._stock:
            raise ValueError("Stock insuficiente para realizar la venta.")
        self.stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self._codigo,
            "nombre": self._nombre,
            "precio": self._precio,
            "stock": self._stock
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Producto':
        try:
            return Producto(
                codigo=str(datos["codigo"]),
                nombre=str(datos["nombre"]),
                precio=float(datos["precio"]),
                stock=int(datos["stock"])
            )
        except (KeyError, ValueError) as e:
            raise KeyError(f"Estructura de producto inválida en JSON: {e}")
