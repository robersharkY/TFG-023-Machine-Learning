## @package Vista
# @brief Clase Vista, interfaz que une todo lo comprendido de la vista con el controlador.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from tkinter.messagebox import showinfo
from Vista.App import App


class Vista:

    ## @brief Constructor de vista.
    def __init__(self):
        self.__app = App()
    
    def iniciar(self):
        self.__app.iniciar_frame()

    def get_combobox_algoritmo(self):
        return self.__app.get_combobox_algoritmo()

    def get_combobox_bag(self):
        return self.__app.get_combobox_bag()
    
    def get_boton_variables(self):
        return self.__app.get_boton_variables()

    def get_menu_archivo(self):
        return self.__app.get_menu_archivo()

    def get_menu_opciones(self):
        return self.__app.get_menu_opciones()

    def get_menu_configuracion(self):
        return self.__app.get_menu_configuracion()
        
    def get_menu_ayuda(self):
        return self.__app.get_menu_ayuda()

    def get_variables(self):
        return self.__app.get_array_variables()
    
    def mostrar_ventana_input(self, array_variables):
        self.__app.abrir_ventana_dialogo(self.__app.get_frame(), array_variables)

    def mostrar_ventana_mensaje(self, mensaje):
        showinfo(title = "Ventana de información", message = mensaje)
