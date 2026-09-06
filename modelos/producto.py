class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data: dict):
        return Producto(
            codigo=data["codigo"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"]
        )
    