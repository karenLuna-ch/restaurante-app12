from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_app():
    servicio = RestauranteServicio()

    def abrir_principal():
        MainView(servicio)

    app = LoginView(servicio, abrir_principal)
    app.mainloop()

if __name__ == "__main__":
    iniciar_app()