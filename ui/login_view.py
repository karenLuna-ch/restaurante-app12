import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class LoginView(tk.Tk):
    def __init__(self, servicio, on_login_success):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success
        
        self.title("Restaurante App - Login")
        self.geometry("400x480")
        self.config(bg="#f8d7da")  # Fondo rosado
        
        # Cargar logo desde la carpeta assets
        ruta_logo = "assets/logo.png"
        if os.path.exists(ruta_logo):
            try:
                imagen_pil = Image.open(ruta_logo)
                imagen_pil = imagen_pil.resize((90, 90))
                self.logo_img = ImageTk.PhotoImage(imagen_pil)
                lbl_logo = tk.Label(self, image=self.logo_img, bg="#f8d7da")
                lbl_logo.pack(pady=10)
            except Exception as e:
                print("Error cargando logo:", e)

        lbl_titulo = tk.Label(self, text="Inicio de Sesión", font=("Arial", 16, "bold"), bg="#f8d7da", fg="#333333")
        lbl_titulo.pack(pady=10)

        lbl_user = tk.Label(self, text="Usuario:", bg="#f8d7da", font=("Arial", 11))
        lbl_user.pack(anchor="w", padx=60)
        self.entry_user = tk.Entry(self, font=("Arial", 12), width=25)
        self.entry_user.pack(pady=5)

        lbl_pass = tk.Label(self, text="Contraseña:", bg="#f8d7da", font=("Arial", 11))
        lbl_pass.pack(anchor="w", padx=60)
        self.entry_pass = tk.Entry(self, font=("Arial", 12), width=25, show="*")
        self.entry_pass.pack(pady=5)

        btn_ingresar = tk.Button(self, text="Ingresar", font=("Arial", 11, "bold"), bg="#e0a899", fg="white", width=15, command=self.intentar_login)
        btn_ingresar.pack(pady=20)

    def intentar_login(self):
        usuario = self.entry_user.get()
        password = self.entry_pass.get()
        user_obj = self.servicio.validar_usuario(usuario, password)
        if user_obj:
            self.on_login_success(user_obj)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")