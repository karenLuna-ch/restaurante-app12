# Restaurante App - Semana 12: Optimización mediante Colecciones

Evolución del sistema modular `restaurante_app` orientada a la optimización de búsquedas, consultas y validaciones en memoria utilizando estructuras auxiliares (`dict` y `set`), manteniendo la persistencia en formato JSON.

---

## 🚀 Mejoras de Rendimiento Aplicadas

| Operación | Colección Utilizada | Tipo de Estructura | Complejidad / Beneficio |
| :--- | :--- | :--- | :--- |
| **Búsqueda de Producto** | `_indice_productos_codigo` | `dict` | Búsqueda $O(1)$ por código de producto sin recorrer la lista. |
| **Búsqueda de Usuario** | `_indice_usuarios_cedula` | `dict` | Búsqueda $O(1)$ por número de cédula o identificación. |
| **Consulta de Ventas por Usuario** | `_indice_ventas_usuario` | `dict` (de listas) | Acceso directo $O(1)$ al historial de un usuario sin escanear todas las ventas. |
| **Validación de Unicidad** | `_codigos_existentes` | `set` | Comprobación instantánea $O(1)$ previa al registro de nuevos productos. |

> **Nota:** Las listas principales (`productos`, `usuarios`, `ventas`) se mantienen intactas para preservar el ordenamiento, la iteración secuencial y la persistencia hacia los archivos JSON.

---

## 📁 Estructura Modular del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md