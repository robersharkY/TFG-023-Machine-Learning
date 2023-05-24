import tkinter as tk
from tkinter import ttk
from tkinter import *
from Vista.MainFrame import MainFrame

# Clase App: Clase donde se reunen todos los frames y características

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Elementos MainFrame
        self.title('Machine learning (TFG 2223-023)')
        self.geometry('500x400')
        self.resizable(False, False)
        self.crear_barra_menu()
        self.frame = MainFrame(self)
        icono_pequeno = tk.PhotoImage(False, file = "../resources/icono_PML.png")
        self.iconphoto(True, icono_pequeno)

        # Elementos ventana input
        self.ventana_input = None
        self.boton_variables = Button(self.ventana_input, text = "Aplicar cambios", font = ("Helvetica",9), background = "#E5CCFF")
        self.entrada_texto_tematicas = None
        self.entrada_texto_probs = None
        self.entrada_texto_extracto = None
        self.entrada_texto_tematicas = None

    def iniciar_frame(self):
        self.mainloop()

    def get_frame(self):
        return self

    def get_menu_archivo(self):
        return self.menu_archivo
    
    def get_menu_opciones(self):
        return self.menu_opciones

    def get_menu_configuracion(self):
        return self.menu_configuracion
    
    def get_menu_ayuda(self):
        return self.menu_ayuda
    
    def get_combobox_algoritmo(self):
        return self.frame.combo_algoritmo
    
    def get_combobox_bag(self):
        return self.frame.combo_bag

    def get_boton_variables(self):
        return self.boton_variables
    
    def get_array_variables(self):
        return [self.entrada_texto_n_tematicas.get(), self.entrada_texto_probs.get(), self.entrada_texto_extracto.get(), 
                self.entrada_texto_tematica.get()]

    # Crea menú del MainFrame
    def crear_barra_menu(self):
        self.barra_menu = tk.Menu(self)
        self.config(menu = self.barra_menu)
        self.menu_archivo = tk.Menu(self.barra_menu, tearoff = False )
        self.menu_configuracion = tk.Menu(self.barra_menu, tearoff = False )
        self.menu_opciones = tk.Menu(self.barra_menu, tearoff = False )
        self.menu_ayuda = tk.Menu(self.barra_menu, tearoff = False )
        self.barra_menu.add_cascade(menu=self.menu_archivo, label="Archivo")
        self.barra_menu.add_cascade(menu=self.menu_opciones, label="Opciones")
        self.barra_menu.add_cascade(menu=self.menu_configuracion, label="Configuración")
        self.barra_menu.add_cascade(menu=self.menu_ayuda, label="Ayuda")

    # Crea ventana para modificar datos
    def abrir_ventana_dialogo(self, frame_padre, array_variables):
        self.ventana_input = tk.Toplevel(frame_padre)
        self.ventana_input.geometry("400x300")
        self.ventana_input.title("Configuración de variables")
        self.ventana_input.resizable(False,False)

        # Canva de fondo para Frame
        canva_fondo = tk.Canvas(self.ventana_input, bg = "#FFFFFF", width = 400, height = 300, highlightthickness = 1)
        canva_fondo.focus_set()
        canva_fondo.pack()

        # Adición de labels, inputs y botones
        label_n_tematicas = tk.Label(self.ventana_input, text = "Nº temáticas máximas a mostrar:", background = "#FFFFFF", font = ("Helvetica",9))
        label_n_probs = tk.Label(self.ventana_input, text = "Umbral diferencia de probs.:", background = "#FFFFFF", font = ("Helvetica",9))
        label_extracto = tk.Label(self.ventana_input, text = "Nombre de columna a extraer:", background = "#FFFFFF", font = ("Helvetica",9))
        label_tematica= tk.Label(self.ventana_input, text = "Nombre de columna de temática:", background = "#FFFFFF", font  =("Helvetica",9))

        label_n_tematicas.pack()
        label_n_probs.pack()
        label_extracto.pack()
        label_tematica.pack()

        self.entrada_texto_n_tematicas = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.entrada_texto_probs = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.entrada_texto_extracto = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))
        self.entrada_texto_tematica = tk.Entry(self.ventana_input, background = "#E5CCFF", font = ("Helvetica",9))

        self.entrada_texto_n_tematicas.insert(0, array_variables[0])
        self.entrada_texto_probs.insert(0, array_variables[1])
        self.entrada_texto_extracto.insert(0, array_variables[2])
        self.entrada_texto_tematica.insert(0, array_variables[3])

        self.entrada_texto_n_tematicas.pack()
        self.entrada_texto_probs.pack()
        self.entrada_texto_extracto.pack()
        self.entrada_texto_tematica.pack()

        self.boton_variables = Button(self.ventana_input, text = "Aplicar cambios", font = ("Helvetica",9), background = "#E5CCFF")
        self.boton_variables.pack()

        # Colocación de elementos
        label_n_tematicas.place(x=30,y=50)
        label_n_probs.place(x=30,y=100)
        label_extracto.place(x=30,y=150)
        label_tematica.place(x=30,y=200)
        self.entrada_texto_n_tematicas.place(x=230,y=50)
        self.entrada_texto_probs.place(x=230,y=100)
        self.entrada_texto_extracto.place(x=230,y=150)
        self.entrada_texto_tematica.place(x=230,y=200)
        self.boton_variables.place(x=150,y=245)




