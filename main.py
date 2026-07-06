from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar_sistema():
   
    mi_restaurante = Restaurante("El Buen Paladar")
    
    print("=== REGISTRANDO PRODUCTOS ===")
    
    
    platillo1 = Platillo(nombre="Lomo Saltado", precio=15.50, tiempo_preparacion=20)
    platillo2 = Platillo(nombre="Ceviche Clásico", precio=18.00, tiempo_preparacion=15)
    
    
    bebida1 = Bebida(nombre="Chicha Morada (Jarra)", precio=8.00, volumen_ml=1000)
    bebida2 = Bebida(nombre="Pisco Sour", precio=12.00, volumen_ml=250, disponible=False)
    
    
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)
    
    
    print("\n=== PRUEBA DE ENCAPSULACIÓN Y VALIDACIÓN ===")
    print(f"Precio actual de {platillo1.nombre}: ${platillo1.obtener_precio():.2f}")
    
    try:
        print("Intentando cambiar el precio a un valor inválido (-3.50)...")
        platillo1.cambiar_precio(-3.50)  # Debería lanzar una excepción
    except ValueError as e:
        print(f"Validación exitosa: {e}")
        
    print("Aplicando un cambio de precio válido ($16.90)...")
    platillo1.cambiar_precio(16.90)
    print(f"Nuevo precio modificado: ${platillo1.obtener_precio():.2f}")

    
    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    ejecutar_sistema()