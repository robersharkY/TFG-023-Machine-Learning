## @package Clasificacion
# @brief Clase Clasificador, contiene todos los métodos y variables necesarias de Machine Learning por la librería Scikit-Learn.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

class Clasificador:

    ## @brief Constructor de Clasificador.
    def __init__(self):
        ## Variable protected[Algoritmo ML], contiene el modelo de algoritmo de Machine Learning. 
        self._modelo = SVC(kernel = "linear", probability = True, decision_function_shape = "ovo")

        ## Variable privada[Bag of words], contiene la bolsa de palabras.
        self.__bag_words = TfidfVectorizer(binary = True)

        ## Variable privada[Float], contiene el umbral de probabilidad para hallar temáticas cercanas.
        self.__alfa = 0.05

        ## Variable privada[Int], contiene el número de temáticas máxima a mostrar.
        self.__n_tematicas = 2

    ## @brief Devuelve el nº de temáticas máximo a mostrar.
    # @return [Int] Número de temáticas máximo a mostrar.
    def get_n_tematicas(self):
        return self.__n_tematicas

    ## @brief Actualiza el nº de temáticas máximo a mostrar.
    # @param n_tematicas [Int] Número de temáticas máximo a mostrar, modifica la variable "self.__n_tematicas".
    def set_n_tematicas(self, n_tematicas):
        self.__n_tematicas = n_tematicas

    ## @brief Devuelve el umbral de probabilidad para hallar temáticas cercanas.
    # @return [Float] Umbral de probabilidad para hallar temáticas cercanas.
    def get_alfa(self):
        return self.__alfa
    
    ## @brief Actualiza el umbral de probabilidad para hallar temáticas cercanas.
    # @param alfa [Int] Umbral de probabilidad para hallar temáticas cercanas, modifica la variable "self.__alfa".
    def set_alfa(self, alfa):
        self.__alfa = alfa
    
    ## @brief Devuelve la bolsa de palabras.
    # @return [Bag of words] Bolsa de palabras.  
    def get_bag_words(self):
        return self.__bag_words
    
    ## @brief Actualiza la bolsa de palabras.
    # @param bag_words [Bag of words] Bolsa de palabras, modifica la variable "self.__bag_words".
    def set_bag_words(self, bag_words):
        self.__bag_words = bag_words

    ## @brief Devuelve el algoritmo actual.
    # @return [Algoritmo ML] Algoritmo actual del clasificador. 
    def get_modelo(self):
        return self._modelo
    
    ## @brief Actualiza el algoritmo actual.
    # @param modelo [Algoritmo ML] Algoritmo a actualizar, modifica la variable "self._modelo".
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    ## @brief Realiza el entrenamiento para preparar y obtener los resultados del algoritmo.
    # @param dataset [Panda Dataset] Dataset del conjunto de entrenamiento.
    # @param columna_extracto [String] Columna de donde se obtienen los extractos.
    # @param columna_tematica [String] Columna de donde se obtienen las temáticas.
    # @return [String] Cadena que indica los resultados del algoritmo.
    def entrenar_modelo(self, dataset, columna_extracto, columna_tematica): 
        #Se obtienen las columnas.
        extractos = dataset[columna_extracto].astype(str)
        labels = dataset[columna_tematica].astype(str)

        #Se realiza el entrenamiento con 20% de test y 80% de training.
        extractos_train, extractos_test, labels_train, labels_test = train_test_split(extractos, labels, test_size = 0.20)
        extractos_train_bag = self.__bag_words.fit_transform(extractos_train)
        extractos_test_bag = self.__bag_words.transform(extractos_test)
        self.entrenamiento(extractos_train_bag, labels_train)
        predicciones = self.crear_predicciones(extractos_test_bag)

        #Se obtiene las variables necesarias para medir el desempeño del algoritmo. 
        accuracy = accuracy_score(labels_test, predicciones)
        precision = precision_score(labels_test, predicciones, average = "weighted")
        recall = recall_score(labels_test, predicciones, average = "weighted")
        f1 = f1_score(labels_test, predicciones, average = "weighted")
        reporte = f" Accuracy: {accuracy:.3%}\n Precisión: {precision:.3%}\n Recall: {recall:.3%}\n F1: {f1:.3%}"
        print("Accuracy: ",accuracy)
        print("Precisión: ",precision)
        print("Recall: ",recall)
        print("F1: ",f1)

        
        return reporte

    ## @brief Realiza las clasificaciones del conjunto de pruebas.
    # @param dataset [Panda Dataset] Dataset del conjunto de pruebas.
    # @param columna_extracto [String] Columna de donde se obtienen los extractos.
    # @return [Array] Array de arrays de las temáticas de cada iniciativa a clasificar.
    def clasificar_sentencias(self, dataset, columna_extracto):
        #Se obtienen las columnas.
        extractos = dataset[columna_extracto].astype(str)

        #Se realiza la clasificación.
        extractos_bag = self.__bag_words.transform(extractos)
        probabilidades_tematicas = self.crear_predicciones_probabilidades(extractos_bag)
        return self.crear_array_tematicas(self._modelo.classes_,probabilidades_tematicas)
    
    ## @brief Crea un array con las temáticas más cercanas a cada iniciativa según el alfa y el nº de temáticas.
    # @param clases [Array] Array de las temáticas ordenado por sus probabilidades.
    # @param probabilidades [Array] Array de las probabilidades de cada temática.
    # @return [Array] Array de arrays de las temáticas de cada iniciativa a clasificar.
    def crear_array_tematicas(self, clases, probabilidades):
        tematicas_sentencia = []
        # Se itera conjunto de se probs de una sola iniciativa, ya que tenemos un array de arrays de probs.
        for prob_sentencia in probabilidades: 
            conjunto_tematicas = []
            # Se obtiene los índices con mas probs. según el número de temáticas a mostrar.
            indices_mas_probs = (-prob_sentencia).argsort()[:self.__n_tematicas]
            ind_valor_maximo = indices_mas_probs[0]
            # Se itera los índices con mas probs y se añade al array si cumple con el umbral.
            for indice in indices_mas_probs:
                if (prob_sentencia[ind_valor_maximo] - prob_sentencia[indice]) <= self.__alfa:
                    conjunto_tematicas.append(clases[indice])
            tematicas_sentencia.append(conjunto_tematicas)
        
        return tematicas_sentencia



