## @package Modelo
# @brief Clase Modelo, interfaz que une todo lo comprendido de clases de datos y manejo de los mismos para ser usado en el controlador.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from Modelo.Limpieza.Procesador import Procesador
from Modelo.Datos.Dataset import Dataset
from Modelo.Clasificacion.Clasificador import Clasificador
from Modelo.Clasificacion.ClasificadorML import ClasificadorML
from Modelo.Clasificacion.ClasificadorAR import ClasificadorAR
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier,ExtraTreeClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression,LinearRegression,SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis,LinearDiscriminantAnalysis
from Vista.Vista import Vista
import re

class Modelo:

    ## @brief Constructor de Modelo.
    def __init__(self):
        ## Variable privada, dataset para realizar los entrenamientos.
        self.__dataset_entrenamiento = Dataset()

        ## Variable privada, dataset para realizar las clasificaciones.
        self.__dataset_prueba = Dataset()

        ## Variable privada, objeto para procesar el lenguaje natural.
        self.__procesador = Procesador()

        ## Variable privada, objeto para realizar todas las funcionalidades de Machine Learning
        self.__clasificador = ClasificadorML()

        ## Variable privada, cadena que indica de que columna se obtendrán las iniciativas.
        self.__columna_extracto = "EXTRACTO"

        ## Variable privada, cadena que indica de que columna se obtendrán y colocarán los resultados y temáticas.
        self.__columna_tematica = "TEMATICA"
    
    ## @brief Lee los datos de un dataset para almacenarlos en el conjunto de entrenamiento.
    # @param direccion_entrenamiento [String] Dirección del dataset de entrenamiento.
    def leer_dataset_entrenamiento(self, direccion_entrenamiento):
        self.__dataset_entrenamiento = Dataset()
        self.__dataset_entrenamiento.leer_datos(direccion_entrenamiento)
    
    ## @brief Lee los datos de un dataset para almacenarlos en el conjunto de pruebas.
    # @param direccion_prueba [String] Dirección del dataset de pruebas.
    def leer_dataset_prueba(self, direccion_prueba):
        self.__dataset_prueba = Dataset()
        self.__dataset_prueba.leer_datos(direccion_prueba)
    
    ## @brief Selecciona el tipo bolsa de palabras deseada y updatea la variable "self.__clasificador".
    # @param tipo [String] Nombre del tipo de bolsa de palabras, los nombres son cogidos del texto de los botones.
    def seleccionar_bag_words(self, tipo):
        if tipo == "CV":
            self.__clasificador.set_bag_words(CountVectorizer(binary = True))
        else: # Para TF-IDF
            self.__clasificador.set_bag_words(TfidfVectorizer(binary = True))

    ## @brief Selecciona el algoritmo deseado y updatea la variable "self.__clasificador".
    # @param tipo [String] Nombre del tipo de algoritmo, los nombres son cogidos del texto de los botones.
    def seleccionar_algoritmo(self, tipo):
        if tipo == "SVC-Lineal SVC":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(SVC(kernel='linear',probability=True))
        elif tipo == "SVC-SVR":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(SVC(kernel='rbf',probability=True))
        elif tipo == "SVC-Nu SVC":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(NuSVC(kernel='linear',probability=True))
        elif tipo == "TR-Decision Tree":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(DecisionTreeClassifier())
        elif tipo == "TR-Extra Tree":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(ExtraTreeClassifier())
        elif tipo == "NB-Multinomial":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(MultinomialNB())
        elif tipo == "NB-Gaussian":
            self.__clasificador = ClasificadorAR()
            self.__clasificador.set_modelo(GaussianNB())
        elif tipo == "NB-Bernoulli":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(BernoulliNB())
        elif tipo == "ENS-Random Forest":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(RandomForestClassifier())
        elif tipo == "ENS-Gradient Boost":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(GradientBoostingClassifier())
        elif tipo == "ENS-Ada Boost":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(AdaBoostClassifier())
        elif tipo == "KNN-K-Neighbors":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(KNeighborsClassifier(n_neighbors = 4))
        elif tipo == "NEU-MLP":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(MLPClassifier())
        elif tipo == "DIS-Quadratic Discriminant":
            self.__clasificador = ClasificadorAR()
            self.__clasificador.set_modelo(QuadraticDiscriminantAnalysis())
        elif tipo == "DIS-Linear Discriminant":
            self.__clasificador = ClasificadorAR()
            self.__clasificador.set_modelo(LinearDiscriminantAnalysis())
        elif tipo == "LM-SGD":
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(SGDClassifier(loss = 'log_loss'))
        else: # Para Logistic Regression
            self.__clasificador = ClasificadorML()
            self.__clasificador.set_modelo(LogisticRegression())


    ## @brief Devuelve el dataset de entrenamiento.
    # @return [Panda Dataset] Dataset para el entrenamiento de los algoritmos.
    def get_dataset_entrenamiento(self):
        return self.__dataset_entrenamiento.get_datos()
    
    ## @brief Devuelve el dataset de pruebas.
    # @return [Panda Dataset] Dataset para el la clasificación de iniciativas.
    def get_dataset_pruebas(self):
        return self.__dataset_prueba.get_datos()
    
    ## @brief Devuelve las variables de la configuración del programa.
    # @return [Array] Variables de configuración del programa.
    def get_variables_configuracion(self):
        return [self.__clasificador.get_n_tematicas(), self.__clasificador.get_alfa(), 
                self.__columna_extracto, self.__columna_tematica]

    ## @brief Verifica que se cumplan con todos los sets de la configuración de variables.
    # @param variables_config [Array] Array con las variables de configuración.
    # @param vista [Vista] Vista del programa que nos ayudará a lanzar ventanas.
    def set_variables_configuracion(self, variables_config, vista):
        conteo = []
        conteo.append(self.set_int_n_tematicas(variables_config[0], vista))
        conteo.append(self.set_float_alfa(variables_config[1], vista))  
        conteo.append(self.set_cadena(self.__columna_extracto, variables_config[2], "Debe introducir un nombre de columna de extracto.", vista))
        conteo.append(self.set_cadena(self.__columna_tematica, variables_config[3], "Debe introducir un nombre de columna de temática.", vista))
        if all(conteo): # Si todos los sets son == True
            vista.mostrar_ventana_mensaje("Se han actualizado todos los datos correctamente.")

    ## @brief Verifica que el nº de temáticas cumpla con ciertos requisitos.
    # @param variable [Int] Entero a examinar que cumple con los requisitos.
    # @param vista [Vista] Vista del programa que nos ayudará a lanzar ventanas.
    # @return [Boolean] Devuelve True si ha sido capaz de actualizar el dato y False si no ha sido capaz de actualizarlo.
    def set_int_n_tematicas(self, variable, vista):
        if variable.isnumeric() and variable != "": # Si la cadena no es vacía y es entero.
            numero = int(variable)
            if numero < 1 or numero > 10: # Si el número es menor a 1 o si es mayor a 10.
                print(numero)
                vista.mostrar_ventana_mensaje("El número de temáticas debe ser entre 1 y 10.")
                return False
            else: # Si el número está entre 1 y 10.
                self.__clasificador.set_n_tematicas(numero)
                return True
        else: # Si la cadena es vacía y no es entero.
            vista.mostrar_ventana_mensaje("Debe introducir un dato entero nº de temáticas.")
            return False
    
    ## @brief Verifica que el alfa de probabilidades cumpla con ciertos requisitos.
    # @param variable [Float] Flotante a examinar que cumple con los requisitos.
    # @param vista [Vista] Vista del programa que nos ayudará a lanzar ventanas.
    # @return [Boolean] Devuelve True si ha sido capaz de actualizar el dato y False si no ha sido capaz de actualizarlo.
    def set_float_alfa(self, variable, vista):
        if re.match(r'^-?\d+(?:\.\d+)$', variable) and variable != "": # Si la cadena no es vacía y tiene punto.
            numero = float(variable)
            if numero <= 0 or numero >= 1: # Si el número es menor o igual a 0 o si es mayor o igual a 1.
                vista.mostrar_ventana_mensaje("El alfa debe ser entre 0 y 1, sin ser estos 0 y 1.")
                return False
            else: # Si el número está entre 0 y 1.
                self.__clasificador.set_alfa(numero)
                return True
        else: # Si la cadena es vacía y no tiene punto.
            vista.mostrar_ventana_mensaje("Debe introducir un dato float en umbral.")
            return False
    
    ## @brief Verifica que no sea una cadena vacía.
    # @param columna [String] variable que contiene el nombre de la columna. 
    # @param variable [String] Cadena a examinar que cumple con los requisitos.
    # @param mensaje [String] Cadena con mensaje de error por si no cumple los requisitos.
    # @param vista [Vista] Vista del programa que nos ayudará a lanzar ventanas.
    # @return [Boolean] Devuelve True si ha sido capaz de actualizar el dato y False si no ha sido capaz de actualizarlo.
    def set_cadena(self, columna, variable, mensaje, vista):
        if variable != "": # Si la cadena no es vacía.
            columna = variable
            return True
        else: # Si la cadena es vacía.
            vista.mostrar_ventana_mensaje(mensaje)
            return False

    ## @brief Verifica la existencia y crea la columna donde se colocarán los resultados.
    def verificar_columna_resultados(self):
        dataset = self.__dataset_prueba.get_datos()
        if self.__columna_tematica not in dataset: # Si no existe dicha columna.
            dataset[self.__columna_tematica] = None # Se crea una columna vacía.
        self.__dataset_prueba.set_datos(dataset)
    
    ## @brief Verifica si hay alguna iniciativa de los datasets que no haya sido procesada.
    def estan_limpios_datasets(self):
        for index, row in self.__dataset_entrenamiento.get_datos().iterrows():
            if not isinstance(row[self.__columna_extracto], list): # Si alguna iniciativa no es de tipo "list".
                return False
        for index, row in self.__dataset_prueba.get_datos().iterrows():
            if not isinstance(row[self.__columna_extracto], list): # Si alguna iniciativa no es de tipo "list".
                return False
        return True
    
    ## @brief Realiza la limpieza del lenguaje natural de cada una de las iniciativas, obteniendo palabras clave.
    # @param dataset [Dataset] Dataset a limpiar iniciativas.
    def limpiar_sentencias(self, dataset):
        for index, row in dataset.get_datos().iterrows():
            if not isinstance(row[self.__columna_extracto], list):
                tokens = self.__procesador.eliminar_palabras_vacias(row[self.__columna_extracto]) # Tokeniza, elimina puntuaciones y palabras vacías.
                tokens = self.__procesador.eliminar_duplicados(tokens) # Elimina palabras repetidas.
                tokens = self.__procesador.lematizar(tokens) # Lematiza cada token.
                dataset.get_datos().at[index, self.__columna_extracto] = tokens
    
    ## @brief Realiza el procesamiento del lenguaje de las iniciativas de ambos archivos.
    def limpiar_datasets(self):
        self.limpiar_sentencias(self.__dataset_entrenamiento)
        self.limpiar_sentencias(self.__dataset_prueba)

    ## @brief Realiza el entrenamiento del conjunto de entrenamiento.
    # @return [String] Devuelve una cadena que indica la precisión del entrenamiento.
    def entrenamiento(self):
        return self.__clasificador.entrenar_modelo(self.__dataset_entrenamiento.get_datos(), self.__columna_extracto, self.__columna_tematica)

    ## @brief Realiza la clasificación de las iniciativas del conjunto de pruebas.
    def clasificar(self):
        self.verificar_columna_resultados() # Se verifica si esta creada la columna para poner las temáticas.
        predicciones = self.__clasificador.clasificar_sentencias(self.__dataset_prueba.get_datos(), self.__columna_extracto)

        for index, row in self.__dataset_prueba.get_datos().iterrows():
            #En la columna temática creada, añade los arrays de temáticas eliminando los corchetes.
           self.__dataset_prueba.get_datos().at[index, self.__columna_tematica] = ', '.join(str(item) for item in predicciones[index])

        
        
        
