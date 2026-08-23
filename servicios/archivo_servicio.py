
import json
import os
from typing import List, Dict, Any


class ArchivoServicio:
    

    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        self.ruta_archivo = ruta_archivo
        self._asegurar_directorio()

    def _asegurar_directorio(self) -> None:
        
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    def guardar_productos(self, productos_dict: List[Dict[str, Any]]) -> bool:
       
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(productos_dict, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"\n[Error de Permisos]: No se tienen permisos de escritura en '{self.ruta_archivo}'.")
        except Exception as e:
            print(f"\n[Error Inesperado al Guardar]: {e}")
        return False

    def cargar_productos(self) -> List[Dict[str, Any]]:
        """Lee y retorna los datos del archivo JSON."""
        if not os.path.exists(self.ruta_archivo):
            return []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if isinstance(datos, list):
                    return datos
                else:
                    print("\n[Error de Estructura]: El archivo JSON no contiene una lista válida.")
                    return []
        except FileNotFoundError:
            print(f"\n[Aviso]: El archivo '{self.ruta_archivo}' no existe aún. Se creará al guardar.")
            return []
        except json.JSONDecodeError:
            print(f"\n[Error de Formato]: El archivo '{self.ruta_archivo}' está corrupto o no tiene formato JSON válido.")
            return []
        except PermissionError:
            print(f"\n[Error de Permisos]: No se tienen permisos de lectura en '{self.ruta_archivo}'.")
            return []