## @package Vista
# @brief Clase App, clase que une todos los frames, ventanas y barras.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

import tkinter as tk
from tkinter import *
from Vista.MainFrame import MainFrame
import os

class App(tk.Tk):

    ## @brief Constructor de App.
    def __init__(self):
        super().__init__()
        self.crear_app() # Se crea los elementos de la app pero no se visualiza aún.
    
    ## @brief Construye y junta todos los elementos visuales de la aplicación.
    def crear_app(self):
        # Elementos MainFrame.
        self.title('Machine learning (TFG 2223-023)')
        self.geometry('500x400')
        self.resizable(False, False)
        self.crear_barra_menu()
        self.__frame = MainFrame(self) # Clase MainFrame construida previamente

        # Elementos de iconos.
        ruta = os.path.dirname(os.path.abspath(__file__))
        imagen = os.path.join(ruta, "..\\..\\resources", "icono_PML.png")
        icono_pequeno = tk.PhotoImage(False, file = imagen)
        self.iconphoto(True, icono_pequeno)

        # Elementos de la ventana de configuración.
        self.__ventana_input = None
        self.__boton_configuracion = Button(self.__ventana_input, text = "Aplicar cambios", font = ("Helvetica",9), background = "#E5CCFF")
        self.__entrada_texto_tematicas = None
        self.__entrada_texto_probs = None
        self.__entrada_texto_extracto = None
        self.__entrada_texto_tematicas = None
    
    ## @brief Muestra el frame de la aplicación.
    def mostrar_app(self):
        self.mainloop()

    ## @brief Devuelve el propio frame de la app.
    # @return [Frame] Frame de la app.
    def get_frame(self):
        return self
    
    ## @brief Devuelve el menú específico del apartado "Archivo".
    # @return [Menu] Menú del apartado "Archivo".
    def get_menu_archivo(self):
        return self.__menu_archivo

    ## @brief Devuelve el menú específico del apartado "Opciones".
    # @return [Menu] Menú del apartado "Opciones".
    def get_menu_opciones(self):
        return self.__menu_opciones

    ## @brief Devuelve el menú específico del apartado "Configuración".
    # @return [Menu] Menú del apartado "Configuración".
    def get_menu_configuracion(self):
        return self.__menu_configuracion

    ## @brief Devuelve el menú específico del apartado "Ayuda".
    # @return [Menu] Menú del apartado "Ayuda".
    def get_menu_ayuda(self):
        return self.__menu_ayuda
    
    ## @brief Devuelve el combo de los algoritmos del Mainframe.
    # @return [ComboBox] Combo de los algoritmos a elegir.
    def get_combobox_algoritmo(self):
        return self.__frame.get_combobox_algoritmo()
    
    ## @brief Devuelve el combo de las bolsas de palabras del Mainframe.
    # @return [ComboBox] Combo de las bolsas de palabras a elegir.
    def get_combobox_bag(self):
        return self.__frame.get_combobox_bag()

    ## @brief Devuelve el botón de "Aplicar cambios" de la ventana de configuración.
    # @return [Button] Botón de aplicar cambios de la ventana de configuración.
    def get_boton_configuracion(self):
        return self.__boton_configuracion
    
    ## @brief Devuelve las variables de configuración actual de la ventana de configuración.
    # @return [Array] Variables de la configuración.
    def get_variables_configuracion(self):
        return [self.__entrada_texto_n_tematicas.get(), self.__entrada_texto_probs.get(), 
                self.__entrada_texto_extracto.get(), self.__entrada_texto_tematica.get()]

    ## @brief Crea el menú de la barra superior de la aplicación.
    def crear_barra_menu(self):
        self.__barra_menu = tk.Menu(self)
        self.config(menu = self.__barra_menu)

        # Se crean los distintos menús.
        self.__menu_archivo = tk.Menu(self.__barra_menu, tearoff = False )
        self.__menu_opciones = tk.Menu(self.__barra_menu, tearoff = False )
        self.__menu_configuracion = tk.Menu(self.__barra_menu, tearoff = False )
        self.__menu_ayuda = tk.Menu(self.__barra_menu, tearoff = False )

        # Se añaden los distintos menús al menú global.
        self.__barra_menu.add_cascade(menu = self.__menu_archivo, label = "Archivo")
        self.__barra_menu.add_cascade(menu = self.__menu_opciones, label = "Opciones")
        self.__barra_menu.add_cascade(menu = self.__menu_configuracion, label = "Configuración")
        self.__barra_menu.add_cascade(menu = self.__menu_ayuda, label = "Ayuda")

    ## @brief Crea la ventana auxiliar del apartado de configuración.
    # @param frame_padre [Frame] Frame principal.
    # @param variables_configuracion [Array] Variables de la configuración actual del apartado de configuración.
    def crear_ventana_configuracion(self, frame_padre, variables_configuracion):
        self.__ventana_input = tk.Toplevel(frame_padre)
        self.__ventana_input.geometry("400x300")
        self.__ventana_input.title("Configuración de variables")
        self.__ventana_input.resizable(False, False)

        # Canva de fondo para Frame
        canva_fondo = tk.Canvas(self.ventana_input, bg = "#FFFFFF", width = 400, height = 300, highlightthickness = 1)
        canva_fondo.focus_set()
        canva_fondo.pack()

        # Adición de labels, inputs y botones
        label_n_tematicas = tk.Label(self.ventana_input, text = "Nº temáticas máximas a mostrar:", background = "#FFFFFF", font = ("Helvetica",9))
        label_n_probs = tk.Label(self.ventana_input, text = "Umbral diferencia de probs.:", background = "#FFFFFF", font = ("Helvetica",9))
        label_extracto = tk.Label(self.ventana_input, text = "Nombre de columna a extraer:", background = "#FFFFFF", font = ("Helvetica",9))
        label_tematica= tk.Label(self.ventana_input, text = "Nombre de columna de temática:", background = "#FFFFFF", font  = ("Helvetica",9))

        label_n_tematicas.pack()
        label_n_probs.pack()
        label_extracto.pack()
        label_tematica.pack()

        self.__entrada_texto_n_tematicas = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.__entrada_texto_probs = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.__entrada_texto_extracto = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.__entrada_texto_tematica = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))

        self.__entrada_texto_n_tematicas.insert(0, variables_configuracion[0])
        self.__entrada_texto_probs.insert(0, variables_configuracion[1])
        self.__entrada_texto_extracto.insert(0, variables_configuracion[2])
        self.__entrada_texto_tematica.insert(0, variables_configuracion[3])

        self.__entrada_texto_n_tematicas.pack()
        self.__entrada_texto_probs.pack()
        self.__entrada_texto_extracto.pack()
        self.__entrada_texto_tematica.pack()

        self.__boton_configuracion = Button(self.ventana_input, text = "Aplicar cambios", font = ("Helvetica", 9), background = "#E5CCFF")
        self.__boton_configuracion.pack()

        # Colocación de elementos
        label_n_tematicas.place(x = 30, y = 50)
        label_n_probs.place(x = 30, y = 100)
        label_extracto.place(x = 30, y = 150)
        label_tematica.place(x = 30, y = 200)
        self.__entrada_texto_n_tematicas.place(x = 230, y = 50)
        self.__entrada_texto_probs.place(x = 230, y = 100)
        self.__entrada_texto_extracto.place(x = 230, y = 150)
        self.__entrada_texto_tematica.place(x = 230, y = 200)
        self.__boton_configuracion.place(x = 150, y = 245)




