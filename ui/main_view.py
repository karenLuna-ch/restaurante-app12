import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self, restaurante_servicio, usuario_actual):
        super().__init__()
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual

        self.title("Sistema de Gestión - Restaurante App")
        self.geometry("900x600")
        
        # Contenedor principal de pestañas o vistas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # 1. Pestaña de Productos (Funcionalidad de semanas anteriores)
        self.crear_pestana_productos()

        # 2. Pestaña de Ventas (Funcionalidad de semanas anteriores)
        self.crear_pestana_ventas()

        # 3. Pestaña de Usuarios (Evolución obligatoria Semana 16 con manejo de eventos)
        # Solo se añade o habilita completamente si es Administrador, o se muestra con control de acceso
        self.seccion_usuarios = SeccionUsuarios(self.notebook, self.restaurante_servicio, self.usuario_actual)
        self.notebook.add(self.seccion_usuarios, text="Gestión de Usuarios")

    def crear_pestana_productos(self):
        frame_productos = ttk.Frame(self.notebook)
        self.notebook.add(frame_productos, text="Productos")
        ttk.Label(frame_productos, text="Módulo de Productos (Semanas Anteriores)", font=("Arial", 14)).pack(pady=20)

    def crear_pestana_ventas(self):
        frame_ventas = ttk.Frame(self.notebook)
        self.notebook.add(frame_ventas, text="Ventas")
        ttk.Label(frame_ventas, text="Módulo de Ventas (Semanas Anteriores)", font=("Arial", 14)).pack(pady=20)


class SeccionUsuarios(ttk.Frame):
    def __init__(self, parent, restaurante_servicio, usuario_actual):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        
        # Validar control de acceso: Solo el Administrador puede gestionar usuarios
        if self.usuario_actual.rol != "Administrador":
            # Si no es admin, mostramos un aviso restrictivo en la pestaña
            lbl_denegado = ttk.Label(self, text="Acceso Restringido. Se requiere rol de Administrador.", font=("Arial", 12), foreground="red")
            lbl_denegado.pack(pady=50)
            return

        self.crear_widgets()
        self.cargar_tabla_usuarios()

    def crear_widgets(self):
        # --- Formulario de Usuario ---
        form_frame = ttk.LabelFrame(self, text="Formulario de Usuarios")
        form_frame.pack(fill="x", padx=10, pady=10)

        # ID Usuario
        ttk.Label(form_frame, text="ID Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_id = ttk.Entry(form_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        # Nombre
        ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(form_frame)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        # Username
        ttk.Label(form_frame, text="Usuario (Username):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_username = ttk.Entry(form_frame)
        self.entry_username.grid(row=2, column=1, padx=5, pady=5)

        # Contraseña
        ttk.Label(form_frame, text="Contraseña:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_password = ttk.Entry(form_frame, show="*")
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)

        # Rol (Combobox obligatorio para evento <<ComboboxSelected>>)
        ttk.Label(form_frame, text="Rol:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.combo_rol = ttk.Combobox(form_frame, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.combo_rol.grid(row=4, column=1, padx=5, pady=5)
        # Asociar evento ComboboxSelected mediante bind()
        self.combo_rol.bind("<<ComboboxSelected>>", self.on_combobox_rol_selected)

        # --- Botones de Acciones (Asociados mediante command=) ---
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)

        self.btn_registrar = ttk.Button(btn_frame, text="Registrar", command=self.accion_registrar)
        self.btn_registrar.pack(side="left", padx=5)

        self.btn_actualizar = ttk.Button(btn_frame, text="Actualizar", command=self.accion_actualizar)
        self.btn_actualizar.pack(side="left", padx=5)

        self.btn_eliminar = ttk.Button(btn_frame, text="Eliminar", command=self.accion_eliminar)
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_limpiar = ttk.Button(btn_frame, text="Limpiar", command=self.accion_limpiar)
        self.btn_limpiar.pack(side="left", padx=5)

        # --- Tabla Treeview para listar usuarios ---
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Usuario", "Rol"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Rol", text="Rol")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Asociar evento <<TreeviewSelect>> mediante bind() ---
        self.tree.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # --- Asociar eventos de teclado mediante bind() ---
        self.bind("<Return>", self.on_key_return)
        self.bind("<Escape>", self.on_key_escape)
        self.focus_set()  # Necesario para capturar las teclas

    # ================= EVENTOS Y CALLBACKS =================

    def on_treeview_select(self, event):
        """Callback para <<TreeviewSelect>>: carga los datos del usuario seleccionado al formulario."""
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion)
            valores = item["values"]
            id_usuario = valores[0]
            
            # Consultar el objeto mediante el servicio
            usuario = self.restaurante_servicio.buscar_usuario_por_id(str(id_usuario))
            if usuario:
                self.entry_id.config(state="normal")
                self.entry_id.delete(0, tk.END)
                self.entry_id.insert(0, usuario.id_usuario)
                self.entry_id.config(state="disabled")  # Bloquear ID en edición
                
                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.insert(0, usuario.nombre)
                
                self.entry_username.delete(0, tk.END)
                self.entry_username.insert(0, usuario.username)
                
                self.entry_password.delete(0, tk.END)
                self.entry_password.insert(0, usuario.password)
                
                self.combo_rol.set(usuario.rol)

    def on_combobox_rol_selected(self, event):
        """Callback para <<ComboboxSelected>>: responde al cambio de opción en el combobox."""
        _ = self.combo_rol.get()

    def on_key_return(self, event):
        """Callback para <Return>: atajo de teclado para registrar el usuario."""
        self.accion_registrar()

    def on_key_escape(self, event):
        """Callback para <Escape>: limpia el formulario y cancela la selección."""
        self.accion_limpiar()

    # ================= ACCIONES DE LOS BOTONES =================

    def accion_registrar(self):
        id_u = self.entry_id.get().strip()
        nombre = self.entry_nombre.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        rol = self.combo_rol.get().strip()

        if not id_u or not nombre or not username or not password or not rol:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
            return

        exito, mensaje = self.restaurante_servicio.registrar_usuario(id_u, nombre, username, password, rol)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargar_tabla_usuarios()
            self.accion_limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    def accion_actualizar(self):
        id_u = self.entry_id.get().strip()
        nombre = self.entry_nombre.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        rol = self.combo_rol.get().strip()

        if not id_u:
            messagebox.showwarning("Selección requerida", "Seleccione un usuario de la tabla para actualizar.")
            return

        exito, mensaje = self.restaurante_servicio.actualizar_usuario(id_u, nombre, username, password, rol)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargar_tabla_usuarios()
            self.accion_limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    def accion_eliminar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Seleccione un usuario de la tabla para eliminar.")
            return

        item = self.tree.item(seleccion)
        id_usuario = item["values"][0]

        # Validar que el administrador actual no se elimine a sí mismo
        if str(id_usuario) == str(self.usuario_actual.id_usuario):
            messagebox.showerror("Acción no permitida", "No puede eliminar la cuenta de administrador con la que se encuentra autenticado.")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar este usuario?")
        if confirmar:
            exito, mensaje = self.restaurante_servicio.eliminar_usuario(str(id_usuario))
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.cargar_tabla_usuarios()
                self.accion_limpiar()
            else:
                messagebox.showerror("Error", mensaje)

    def accion_limpiar(self):
        """Limpia el formulario y restablece el estado inicial."""
        self.entry_id.config(state="normal")
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.combo_rol.set("")
        
        # Quitar selección del Treeview
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def cargar_tabla_usuarios(self):
        """Llena el Treeview con los usuarios registrados en el servicio."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for u in self.restaurante_servicio.usuarios:
            self.tree.insert("", "end", values=(u.id_usuario, u.nombre, u.username, u.rol))