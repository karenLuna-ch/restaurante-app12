import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    RUTA_DATOS = "datos"
    RUTA_PRODUCTOS = os.path.join(RUTA_DATOS, "productos.json")
    RUTA_USUARIOS = os.path.join(RUTA_DATOS, "usuarios.json")
    RUTA_VENTAS = os.path.join(RUTA_DATOS, "ventas.json")

    @classmethod
    def _asegurar_directorio(cls):
        if not os.path.exists(cls.RUTA_DATOS):
            os.makedirs(cls.RUTA_DATOS)

    # --- PRODUCTOS ---
    @classmethod
    def guardar_productos(cls, productos: list[Producto]) -> None:
        cls._asegurar_directorio()
        try:
            with open(cls.RUTA_PRODUCTOS, "w", encoding="utf-8") as f:
                json.dump([p.a_diccionario() for p in productos], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("[Error] Sin permisos para guardar productos.json")

    @classmethod
    def cargar_productos(cls) -> list[Producto]:
        if not os.path.exists(cls.RUTA_PRODUCTOS):
            return []
        try:
            with open(cls.RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Producto.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"[Advertencia] Error al cargar productos ({e}). Iniciando colección vacía.")
            return []
        except PermissionError:
            print("[Error] Sin permisos de lectura para productos.json")
            return []

    # --- USUARIOS ---
    @classmethod
    def guardar_usuarios(cls, usuarios: list[Usuario]) -> None:
        cls._asegurar_directorio()
        try:
            with open(cls.RUTA_USUARIOS, "w", encoding="utf-8") as f:
                json.dump([u.a_diccionario() for u in usuarios], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("[Error] Sin permisos para guardar usuarios.json")

    @classmethod
    def cargar_usuarios(cls) -> list[Usuario]:
        if not os.path.exists(cls.RUTA_USUARIOS):
            return []
        try:
            with open(cls.RUTA_USUARIOS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"[Advertencia] Error al cargar usuarios ({e}). Iniciando colección vacía.")
            return []
        except PermissionError:
            print("[Error] Sin permisos de lectura para usuarios.json")
            return []

    # --- VENTAS ---
    @classmethod
    def guardar_ventas(cls, ventas: list[Venta]) -> None:
        cls._asegurar_directorio()
        try:
            with open(cls.RUTA_VENTAS, "w", encoding="utf-8") as f:
                json.dump([v.a_diccionario() for v in ventas], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("[Error] Sin permisos para guardar ventas.json")

    @classmethod
    def cargar_ventas(cls) -> list[Venta]:
        if not os.path.exists(cls.RUTA_VENTAS):
            return []
        try:
            with open(cls.RUTA_VENTAS, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta.desde_diccionario(item) for item in datos]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"[Advertencia] Error al cargar ventas ({e}). Iniciando colección vacía.")
            return []
        except PermissionError:
            print("[Error] Sin permisos de lectura para ventas.json")
            return []