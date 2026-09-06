from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n" + "=" * 40)
    print("      RESTAURANTE APP - SEMANA 12")
    print("=" * 40)
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Buscar producto por código")
    print("4. Buscar usuario por cédula")
    print("5. Registrar venta")
    print("6. Consultar ventas por usuario")
    print("7. Salir")
    print("=" * 40)


def ejecutar_app():
    servicio = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- Registrar Usuario ---")
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()

            if not cedula or not nombre or not correo:
                print("⚠️ Todos los campos son obligatorios.")
            elif servicio.registrar_usuario(cedula, nombre, correo):
                print("✅ Usuario registrado con éxito.")
            else:
                print("❌ Error: Ya existe un usuario con esa cédula.")

        elif opcion == "2":
            print("\n--- Registrar Producto ---")
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            
            try:
                precio = float(input("Precio: ").strip())
                stock = int(input("Stock inicial: ").strip())
                
                if precio <= 0 or stock < 0:
                    print("⚠️ El precio debe ser mayor a 0 y el stock no puede ser negativo.")
                elif servicio.registrar_producto(codigo, nombre, precio, stock):
                    print("✅ Producto registrado con éxito.")
                else:
                    print("❌ Error: Ya existe un producto con ese código.")
            except ValueError:
                print("⚠️ Formato de número inválido para precio o stock.")

        elif opcion == "3":
            print("\n--- Buscar Producto ---")
            codigo = input("Ingrese el código del producto: ").strip()
            producto = servicio.buscar_producto(codigo)

            if producto:
                print(f"📦 Producto: {producto.nombre} | Código: {producto.codigo} | Precio: ${producto.precio:.2f} | Stock: {producto.stock}")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            print("\n--- Buscar Usuario ---")
            cedula = input("Ingrese la cédula del usuario: ").strip()
            usuario = servicio.buscar_usuario(cedula)

            if usuario:
                print(f"👤 Usuario: {usuario.nombre} | Cédula: {usuario.cedula} | Correo: {usuario.correo}")
            else:
                print("❌ Usuario no encontrado.")

        elif opcion == "5":
            print("\n--- Registrar Venta ---")
            cedula = input("Cédula del usuario: ").strip()
            codigo = input("Código del producto: ").strip()

            try:
                cantidad = int(input("Cantidad a comprar: ").strip())
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a 0.")
                else:
                    exito, mensaje = servicio.registrar_venta(cedula, codigo, cantidad)
                    if exito:
                        print(f"✅ {mensaje}")
                    else:
                        print(f"❌ {mensaje}")
            except ValueError:
                print("⚠️ Ingrese una cantidad numérica entera.")

        elif opcion == "6":
            print("\n--- Consultar Ventas de Usuario ---")
            cedula = input("Ingrese la cédula del usuario: ").strip()
            ventas = servicio.consultar_ventas_usuario(cedula)

            if ventas:
                print(f"\n📋 Historial de ventas para la cédula {cedula}:")
                for v in ventas:
                    print(f"  • Venta #{v.id_venta} | Producto: {v.codigo_producto} | Cantidad: {v.cantidad} | Total: ${v.total:.2f}")
            else:
                print("ℹ️ No se encontraron ventas registradas para este usuario.")

        elif opcion == "7":
            print("\n👋 ¡Gracias por usar Restaurante App! Guardando sesión...")
            break
        else:
            print("⚠️ Opción no válida. Intente del 1 al 7.")


if __name__ == "__main__":
    ejecutar_app()