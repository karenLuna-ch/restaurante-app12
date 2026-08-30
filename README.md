# Restaurante App - Semana 11

**Estudiante:** Karen Antonela Chango Luna
**Asignatura:** Programación Orientada a Objetos
**Institución:** Universidad Estatal Amazónica

## Descripción del Sistema
`restaurante_app` es una aplicación modular en Python desarrollada bajo los principios de Programación Orientada a Objetos. En esta entrega (Semana 11), el sistema evoluciona incorporando relaciones inter-objeto mediante colecciones, relacionando a un `Usuario` con un `Producto` a través de la entidad `Venta`. Además, incluye control estricto de inventario (stock) y persistencia completa en formato JSON.

## Estructura del Proyecto
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