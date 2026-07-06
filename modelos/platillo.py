from modelos.producto import Producto

class Platillo(Producto):
    
    
    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, disponible: bool = True):
        # Invocamos al constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo específico (en minutos)
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self) -> str:
        
        estado = "Disponible" if self.disponible else "Agotado"
        return (f"[PLATILLO] {self.nombre}\n"
                f"  - Precio: ${self.obtener_precio():.2f}\n"
                f"  - Tiempo de cocina: {self.tiempo_preparacion} minutos\n"
                f"  - Estado: {estado}")
