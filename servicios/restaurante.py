from typing import List, Set, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    

    def __init__(self) -> None:
      
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto:
            self._productos.remove(producto)
            return True
        return False

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_categorias_unicas(self) -> Set[str]:
        # SET: Obtiene categorías sin elementos duplicados
        return {p.categoria.title() for p in self._productos}

    # --- Métodos de Usuarios ---

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios