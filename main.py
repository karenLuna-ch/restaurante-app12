from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def main():

    restaurante = Restaurante()

    while True:

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))

            producto = Producto(codigo, nombre, categoria, precio)

            try:
                restaurante.registrar_producto(producto)
                print("Producto registrado correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == "2":

            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            volumen = int(input("Volumen (ml): "))

            bebida = Bebida(codigo, nombre, categoria, precio, volumen)

            try:
                restaurante.registrar_producto(bebida)
                print("Bebida registrada correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == "3":

            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            cliente = Cliente(identificacion, nombre, correo)

            try:
                restaurante.registrar_cliente(cliente)
                print("Cliente registrado correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == "4":

            restaurante.listar_productos()

        elif opcion == "5":

            restaurante.listar_clientes()

        elif opcion == "6":

            print("Gracias por utilizar el sistema.")
            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()