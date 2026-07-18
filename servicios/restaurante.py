from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # Registrar producto o bebida
    def registrar_producto(self, producto: Producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                raise ValueError("Ya existe un producto con ese código.")

        self.productos.append(producto)

    # Registrar cliente
    def registrar_cliente(self, cliente: Cliente):
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                raise ValueError("Ya existe un cliente con esa identificación.")

        self.clientes.append(cliente)

    # Listar productos
    def listar_productos(self):
        if not self.productos:
            print("\nNo hay productos registrados.")
            return

        print("\n===== PRODUCTOS =====")
        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 40)

    # Listar clientes
    def listar_clientes(self):
        if not self.clientes:
            print("\nNo hay clientes registrados.")
            return

        print("\n===== CLIENTES =====")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
            print("-" * 40)