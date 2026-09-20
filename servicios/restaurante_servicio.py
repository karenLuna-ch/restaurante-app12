import os
import json

class RestauranteServicio:
    def __init__(self):
        # Rutas relativas basadas en tu estructura de carpetas
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_productos = os.path.join(base_dir, "datos", "productos.json")
        self.ruta_usuarios = os.path.join(base_dir, "datos", "usuarios.json")

    def _leer_json(self, ruta):
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _escribir_json(self, ruta, datos):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    # --- LÓGICA DE USUARIOS ---
    def validar_usuario(self, username, password):
        usuarios = self._leer_json(self.ruta_usuarios)
        for u in usuarios:
            if u.get("usuario") == username and u.get("password") == password:
                return True
        return False

    def obtener_usuarios(self):
        return self._leer_json(self.ruta_usuarios)

    # --- LÓGICA DE PRODUCTOS (CRUD) ---
    def obtener_productos(self):
        return self._leer_json(self.ruta_productos)

    def registrar_producto(self, producto):
        productos = self.obtener_productos()
        # Validación básica de negocio
        if not producto.get("id") or not producto.get("nombre"):
            raise ValueError("El ID y el nombre del producto son obligatorios.")
        
        # Verificar duplicados
        for p in productos:
            if str(p.get("id")) == str(producto.get("id")):
                raise ValueError("Ya existe un producto con ese ID.")

        productos.append(producto)
        self._escribir_json(self.ruta_productos, productos)

    def actualizar_producto(self, producto_act):
        productos = self.obtener_productos()
        encontrado = False
        for i, p in enumerate(productos):
            if str(p.get("id")) == str(producto_act.get("id")):
                productos[i] = producto_act
                encontrado = True
                break
        if not encontrado:
            raise ValueError("No se encontró el producto a actualizar.")
        self._escribir_json(self.ruta_productos, productos)

    def eliminar_producto(self, producto_id):
        productos = self.obtener_productos()
        nuevos_productos = [p for p in productos if str(p.get("id")) != str(producto_id)]
        if len(nuevos_productos) == len(productos):
            raise ValueError("No se encontró el producto a eliminar.")
        self._escribir_json(self.ruta_productos, nuevos_productos)