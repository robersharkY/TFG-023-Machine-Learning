from tkinter.messagebox import showinfo
from Vista.App import App

# Clase Vista: Contiene todos los métodos que forman la vista

class Vista:

    def __init__(self):
        self.app_ = App()
    
    def iniciar(self):
        self.app_.iniciar_frame()

    def get_combobox_algoritmo(self):
        return self.app_.get_combobox_algoritmo()

    def get_combobox_bag(self):
        return self.app_.get_combobox_bag()
    
    def get_boton_variables(self):
        return self.app_.get_boton_variables()

    def get_menu_archivo(self):
        return self.app_.get_menu_archivo()

    def get_menu_opciones(self):
        return self.app_.get_menu_opciones()

    def get_menu_configuracion(self):
        return self.app_.get_menu_configuracion()
        
    def get_menu_ayuda(self):
        return self.app_.get_menu_ayuda()

    def get_variables(self):
        return self.app_.get_array_variables()
    
    def mostrar_ventana_input(self, array_variables):
        self.app_.abrir_ventana_dialogo(self.app_.get_frame(), array_variables)

    def mostrar_ventana_mensaje(self, mensaje):
        showinfo(title = "Ventana de información", message = mensaje)
