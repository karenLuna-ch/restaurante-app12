from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self._productos: list[Producto] = ArchivoServicio.cargar_productos()
        self._usuarios: list[Usuario] = ArchivoServicio.cargar_usuarios()
        self._ventas: list[Venta] = ArchivoServicio.cargar_ventas()

    # --- PRODUCTOS ---
    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        if self.buscar_producto(codigo) is not None:
            return False
        nuevo = Producto(codigo, nombre, precio, stock)
        self._productos.append(nuevo)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def obtener_productos(self) -> list[Producto]:
        return self._productos

    # --- USUARIOS ---
    def registrar_usuario(self, identificacion: str, nombre: str, correo: str) -> bool:
        if self.buscar_usuario(identificacion) is not None:
            return False
        nuevo = Usuario(identificacion, nombre, correo)
        self._usuarios.append(nuevo)
        ArchivoServicio.guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def obtener_usuarios(self) -> list[Usuario]:
        return self._usuarios

    # --- OPERACIÓN DE VENTA Y CONSULTAS ---
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        # Descontar stock y agregar la venta
        producto.vender(cantidad)
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)

        # Guardar en disco ambas colecciones afectadas
        ArchivoServicio.guardar_productos(self._productos)
        ArchivoServicio.guardar_ventas(self._ventas)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[tuple[Venta, Producto]]:
        ventas_usuario: list[tuple[Venta, Producto]] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                prod = self.buscar_producto(venta.producto_codigo)
                if prod:
                    ventas_usuario.append((venta, prod))
        return ventas_usuario