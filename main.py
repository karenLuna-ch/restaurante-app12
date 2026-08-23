from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

# Opciones del menú por consola
OPCIONES_MENU = (
    "\n==========================================",
    "   SISTEMA DE GESTIÓN - RESTAURANTE APP   ",
    "==========================================",
    "1. Registrar producto",
    "2. Buscar producto por ID",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar todos los productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Guardar y sincronizar cambios manualmente",
    "9. Salir del sistema"
)


def sincronizar_datos(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Extrae los diccionarios de productos y los guarda en el archivo JSON."""
    datos = restaurante.obtener_productos_como_diccionario()
    if archivo_servicio.guardar_productos(datos):
        print("✔ [Sincronización]: Cambios guardados en datos/productos.json.")


def solicitar_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un valor numérico entero válido.")


def solicitar_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingrese un número decimal válido.")


def ejecutar_registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Producto ---")
    try:
        id_prod = solicitar_entero("ID del producto: ")
        nombre = input("Nombre: ")
        precio = solicitar_flotante("Precio: $")
        categoria = input("Categoría: ")

        nuevo = Producto(id_prod, nombre, precio, categoria)
        restaurante.registrar_producto(nuevo)
        print("✔ Producto registrado en memoria.")
        sincronizar_datos(restaurante, archivo_servicio)
    except ValueError as e:
        print(f"❌ Error de validación: {e}")


def ejecutar_buscar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Buscar Producto ---")
    id_prod = solicitar_entero("Ingrese ID a buscar: ")
    producto = restaurante.buscar_producto_por_id(id_prod)
    if producto:
        print(f"✔ Encontrado: {producto}")
    else:
        print("❌ No existe ningún producto con ese ID.")


def ejecutar_actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Actualizar Producto ---")
    id_prod = solicitar_entero("ID del producto a modificar: ")
    producto = restaurante.buscar_producto_por_id(id_prod)

    if not producto:
        print("❌ Producto no encontrado.")
        return

    print(f"Estado actual: {producto}")
    try:
        nombre = input("Nuevo Nombre (presione Enter para conservar): ") or producto.nombre
        categoria = input("Nueva Categoría (presione Enter para conservar): ") or producto.categoria
        prec_str = input("Nuevo Precio (presione Enter para conservar): ")
        precio = float(prec_str) if prec_str.strip() else producto.precio

        if restaurante.actualizar_producto(id_prod, nombre, precio, categoria):
            print("✔ Producto actualizado en memoria.")
            sincronizar_datos(restaurante, archivo_servicio)
    except ValueError as e:
        print(f"❌ Error al actualizar: {e}")


def ejecutar_eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Eliminar Producto ---")
    id_prod = solicitar_entero("ID del producto a eliminar: ")
    if restaurante.eliminar_producto(id_prod):
        print("✔ Producto eliminado de la memoria.")
        sincronizar_datos(restaurante, archivo_servicio)
    else:
        print("❌ No se encontró el producto especificado.")


def ejecutar_listar_productos(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Catálogo de Productos ---")
    productos = restaurante.obtener_todos_los_productos()
    if not productos:
        print("No hay productos cargados en la lista.")
        return
    for prod in productos:
        print(f"  • {prod}")


def ejecutar_registrar_usuario(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar Usuario (Memoria) ---")
    identificacion = input("Identificación: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")

    usuario = Usuario(identificacion, nombre, correo)
    restaurante.registrar_usuario(usuario)
    print("✔ Usuario agregado a la memoria del sistema.")


def ejecutar_listar_usuarios(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Usuarios Registrados en Memoria ---")
    usuarios = restaurante.obtener_todos_los_usuarios()
    if not usuarios:
        print("No hay usuarios en memoria.")
        return
    for u in usuarios:
        print(f"  • {u}")


def ejecutar_sincronizacion(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    sincronizar_datos(restaurante, archivo_servicio)


def main() -> None:
    # 1. Instanciación de servicios
    archivo_servicio = ArchivoServicio("datos/productos.json")
    restaurante = Restaurante()

    # 2. Carga inicial desde archivo JSON
    print("Cargando productos almacenados...")
    datos_recuperados = archivo_servicio.cargar_productos()
    restaurante.cargar_desde_diccionarios(datos_recuperados)

    # 3. Diccionario despachador
    menu_despachador = {
        "1": ejecutar_registrar_producto,
        "2": ejecutar_buscar_producto,
        "3": ejecutar_actualizar_producto,
        "4": ejecutar_eliminar_producto,
        "5": ejecutar_listar_productos,
        "6": ejecutar_registrar_usuario,
        "7": ejecutar_listar_usuarios,
        "8": ejecutar_sincronizacion,
    }

    # 4. Bucle principal
    while True:
        for opcion in OPCIONES_MENU:
            print(opcion)
        print("------------------------------------------")

        eleccion = input("Seleccione una opción (1-9): ").strip()

        if eleccion == "9":
            print("\nGuardando cambios finales y cerrando la aplicación...")
            sincronizar_datos(restaurante, archivo_servicio)
            print("¡Hasta luego!")
            break

        accion = menu_despachador.get(eleccion)
        if accion:
            accion(restaurante, archivo_servicio)
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()