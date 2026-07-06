# Sistema de Gestión de Restaurante Básico (POO)

**Estudiante:** Karen Antonela Chango Luna  
**Materia:** Programación Orientada a Objetos  

# Sistema de Gestión - Restaurante App (Versión 2)

Este proyecto consiste en una aplicación modular desarrollada en **Python** utilizando el paradigma de **Programación Orientada a Objetos (POO)**. El sistema está diseñado para administrar el catálogo de productos de un restaurante, clasificándolos de manera lógica en platillos y bebidas.

El diseño arquitectónico toma como referencia metodológica los principios de modularidad y separación de responsabilidades aprendidos en clase, adaptándolos a un contexto de negocio gastronómico.

---

## 🛠️ Estructura del Proyecto

El código está organizado bajo una estructura limpia y escalable:

```text
RESTAURANTE_APP2/
├── modelos/
│   ├── __init__.py
│   ├── producto.py    # Clase padre (General)
│   ├── platillo.py    # Clase hija (Especializada)
│   └── bebida.py      # Clase hija (Especializada)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py # Clase de servicio (Gestión de lista/menú)
├── main.py            # Punto de entrada de la aplicación
└── README.md          # Documentación del proyecto