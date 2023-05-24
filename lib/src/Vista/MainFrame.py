from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

# Clase MainFrame: Contenido del frame principal

class MainFrame(ttk.Frame):

    def __init__(self,container):
        super().__init__(container)

        # Canva de fondo para Frame
        canva_fondo = Canvas(self,bg = "#FFFFFF", width = 500, height = 400, highlightthickness = 1)
        canva_fondo.focus_set()
        canva_fondo.pack()

        # Cambio de estilo en combobox
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

        # Adición de imagen en MainFrame
        self.imagen_ull = Image.open("../resources/ull-nuevo-logo.jpg")
        self.imagen_ull = self.imagen_ull.resize((200,100))
        self.img = ImageTk.PhotoImage(self.imagen_ull)
        self.label_imagen = ttk.Label(self, image = self.img, background = "#FFFFFF")
        self.label_imagen.image = self.img
        self.label_imagen.place(x=155,y=175)

        # Adición de labels y combobox
        label_seleccion_bag = ttk.Label(self, text = "Selecciona bag of words:", font = ("Helvetica",11), background = "#FFFFFF")
        self.combo_bag = ttk.Combobox(state = "readonly", values = ["TF-IDF", "CV"], font = ("Helvetica",10), style = "TCombobox")
        self.combo_bag.set("TF-IDF")

        label_seleccion_algoritmo = ttk.Label(self,text = "Selecciona algoritmo:",font=("Helvetica",11), background = "#FFFFFF")
        self.combo_algoritmo = ttk.Combobox(
            state = "readonly",
            values = ["SVC-Lineal SVC", "SVC-SVR", "SVC-Nu SVC", "TR-Decision Tree", "TR-Extra Tree","NB-Multinomial", 
            "NB-Gaussian", "NB-Bernoulli", "ENS-Random Forest", "ENS-Gradient Boost", "ENS-Ada Boost", "KNN-K-Neighbors", 
            "NEU-MLP","DIS-Quadratic Discriminant", "DIS-Linear Discriminant", "LM-SGD", "LM-Regresión logística"], 
            font = ("Helvetica",10), background = "#E5CCFF" )
        self.combo_algoritmo.set("SVC-SVC Lineal")

        # Colocación de elementos
        label_seleccion_bag.place(x=173,y=30)
        self.combo_bag.place(x=175,y=55)
        label_seleccion_algoritmo.place(x=185,y=100)
        self.combo_algoritmo.place(x=175,y=125)
        self.pack()
