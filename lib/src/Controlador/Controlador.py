## @package Controlador
# @brief Clase Controlador, interfaz que une modelo y vista, la cual maneja toda la aplicación.
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

    ## @brief Constructor de Controlador.
    def __init__(self):
        ## Variable privada, representa la vista del programa.
        self.__vista = Vista()

        ## Variable privada, representa el modelo del programa.
        self.__modelo = Modelo()

        ## Variable privada, representa el botón de "Aplicar cambios" del apartado de "Configuración".
        self.__boton_configuracion = []

    ## @brief Inicia la aplicación.
    def iniciar(self):
        self.anadir_funcionalidades() # Inicia todo lo necesario antes de empezar.
        self.__vista.iniciar_frame() # Muestra el frame.
    
    ## @brief Añade las funcionalidades a cada uno de los botones.
    def anadir_funcionalidades(self):
        # Almacena en variables los elementos de la vista que tendrán funcionalidad
        self.__boton_configuracion = self.__vista.get_boton_configuracion()
        menu_archivo = self.__vista.get_menu_archivo()
        menu_opciones = self.__vista.get_menu_opciones()
        menu_configuracion = self.__vista.get_menu_configuracion()
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

        # Se añaden las funcionalidades a cada uno de los elementos
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
            command = lambda: self.mostrar_tabla(self.__modelo.get_dataset_pruebas(), 1000, 500)) 

        menu_opciones.add_command(    
            label = "Mostrar conjunto de entrenamiento",
            command = lambda: self.mostrar_tabla(self.__modelo.get_dataset_entrenamiento(), 1000, 800))
            
        menu_configuracion.add_command(    
            label = "Configurar variables",
            command = self.realizar_configuracion)

        menu_ayuda.add_command(    
            label = "Información",
            command = lambda: self.__vista.mostrar_ventana_mensaje(texto_ayuda))

        combo_bag.bind("<<ComboboxSelected>>", lambda _ :self.__modelo.seleccionar_bag_words(combo_bag.get()))
        combo_algoritmo.bind("<<ComboboxSelected>>", lambda _ :self.__modelo.seleccionar_algoritmo(combo_algoritmo.get()))
    
    ## @brief Permite seleccionar el archivo del conjunto de test.
    def seleccionar_archivo_test(self):
        tipos_archivo = ( ('CSV', '*.csv'), ('All files', '*.*'))
        direccion_archivo = fd.askopenfilenames(title = 'Abrir archivo', filetypes = tipos_archivo)

        if len(direccion_archivo) == 0: # Si quita el seleccionador.
            pass
        elif len(direccion_archivo) > 1:
            self.__vista.mostrar_ventana_mensaje("Seleccione solo 1 archivo") # Si selecciona más de un archivo.
        else:
            self.__modelo.leer_dataset_prueba(direccion_archivo[0]) # Si selecciona un archivo.

    ## @brief Permite seleccionar el archivo del conjunto de entrenamiento.
    def seleccionar_archivo_entrenamiento(self):
        tipos_archivo = (('CSV', '*.csv'), ('All files', '*.*'))
        direccion_archivo = fd.askopenfilenames(title = 'Abrir archivo', filetypes = tipos_archivo)

        if len(direccion_archivo) == 0: # Si quita el seleccionador.
            pass
        elif len(direccion_archivo) > 1:
            self.__vista.mostrar_ventana_mensaje("Seleccione solo 1 archivo") # Si selecciona más de un archivo.
        else:
            self.__modelo.leer_dataset_entrenamiento(direccion_archivo[0]) # Si selecciona un archivo.

    ## @brief Se encarga de abrir la ventana de configuración y actualizar las variables.
    def realizar_configuracion(self):
        self.__vista.mostrar_ventana_configuracion(self.__modelo.get_variables_configuracion())
        self.__boton_boton_configuracion = self.__vista.get_boton_configuracion() # Se implementa botón de "Aplicar cambios"
        self.__boton_boton_configuracion.configure(command = lambda: self.__modelo.set_variables_configuracion(self.__vista.get_variables_configuracion(), self.__vista))
    
    ## @brief Muestra una ventana con formato de dataset, con la información dada en los parámetros.
    # @param dataset [Panda dataset] Dataset a mostrar.
    # @param anchura [Int] Anchura de la ventana.
    # @param max_anchura_celda [Int] Anchura máxima de las celdas.
    def mostrar_tabla(self, dataset, anchura, max_anchura_celda):
        ventana_tabla = tk.Tk()
        frame = tk.Frame(ventana_tabla)
        frame.pack(fill = 'both', expand = True)
        frame.pack(fill = 'x', expand = True) 
        frame.pack(fill = 'y', expand = True)
        pt = Table(frame, dataframe = dataset, width = 1000, maxcellwidth = 800)
        pt.show()
        ventana_tabla.mainloop()

    ## @brief LLama al entrenamiento del modelo y controla los errores
    def entrenamiento_datasets(self):
        # Si algún conjunto de ambos esta vacío.
        if self.__modelo.get_dataset_entrenamiento() is None or self.__modelo.get_dataset_pruebas() is None:
            self.__vista.mostrar_ventana_mensaje("Seleccione antes un archivo de entrenamiento y pruebas")
        else: # Si ningún conjunto esta vacío.
            self.__modelo.limpiar_datasets()
            self.__vista.mostrar_ventana_mensaje(self.__modelo.entrenamiento())

    ## @brief LLama a la clasificación del modelo y controla los errores.
    def clasificar(self):
        # Si algún modelo de ambos esta vacío.
        if self.__modelo.get_dataset_entrenamiento() is None or self.__modelo.get_dataset_pruebas() is None:
            self.__vista.mostrar_ventana_mensaje("Seleccione antes un archivo de entrenamiento y pruebas")
        elif self.__modelo.estan_limpios_datasets() == False: # Si alguna iniciativa no ha sido procesada.
            self.__vista.mostrar_ventana_mensaje("Realice antes el entrenamiento necesario")
        else: # Si ninguna esta vacía y todas las iniciativas han sido procesadas.
            self.__modelo.clasificar()
            self.mostrar_tabla(self.__modelo.get_dataset_pruebas(), 1000, 500)
    
    
            

        

