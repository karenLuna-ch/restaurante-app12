from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_app():
    archivo_serv = ArchivoServicio()
    servicio = RestauranteServicio(archivo_serv)
    
    def abrir_ventana_principal(usuario_actual):
        login_window.destroy()
        app_principal = MainView(servicio, usuario_actual)
        app_principal.mainloop()

    login_window = LoginView(servicio, abrir_ventana_principal)
    login_window.mainloop()

if __name__ == "__main__":
    iniciar_app()