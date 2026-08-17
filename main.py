import sys
from typing import Tuple, Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)

def ejecutar_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    codigo = input("Ingrese código único: ").strip()
    nombre = input("Ingrese nombre del producto: ").strip()
    categoria = input("Ingrese categoría: ").strip()
    try:
        precio = float(input("Ingrese precio ($): "))
        if precio <= 0:
            print("Error: El precio debe ser un valor positivo.")
            return
    except ValueError:
        print("Error: Ingrese un número válido para el precio.")
        return

    if servicio.registrar_producto(Producto(codigo, nombre, categoria, precio)):
        print("✓ Producto registrado exitosamente.")
    else:
        print("× Error: El código ya se encuentra registrado.")

def ejecutar_buscar_producto(servicio: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese código a buscar: ").strip()
    producto = servicio.buscar_producto_por_codigo(codigo)
    if producto:
        print(f"Encontrado: {producto}")
    else:
        print("× Producto no encontrado.")

def ejecutar_actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese código del producto a actualizar: ").strip()
    if not servicio.buscar_producto_por_codigo(codigo):
        print("× Error: El producto no existe.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()
    try:
        precio = float(input("Nuevo precio ($): "))
        if precio <= 0:
            print("Error: El precio debe ser un valor positivo.")
            return
    except ValueError:
        print("Error: Precio inválido.")
        return

    if servicio.actualizar_producto(codigo, nombre, categoria, precio):
        print("✓ Producto actualizado exitosamente.")

def ejecutar_eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        print("✓ Producto eliminado con éxito.")
    else:
        print("× Error: El producto no existe.")

def ejecutar_listar_productos(servicio: Restaurante) -> None:
    print("\n--- Listado de Productos ---")
    productos = servicio.obtener_productos()
    if not productos:
        print("No hay productos registrados.")
    else:
        for p in productos:
            print(f"  • {p}")

def ejecutar_registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    identificacion = input("Identificación/Cédula: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electrónico: ").strip()

    if not identificacion or not nombre or not correo:
        print("Error: Todos los campos son obligatorios.")
        return

    if servicio.registrar_usuario(Usuario(identificacion, nombre, correo)):
        print("✓ Usuario registrado exitosamente.")
    else:
        print("× Error: La identificación ya se encuentra registrada.")

def ejecutar_listar_usuarios(servicio: Restaurante) -> None:
    print("\n--- Listado de Usuarios ---")
    usuarios = servicio.obtener_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            print(f"  • {u}")

def ejecutar_mostrar_categorias(servicio: Restaurante) -> None:
    print("\n--- Categorías Únicas ---")
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("No existen categorías registradas.")
    else:
        for c in categorias:
            print(f"  - {c}")

def ejecutar_salir(servicio: Restaurante) -> None:
    print("\nSaliendo del sistema...")
    sys.exit(0)

def main() -> None:
    restaurante = Restaurante()

    
    menu_despachador: Dict[str, Callable[[Restaurante], None]] = {
        "1": ejecutar_registrar_producto,
        "2": ejecutar_buscar_producto,
        "3": ejecutar_actualizar_producto,
        "4": ejecutar_eliminar_producto,
        "5": ejecutar_listar_productos,
        "6": ejecutar_registrar_usuario,
        "7": ejecutar_listar_usuarios,
        "8": ejecutar_mostrar_categorias,
        "9": ejecutar_salir
    }

    while True:
        print("\n========================================")
        print("        SISTEMA DE RESTAURANTE        ")
        print("========================================")
        for opcion in OPCIONES_MENU:
            print(opcion)
        print("----------------------------------------")

        eleccion = input("Seleccione una opción (1-9): ").strip()
        accion = menu_despachador.get(eleccion)
        if accion:
            accion(restaurante)
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()