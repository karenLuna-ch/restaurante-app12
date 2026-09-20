# Restaurante App - Semana 14

## Propósito de la actividad
Evolución de la aplicación de gestión para el restaurante, integrando una interfaz gráfica basada en **componentes y contenedores de Tkinter/ttk** (como `Frame`, `LabelFrame`, `Entry`, `Button` y `Treeview`). Se mantiene la arquitectura modular y la separación de responsabilidades, delegando las validaciones y reglas de negocio al servicio correspondiente y asegurando la persistencia mediante archivos JSON.

## Estructura del Proyecto
restaurante_app2/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

## Componentes y Contenedores Utilizados
- **Contenedores:** `ttk.Frame` y `ttk.LabelFrame` para agrupar visualmente los formularios de registro y los paneles de listado.
- **Componentes de Entrada y Acción:** `ttk.Entry` para la captura de datos y `ttk.Button` vinculados mediante `command=` para ejecutar las operaciones CRUD.
- **Visualización:** `ttk.Treeview` estructurado con barras de desplazamiento para la consulta organizada de productos y usuarios.

## Operaciones Implementadas (CRUD de Productos)
- **Registro:** Permite dar de alta nuevos productos y persistirlos automáticamente en `productos.json`.
- **Consulta / Carga:** Visualiza el catálogo actual de productos y la información de usuarios registrados.
- **Actualización:** Modifica registros existentes manteniendo la persistencia.
- **Eliminación:** Borra elementos del sistema de manera controlada a través de la capa de servicios.

## Instrucciones de Ejecución
1. Asegúrate de tener Python instalado con soporte para Tkinter.
2. Abre la terminal en la raíz del proyecto.
3. Ejecuta el punto de entrada principal:
   ```bash
   python main.py