class Usuario:
    def __init__(self, cedula: str, nombre: str, correo: str):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo

    def to_dict(self) -> dict:
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @staticmethod
    def from_dict(data: dict):
        return Usuario(
            cedula=data["cedula"],
            nombre=data["nombre"],
            correo=data["correo"]
        )
    