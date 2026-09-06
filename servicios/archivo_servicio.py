import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    def __init__(self):
        self.ruta_datos = os.path.join(os.path.dirname(__file__), "..", "datos")

    def _leer_json(self, nombre_archivo: str) -> list:
        filepath = os.path.join(self.ruta_datos, nombre_archivo)
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _guardar_json(self, nombre_archivo: str, datos: list):
        filepath = os.path.join(self.ruta_datos, nombre_archivo)
        os.makedirs(self.ruta_datos, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_productos(self) -> list[Producto]:
        return [Producto.from_dict(p) for p in self._leer_json("productos.json")]

    def guardar_productos(self, productos: list[Producto]):
        self._guardar_json("productos.json", [p.to_dict() for p in productos])

    def cargar_usuarios(self) -> list[Usuario]:
        return [Usuario.from_dict(u) for u in self._leer_json("usuarios.json")]

    def guardar_usuarios(self, usuarios: list[Usuario]):
        self._guardar_json("usuarios.json", [u.to_dict() for u in usuarios])

    def cargar_ventas(self) -> list[Venta]:
        return [Venta.from_dict(v) for v in self._leer_json("ventas.json")]

    def guardar_ventas(self, ventas: list[Venta]):
        self._guardar_json("ventas.json", [v.to_dict() for v in ventas])
        