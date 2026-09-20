import tkinter as tk
from tkinter import messagebox, ttk

class MainView(tk.Toplevel):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Gestión - Restaurante App")
        self.geometry("900x550")

        self.crear_componentes()
        self.cargar_tabla_productos()
        self.cargar_tabla_usuarios()

    def crear_componentes(self):
        # Contenedor Principal en pestañas o secciones
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- SECCIÓN PRODUCTOS ---
        tab_productos = ttk.Frame(notebook, padding="10")
        notebook.add(tab_productos, text="Gestión de Productos")

        # Contenedor Izquierdo: Formulario y Acciones
        form_frame = ttk.LabelFrame(tab_productos, text=" Datos del Producto ", padding="10")
        form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(form_frame, text="ID:").pack(anchor="w", pady=2)
        self.txt_id = ttk.Entry(form_frame, width=25)
        self.txt_id.pack(pady=2)

        ttk.Label(form_frame, text="Nombre:").pack(anchor="w", pady=2)
        self.txt_nombre = ttk.Entry(form_frame, width=25)
        self.txt_nombre.pack(pady=2)

        ttk.Label(form_frame, text="Precio:").pack(anchor="w", pady=2)
        self.txt_precio = ttk.Entry(form_frame, width=25)
        self.txt_precio.pack(pady=2)

        # Contenedor de Botones de Acción (con command=)
        btn_frame = ttk.Frame(form_frame, padding="5")
        btn_frame.pack(fill=tk.X, pady=15)

        ttk.Button(btn_frame, text="Registrar", command=self.registrar_producto).pack(fill=tk.X, pady=3)
        ttk.Button(btn_frame, text="Actualizar", command=self.actualizar_producto).pack(fill=tk.X, pady=3)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).pack(fill=tk.X, pady=3)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario).pack(fill=tk.X, pady=3)

        # Contenedor Derecho: Tabla (Treeview) de Productos
        table_frame = ttk.LabelFrame(tab_productos, text=" Listado de Productos ", padding="10")
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.tree_productos = ttk.Treeview(table_frame, columns=("ID", "Nombre", "Precio"), show="headings")
        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree_productos.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_productos.configure(yscrollcommand=scrollbar.set)

        # --- SECCIÓN USUARIOS ---
        tab_usuarios = ttk.Frame(notebook, padding="10")
        notebook.add(tab_usuarios, text="Consulta de Usuarios")

        user_table_frame = ttk.LabelFrame(tab_usuarios, text=" Usuarios Registrados ", padding="10")
        user_table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.tree_usuarios = ttk.Treeview(user_table_frame, columns=("Usuario", "Rol"), show="headings")
        self.tree_usuarios.heading("Usuario", text="Usuario")
        self.tree_usuarios.heading("Rol", text="Rol / Tipo")
        self.tree_usuarios.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        scroll_user = ttk.Scrollbar(user_table_frame, orient=tk.VERTICAL, command=self.tree_usuarios.yview)
        scroll_user.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree_usuarios.configure(yscrollcommand=scroll_user.set)

    # --- MÉTODOS DE CONTROL Y DELEGACIÓN AL SERVICIO ---
    def cargar_tabla_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_productos.insert("", tk.END, values=(p.get("id"), p.get("nombre"), p.get("precio")))

    def cargar_tabla_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree_usuarios.insert("", tk.END, values=(u.get("usuario"), u.get("rol", "General")))

    def registrar_producto(self):
        try:
            nuevo = {
                "id": self.txt_id.get().strip(),
                "nombre": self.txt_nombre.get().strip(),
                "precio": float(self.txt_precio.get().strip())
            }
            self.servicio.registrar_producto(nuevo)
            self.cargar_tabla_productos()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_producto(self):
        try:
            actualizado = {
                "id": self.txt_id.get().strip(),
                "nombre": self.txt_nombre.get().strip(),
                "precio": float(self.txt_precio.get().strip())
            }
            self.servicio.actualizar_producto(actualizado)
            self.cargar_tabla_productos()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_producto(self):
        try:
            prod_id = self.txt_id.get().strip()
            self.servicio.eliminar_producto(prod_id)
            self.cargar_tabla_productos()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_formulario(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        