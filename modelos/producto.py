
class Producto:
    """Clase base que representa las propiedades comunes de un producto."""
    
    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        self.__precio = 0.0  # Atributo privado encapsulado
        self.cambiar_precio(precio)  # Valida el precio al construir el objeto
        self.disponible = disponible

    
    def obtener_precio(self) -> float:
        return self.__precio

    
    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio <= 0:
            raise ValueError("El precio no puede ser negativo ni igual a cero.")
        self.__precio = nuevo_precio

    def mostrar_informacion(self) -> str:
        """Método base que será sobrescrito en las clases hijas."""
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"