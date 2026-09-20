import tkinter as tk
from tkinter import messagebox, ttk

class LoginView(tk.Tk):
    def __init__(self, servicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success
        
        self.title("Restaurante App - Login")
        self.geometry("350x250")
        self.resizable(False, False)
        
        self.crear_componentes()

    def crear_componentes(self):
        # Contenedor principal
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Iniciar Sesión", font=("Arial", 14, "bold")).pack(pady=10)

        # Campos
        ttk.Label(main_frame, text="Usuario:").pack(anchor="w")
        self.txt_usuario = ttk.Entry(main_frame, width=30)
        self.txt_usuario.pack(pady=5)

        ttk.Label(main_frame, text="Contraseña:").pack(anchor="w")
        self.txt_password = ttk.Entry(main_frame, width=30, show="*")
        self.txt_password.pack(pady=5)

        # Botón de acceso
        ttk.Button(main_frame, text="Ingresar", command=self.intentar_login).pack(pady=15, fill=tk.X)

    def intentar_login(self):
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        if self.servicio.validar_usuario(usuario, password):
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}")
            self.destroy()
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")