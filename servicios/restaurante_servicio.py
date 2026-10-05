from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        data = self.archivo_servicio.leer_json("datos/usuarios.json")
        return [Usuario.from_dict(u) for u in data]

    def guardar_usuarios(self):
        data = [u.to_dict() for u in self.usuarios]
        self.archivo_servicio.escribir_json("datos/usuarios.json", data)

    def validar_usuario(self, username, password):
        self.usuarios = self.cargar_usuarios()
        for u in self.usuarios:
            if (str(u.username) == str(username) or str(u.id_usuario) == str(username)) and str(u.password) == str(password):
                return u
        return None

    def registrar_usuario(self, id_usuario, nombre, username, password, rol):
        for u in self.usuarios:
            if u.id_usuario == id_usuario or u.username == username:
                return False, "El ID o el nombre de usuario ya existen."
        
        nuevo_usuario = Usuario(id_usuario, nombre, username, password, rol)
        self.usuarios.append(nuevo_usuario)
        self.guardar_usuarios()
        return True, "Usuario registrado exitosamente."

    def actualizar_usuario(self, id_usuario, nombre, username, password, rol):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                u.nombre = nombre
                u.username = username
                if password:
                    u.password = password
                u.rol = rol
                self.guardar_usuarios()
                return True, "Usuario actualizado exitosamente."
        return False, "Usuario no encontrado."

    def eliminar_usuario(self, id_usuario):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                self.usuarios.remove(u)
                self.guardar_usuarios()
                return True, "Usuario eliminado exitosamente."
        return False, "Usuario no encontrado."

    def buscar_usuario_por_id(self, id_usuario):
        for u in self.usuarios:
            if str(u.id_usuario) == str(id_usuario):
                return u
        return None