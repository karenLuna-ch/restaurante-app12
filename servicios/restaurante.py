from typing import List, Optional, Dict, Any
from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # --- MÉTODOS DE PRODUCTOS ---

    def obtener_todos_los_productos(self) -> List[Producto]:
       
        return self._productos

    def obtener_productos_como_diccionario(self) -> List[Dict[str, Any]]:
        
        return [producto.a_diccionario() for producto in self._productos]

    def cargar_desde_diccionarios(self, lista_datos: List[Dict[str, Any]]) -> None:
        
        self._productos.clear()
        registros_omitidos = 0

        for idx, datos in enumerate(lista_datos, start=1):
            try:
                producto = Producto.desde_diccionario(datos)
                self._productos.append(producto)
            except (KeyError, ValueError) as err:
                registros_omitidos += 1
                print(f" -> Registro #{idx} omitido por datos inválidos: {err}")

        if registros_omitidos > 0:
            print(f" -> Se cargaron {len(self._productos)} productos ({registros_omitidos} omitidos por errores).")

    def registrar_producto(self, producto: Producto) -> bool:
        
        if self.buscar_producto_por_id(producto.id_producto) is not None:
            raise ValueError(f"Ya existe un producto registrado con el ID {producto.id_producto}.")
        self._productos.append(producto)
        return True

    def buscar_producto_por_id(self, id_producto: int) -> Optional[Producto]:
        
        for p in self._productos:
            if p.id_producto == id_producto:
                return p
        return None

    def actualizar_producto(self, id_producto: int, nombre: str, precio: float, categoria: str) -> bool:
        
        producto = self.buscar_producto_por_id(id_producto)
        if producto is None:
            return False

        producto.nombre = nombre
        producto.precio = precio
        producto.categoria = categoria
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        
        producto = self.buscar_producto_por_id(id_producto)
        if producto is not None:
            self._productos.remove(producto)
            return True
        return False

    # --- MÉTODOS DE USUARIOS (EN MEMORIA) ---

    def registrar_usuario(self, usuario: Usuario) -> None:
        
        self._usuarios.append(usuario)

    def obtener_todos_los_usuarios(self) -> List[Usuario]:
        
        return self._usuarios