
from typing import Dict, Any


class Producto:
    
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @property
    def id_producto(self) -> int:
        return self._id_producto

    @id_producto.setter
    def id_producto(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del producto debe ser un entero positivo.")
        self._id_producto = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")
        self._precio = float(valor)

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    def a_diccionario(self) -> Dict[str, Any]:
       
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @classmethod
    def desde_diccionario(cls, datos: Dict[str, Any]) -> "Producto":
        
        claves_requeridas = {"id_producto", "nombre", "precio", "categoria"}
        claves_faltantes = claves_requeridas - datos.keys()
        
        if claves_faltantes:
            raise KeyError(f"Registro incompleto. Faltan las claves: {', '.join(claves_faltantes)}")

        return cls(
            id_producto=int(datos["id_producto"]),
            nombre=str(datos["nombre"]),
            precio=float(datos["precio"]),
            categoria=str(datos["categoria"])
        )

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria}"