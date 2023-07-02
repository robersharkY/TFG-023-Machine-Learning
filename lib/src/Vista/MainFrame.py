## @package Vista
# @brief Clase MainFrame, contenedor del frame principal del programa.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os
import sys


class MainFrame(ttk.Frame):
    
    ## @brief Constructor de Mainframe, en el se construye toda la interfaz de usuario del frame principal
    # @param container [Container] Container del frame.
    def __init__(self, container):
        super().__init__(container)

        # Canva de fondo para frame.
        canva_fondo = Canvas(self,bg = "#FFFFFF", width = 500, height = 400, highlightthickness = 1)
        canva_fondo.focus_set()
        canva_fondo.pack()

        # Cambio de estilo en combobox.
        combobox_estilo = ttk.Style()
        combobox_estilo.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'fieldbackground': '#CCCCFF',
                                       'selectbackground': '#CCCCFF',
                                       'selectforeground': '#000000'
                                       }}})
        combobox_estilo.theme_use("combostyle") 
        self.option_add("*TCombobox*Listbox*Background", '#CCCCFF')

        # Adición de imagen en MainFrame.
        ruta = os.path.dirname(os.path.abspath(os.getcwd()))
        #imagen = os.path.join(ruta, "..\\..\\resources", "ull-nuevo-logo.jpg")
        imagen = self.resource_path("..\\..\\..\\resources\\ull-nuevo-logo.jpg")
        self.__imagen_ull = Image.open(imagen)
        self.__imagen_ull = self.__imagen_ull.resize((200, 100))
        self.__img = ImageTk.PhotoImage(self.__imagen_ull)
        self.__label_imagen = ttk.Label(self, image = self.__img, background = "#FFFFFF")
        self.__label_imagen.image = self.__img
        self.__label_imagen.place(x = 155, y = 175)

        # Adición de labels y combobox.
        label_seleccion_bag = ttk.Label(self, text = "Selecciona bag of words:", font = ("Helvetica",11), background = "#FFFFFF")
        self.__combo_bag = ttk.Combobox(state = "readonly", values = ["TF-IDF", "CV"], font = ("Helvetica",10), style = "TCombobox")
        self.__combo_bag.set("TF-IDF")

        label_seleccion_algoritmo = ttk.Label(self, text = "Selecciona algoritmo:", font=("Helvetica",11), background = "#FFFFFF")
        self.__combo_algoritmo = ttk.Combobox(
            state = "readonly",
            values = ["SVC-Lineal SVC", "SVC-SVR", "TR-Decision Tree", "TR-Extra Tree","NB-Multinomial", "NB-Gaussian", 
            "NB-Bernoulli", "ENS-Random Forest", "ENS-Gradient Boost", "ENS-Ada Boost", "KNN-K-Neighbors","KNN-Nearest Centroid", 
            "NEU-MLP","DIS-Quadratic Discriminant", "DIS-Linear Discriminant", "LM-SGD", "LM-Logistic Regression"], 
            font = ("Helvetica", 10), background = "#E5CCFF" )
        self.__combo_algoritmo.set("SVC-SVC Lineal")

        # Colocación de elementos.
        label_seleccion_bag.place(x = 173, y = 30)
        self.__combo_bag.place(x = 175, y = 55)
        label_seleccion_algoritmo.place(x = 185, y = 100)
        self.__combo_algoritmo.place(x = 175, y = 125)
        self.pack()

    ## @brief Devuelve el combo de los algoritmos.
    # @return [ComboBox] Combo de los algoritmos a elegir.
    def get_combobox_algoritmo(self):
        return self.__combo_algoritmo

    ## @brief Devuelve el combo de las bolsas de palabras.
    # @return [ComboBox] Combo de las bolsas de palabras a elegir.
    def get_combobox_bag(self):
        return self.__combo_bag

    ## @brief Método necesario para que tanto el generador de exe como el programa cargue las imágenes.
    # @param relative_path [String] ruta relativa del archivo.
    # @return [Image] Imagen cargada de dicha ruta.
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(__file__)

        return os.path.join(base_path, relative_path)
