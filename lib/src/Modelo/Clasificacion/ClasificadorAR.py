## @package Clasificacion
# @brief Clase ClasificadorAR, Clase hija de Clasificador que contiene ciertos métodos para transformar datos a array y así lograr hacer funcionar los métodos de Clasificador.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from Modelo.Clasificacion.Clasificador import Clasificador

class ClasificadorAR(Clasificador):

    ## @brief Constructor de ClasificadorAR.
    def __init__(self):
        super().__init__()
    
    ## @brief Realiza el entrenamiento con datos transformados en array (necesario para ciertos algoritmos).
    # @param extractos_train_bag [Array] Extractos de entrenamiento.
    # @param extractos_train_bag [Array] Labels de entrenamiento.
    def entrenamiento(self, extractos_train_bag, labels_train):
        self._modelo.fit(extractos_train_bag.toarray(), labels_train)

    ## @brief Crea las predicciones del entrenamiento transformados en array (necesario para ciertos algoritmos).
    # @param extractos_test_bag [Array] Extractos de test.
    # @return [Array] Array de predicciones del dataset de entrenamiento.
    def crear_predicciones(self, extractos_test_bag):
        return self._modelo.predict(extractos_test_bag.toarray())

    ## @brief Crea las prediciones según sus probabilidades con datos transformados en array (necesario para ciertos algoritmos).
    # @param extractos_bag [Array] Extractos de dataset de prueba.
    # @return [Matrix] Matriz de probabilidades, cada array son las probabilidades de todas las temáticas de cada iniciativa.
    def crear_predicciones_probabilidades(self, extractos_bag):
        return self._modelo.predict_proba(extractos_bag.toarray())