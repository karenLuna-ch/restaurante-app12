# Restaurante App - Semana 16

## 📌 Propósito de la Semana 16
Esta semana el proyecto evoluciona aplicando el **manejo de eventos en Tkinter** dentro de una situación real del sistema: la **gestión de usuarios**. Se implementa el CRUD completo (registrar, consultar, actualizar y eliminar) integrando eventos virtuales, de teclado y selección, manteniendo la arquitectura modular, la separación de responsabilidades y la persistencia en archivos JSON.

---

## 🛠️ Estructura del Proyecto
El proyecto mantiene una arquitectura modular clara:
```text
restaurante_app2/
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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/                  (íconos, logo y recursos visuales)
├── main.py
└── README.md