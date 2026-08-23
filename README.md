# Restaurante App - Semana 10 (Persistencia JSON)

**Estudiante:** Karen Antonela Chango Luna  
**Carrera:** Tecnologías de la Información - Universidad Estatal Amazónica  

## Descripción del Sistema
Evolución del sistema `restaurante_app` que incorpora **persistencia de datos real** mediante un archivo externo en formato JSON (`datos/productos.json`). El sistema permite registrar, actualizar, eliminar, buscar y listar productos, garantizando que la información subsista tras el cierre de la aplicación.

---

## Estructura del Proyecto
```text
restaurante_app2/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
