from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- RESTAURANTE APP - SEMANA 11 ---")
    print("1. Registrar Usuario")
    print("2. Listar Usuarios")
    print("3. Registrar Producto")
    print("4. Listar Productos")
    print("5. Realizar Venta")
    print("6. Consultar Ventas por Usuario")
    print("0. Salir")

def main():
    servicio = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                id_usr = input("Identificación: ").strip()
                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()
                if servicio.registrar_usuario(id_usr, nombre, correo):
                    print("--> Usuario registrado exitosamente.")
                else:
                    print("[!] La identificación ya está registrada.")
            except ValueError as e:
                print(f"[!] Error: {e}")

        elif opcion == "2":
            usuarios = servicio.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\n--- LISTA DE USUARIOS ---")
                for u in usuarios:
                    print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

        elif opcion == "3":
            try:
                cod = input("Código: ").strip()
                nom = input("Nombre: ").strip()
                pre = float(input("Precio: "))
                stk = int(input("Stock inicial: "))
                if servicio.registrar_producto(cod, nom, pre, stk):
                    print("--> Producto registrado exitosamente.")
                else:
                    print("[!] El código del producto ya existe.")
            except ValueError as e:
                print(f"[!] Entrada inválida: {e}")

        elif opcion == "4":
            productos = servicio.obtener_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in productos:
                    print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "5":
            try:
                id_usr = input("Identificación del Usuario: ").strip()
                cod_prod = input("Código del Producto: ").strip()
                cant = int(input("Cantidad a comprar: "))

                if servicio.vender_producto(cod_prod, id_usr, cant):
                    print("--> Venta realizada con éxito y stock actualizado.")
                else:
                    print("[!] Venta rechazada. Verifique la existencia del usuario/producto o la disponibilidad de stock.")
            except ValueError as e:
                print(f"[!] Error en el ingreso de datos: {e}")

        elif opcion == "6":
            id_usr = input("Identificación del Usuario: ").strip()
            usr = servicio.buscar_usuario(id_usr)
            if not usr:
                print("[!] El usuario no existe.")
            else:
                ventas = servicio.consultar_ventas_usuario(id_usr)
                if not ventas:
                    print(f"El usuario {usr.nombre} no tiene ventas registradas.")
                else:
                    print(f"\n--- HISTORIAL DE VENTAS: {usr.nombre} ---")
                    for venta, prod in ventas:
                        print(f"Producto: {prod.nombre} | Cantidad: {venta.cantidad}")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()