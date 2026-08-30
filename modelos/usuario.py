class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self._identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        if "@" not in valor or "." not in valor:
            raise ValueError("El correo electrónico no es válido.")
        self._correo = valor.strip()

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self._identificacion,
            "nombre": self._nombre,
            "correo": self._correo
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Usuario':
        try:
            return Usuario(
                identificacion=str(datos["identificacion"]),
                nombre=str(datos["nombre"]),
                correo=str(datos["correo"])
            )
        except (KeyError, ValueError) as e:
            raise KeyError(f"Estructura de usuario inválida en JSON: {e}")