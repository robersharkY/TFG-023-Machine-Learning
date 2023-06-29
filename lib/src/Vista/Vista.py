## @package Vista
# @brief Clase Vista, interfaz que une todo lo comprendido de la vista para ser usado en el controlador.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from tkinter.messagebox import showinfo
from Vista.App import App
import tkinter as tk


class Vista:

    ## @brief Constructor de vista.
    def __init__(self):
        self.__app = App()
    
    ## @brief Muestra el frame de la aplicación.
    def iniciar_frame(self):
        self.__app.mostrar_app()

    ## @brief Devuelve el combo de los algoritmos del Mainframe.
    # @return [ComboBox] Combo de los algoritmos a elegir.
    def get_combobox_algoritmo(self):
        return self.__app.get_combobox_algoritmo()
    
    ## @brief Devuelve el combo de las bolsas de palabras del Mainframe.
    # @return [ComboBox] Combo de las bolsas de palabras a elegir.
    def get_combobox_bag(self):
        return self.__app.get_combobox_bag()
    
    ## @brief Devuelve el botón de "Aplicar cambios" de la ventana de configuración.
    # @return [Button] Botón de aplicar cambios de la ventana de configuración.
    def get_boton_configuracion(self):
        return self.__app.get_boton_configuracion()

    ## @brief Devuelve el menú específico del apartado "Archivo" de la app.
    # @return [Menu] Menú del apartado "Archivo".
    def get_menu_archivo(self):
        return self.__app.get_menu_archivo()

    ## @brief Devuelve el menú específico del apartado "Opciones" de la app.
    # @return [Menu] Menú del apartado "Opciones".
    def get_menu_opciones(self):
        return self.__app.get_menu_opciones()

    ## @brief Devuelve el menú específico del apartado "Configuración" de la app.
    # @return [Menu] Menú del apartado "Configuración".
    def get_menu_configuracion(self):
        return self.__app.get_menu_configuracion()

    ## @brief Devuelve el menú específico del apartado "Ayuda" de la app.
    # @return [Menu] Menú del apartado "Ayuda".
    def get_menu_ayuda(self):
        return self.__app.get_menu_ayuda()

    ## @brief Devuelve las variables de configuración actual de la ventana de configuración.
    # @return [Array] Variables de la configuración.
    def get_variables_configuracion(self):
        return self.__app.get_variables_configuracion()
    
    ## @brief Crea la ventana auxiliar del apartado de configuración.
    # @param variables_configuracion [Array] Variables de la configuración actual del apartado de configuración. 
    def mostrar_ventana_configuracion(self, variables_configuracion):
        self.__app.crear_ventana_configuracion(self.__app.get_frame(), variables_configuracion)
    
    ## @brief Crea ventanas de avisos de cadenas que se pasen por parámetro.
    # @param mensaje [String] Cadena a mostrar en la ventana de aviso.
    def mostrar_ventana_mensaje(self, mensaje):
        showinfo(title = "Ventana de información", message = mensaje)
        
