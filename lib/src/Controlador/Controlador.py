## @package Controlador
# @brief Clase Vista, interfaz que une modelo y vista, la cual maneja toda la aplicación.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023
import tkinter as tk
from tkinter import filedialog as fd
from pandastable import Table, TableModel
from pandas import pandas
from Vista.Vista import Vista
from Modelo.Modelo import Modelo

class Controlador:

    def __init__(self):
        self.__vista = Vista()
        self.__modelo = Modelo()
        self.boton_variables = self.__vista.get_boton_variables()

        menu_archivo = self.__vista.get_menu_archivo()
        menu_configuracion = self.__vista.get_menu_configuracion()
        menu_opciones = self.__vista.get_menu_opciones()
        menu_ayuda = self.__vista.get_menu_ayuda()
        combo_bag = self.__vista.get_combobox_bag()
        combo_algoritmo = self.__vista.get_combobox_algoritmo()
        texto_ayuda = (f"TFG realizado por el alumno Roberto Carlos García Cruz para la ULL\n\n"
                    "Para hacer un uso correcto de la app se debe hacer lo siguiente:\n\n" 
                    "1º Primero se debe abrir un archivo de pruebas y otro de entrenamiento (Archivo > Abrir conjunto...)\n\n"
                    "2º Posteriormente se debe entrenar antes de realizar las clasificaciones en el archivo de pruebas (Opciones > Entrenar modelo)\n\n"
                    "3º Finalmente se debe realizar las clasificaciones (Opciones > Realizar clasificaciones)\n\n"
                    "Cada vez que se cambie el algoritmo, el bag of words o cualquiera de los archivos, "
                    "se deberá realizar de nuevo los pasos 2 y 3 anteriormente comentados")

        menu_archivo.add_command(    
            label = "Abrir conjunto de pruebas",
            command = self.seleccionar_archivo_test)

        menu_archivo.add_command(    
            label = "Abrir conjunto de entrenamiento",
            command = self.seleccionar_archivo_entrenamiento)

        menu_opciones.add_command(    
            label = "Entrenar modelo",
            command = self.entrenamiento_datasets)

        menu_opciones.add_command(    
            label = "Realizar clasificaciones",
            command = self.clasificar)

        menu_opciones.add_command(    
            label = "Mostrar conjunto de pruebas",
            command = lambda: self.mostrar_tabla(self.__modelo.get_datos_pruebas(), 1000, 500)) 

        menu_opciones.add_command(    
            label = "Mostrar conjunto de entrenamiento",
            command = lambda: self.mostrar_tabla(self.__modelo.get_datos_entrenamiento(), 1000, 800))
            
        menu_configuracion.add_command(    
            label = "Configurar variables",
            command = self.definir_variables)

        menu_ayuda.add_command(    
            label = "Información",
            command = lambda: self.__vista.mostrar_ventana_mensaje(texto_ayuda))

        combo_bag.bind("<<ComboboxSelected>>", lambda _ :self.seleccionar_bag_words(combo_bag.get()))
        combo_algoritmo.bind("<<ComboboxSelected>>", lambda _ :self.seleccionar_algoritmo(combo_algoritmo.get()))

    def iniciar(self):
        self.__vista.iniciar()
    
    def seleccionar_archivo_test(self):
        filetypes = ( ('text files', '*.csv'), ('All files', '*.*'))
        direccion_archivo = fd.askopenfilenames(title = 'Abrir archivo', filetypes = filetypes)

        if len(direccion_archivo) == 0:
            pass
        elif len(direccion_archivo) > 1:
            self.__vista.mostrar_ventana_mensaje("Seleccione solo 1 archivo")
        else:
            self.__modelo.leer_dataset_prueba(direccion_archivo[0])

    def seleccionar_archivo_entrenamiento(self):
        filetypes = (('text files', '*.csv'), ('All files', '*.*'))
        direccion_archivo = fd.askopenfilenames(title = 'Abrir archivo', filetypes = filetypes)

        if len(direccion_archivo) == 0:
            pass
        elif len(direccion_archivo) > 1:
            self.__vista.mostrar_ventana_mensaje("Seleccione solo 1 archivo")
        else:
            self.__modelo.leer_dataset_entrenamiento(direccion_archivo[0])
    
    def definir_variables(self):
        self.__vista.mostrar_ventana_input(self.__modelo.get_array_variables())
        self.boton_variables = self.__vista.get_boton_variables()
        self.boton_variables.configure(command = self.anadir_variables)

    def anadir_variables(self):
        self.__modelo.set_variables(self.__vista.get_variables(),self.vista_)
    
    def seleccionar_bag_words(self, frase):
        self.__modelo.seleccionar_bag_words(frase)

    def seleccionar_algoritmo(self, frase):
        self.__modelo.seleccionar_algoritmo(frase)
        
    def mostrar_tabla(self, dataset, anchura, max_anchura_celda):
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack(fill = 'both', expand = True)
        frame.pack(fill = 'x', expand = True) 
        frame.pack(fill = 'y', expand = True)
        pt = Table(frame, dataframe = dataset, width = 1000, maxcellwidth = 800)
        pt.show()
        root.mainloop()

    def entrenamiento_datasets(self):
        # Si algún modelo de ambos esta vacío
        if self.__modelo.get_datos_entrenamiento() is None or self.__modelo.get_datos_pruebas() is None:
            self.__vista.mostrar_ventana_mensaje("Seleccione antes un archivo de entrenamiento y pruebas")
        else:
            self.__modelo.limpiar_datasets()
            self.__vista.mostrar_ventana_mensaje(self.__modelo.entrenamiento())


    def clasificar(self):
        # Si algún modelo de ambos esta vacío
        if self.__modelo.get_datos_entrenamiento() is None or self.__modelo.get_datos_pruebas() is None:
            self.__vista.mostrar_ventana_mensaje("Seleccione antes un archivo de entrenamiento y pruebas")
        elif self.__modelo.estan_limpios_datasets() == False:
            self.__vista.mostrar_ventana_mensaje("Realice antes el entrenamiento necesario")
        else:
            self.__modelo.clasificar()
            self.mostrar_tabla(self.__modelo.get_datos_pruebas(), 1000, 500)
    
    
            

        

