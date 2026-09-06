from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        # Instancia del servicio de archivos
        self.archivo_servicio = ArchivoServicio()
        
        # Colecciones principales (Listas para persistencia en JSON)
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        
        # Estructuras auxiliares (Índices para búsquedas O(1))
        self._indice_productos_codigo: dict[str, Producto] = {}
        self._indice_usuarios_cedula: dict[str, Usuario] = {}
        self._indice_ventas_usuario: dict[str, list[Venta]] = {}
        self._codigos_existentes: set[str] = set()

        # Cargar datos iniciales desde JSON
        self.cargar_datos()

    def _reconstruir_indices(self):
        """Construye los diccionarios y conjuntos auxiliares a partir de las listas principales."""
        self._indice_productos_codigo = {p.codigo: p for p in self._productos}
        self._codigos_existentes = {p.codigo for p in self._productos}
        self._indice_usuarios_cedula = {u.cedula: u for u in self._usuarios}
        
        self._indice_ventas_usuario = {}
        for v in self._ventas:
            cedula = v.cedula_usuario
            if cedula not in self._indice_ventas_usuario:
                self._indice_ventas_usuario[cedula] = []
            self._indice_ventas_usuario[cedula].append(v)

    def cargar_datos(self):
        """Carga datos desde JSON y reconstruye los índices auxiliares."""
        self._productos = self.archivo_servicio.cargar_productos()
        self._usuarios = self.archivo_servicio.cargar_usuarios()
        self._ventas = self.archivo_servicio.cargar_ventas()
        self._reconstruir_indices()

    def guardar_datos(self):
        """Guarda las listas principales en sus respectivos archivos JSON."""
        self.archivo_servicio.guardar_productos(self._productos)
        self.archivo_servicio.guardar_usuarios(self._usuarios)
        self.archivo_servicio.guardar_ventas(self._ventas)

    # --- BÚSQUEDAS OPTIMIZADAS CON DICCIONARIOS O(1) ---

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._indice_productos_codigo.get(codigo)

    def buscar_usuario(self, cedula: str) -> Usuario | None:
        return self._indice_usuarios_cedula.get(cedula)

    def consultar_ventas_usuario(self, cedula: str) -> list[Venta]:
        return self._indice_ventas_usuario.get(cedula, [])

    # --- REGISTRO Y OPERACIONES ---

    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        # Validación de unicidad directa con el conjunto
        if codigo in self._codigos_existentes:
            return False

        nuevo = Producto(codigo, nombre, precio, stock)
        self._productos.append(nuevo)
        
        # Actualización de índices
        self._indice_productos_codigo[codigo] = nuevo
        self._codigos_existentes.add(codigo)
        
        self.guardar_datos()
        return True

    def registrar_usuario(self, cedula: str, nombre: str, correo: str) -> bool:
        if cedula in self._indice_usuarios_cedula:
            return False

        nuevo = Usuario(cedula, nombre, correo)
        self._usuarios.append(nuevo)
        self._indice_usuarios_cedula[cedula] = nuevo
        
        self.guardar_datos()
        return True

    def registrar_venta(self, cedula_usuario: str, codigo_producto: str, cantidad: int) -> tuple[bool, str]:
        usuario = self.buscar_usuario(cedula_usuario)
        if not usuario:
            return False, "Usuario no encontrado."

        producto = self.buscar_producto(codigo_producto)
        if not producto:
            return False, "Producto no encontrado."

        if producto.stock < cantidad:
            return False, f"Stock insuficiente. Disponible: {producto.stock}"

        # Actualizar stock y total
        producto.stock -= cantidad
        total = producto.precio * cantidad

        nueva_venta = Venta(
            id_venta=len(self._ventas) + 1,
            cedula_usuario=cedula_usuario,
            codigo_producto=codigo_producto,
            cantidad=cantidad,
            total=total
        )
        
        self._ventas.append(nueva_venta)

        # Actualizar índice de ventas
        if cedula_usuario not in self._indice_ventas_usuario:
            self._indice_ventas_usuario[cedula_usuario] = []
        self._indice_ventas_usuario[cedula_usuario].append(nueva_venta)

        self.guardar_datos()
        return True, "Venta registrada exitosamente."