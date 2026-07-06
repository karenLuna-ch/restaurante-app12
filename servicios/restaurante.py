from modelos.producto import Producto

class Restaurante:
    """Clase encargada de almacenar y gestionar los productos del menú."""
    
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento = nombre_establecimiento
        
        self.__menu = []

    def agregar_producto(self, producto: Producto):
        """Almacena un objeto Producto (o sus herederos) en la lista."""
        self.__menu.append(producto)
        print(f"  + Registrado con éxito en sistema: {producto.nombre}")

    def mostrar_menu_completo(self):
        """Imprime la lista aplicando polimorfismo dinámico."""
        print(f"\n=========================================")
        print(f"      MENÚ GENERAL - {self.nombre_establecimiento.upper()}      ")
        print(f"=========================================")
        
        if not self.__menu:
            print("El menú se encuentra vacío.")
            return

        for producto in self.__menu:
            
            print(producto.mostrar_informacion())
            print("-" * 41)