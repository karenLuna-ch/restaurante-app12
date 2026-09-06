class Venta:
    def __init__(self, id_venta: int, cedula_usuario: str, codigo_producto: str, cantidad: int, total: float):
        self.id_venta = id_venta
        self.cedula_usuario = cedula_usuario
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.total = total

    def to_dict(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "cedula_usuario": self.cedula_usuario,
            "codigo_producto": self.codigo_producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @staticmethod
    def from_dict(data: dict):
        return Venta(
            id_venta=data["id_venta"],
            cedula_usuario=data["cedula_usuario"],
            codigo_producto=data["codigo_producto"],
            cantidad=data["cantidad"],
            total=data["total"]
        )
    