from modelos.producto import Producto

class Bebida(Producto):
    
    
    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponible: bool = True):
        # Invocamos al constructor de la clase padre
        super().__init__(nombre, precio, disponible)
        # Atributo específico (en mililitros)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self) -> str:
        
        estado = "Disponible" if self.disponible else "Agotado"
        return (f"[BEBIDA]   {self.nombre}\n"
                f"  - Precio: ${self.obtener_precio():.2f}\n"
                f"  - Volumen: {self.volumen_ml} ml\n"
                f"  - Estado: {estado}")