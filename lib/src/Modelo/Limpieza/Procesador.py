## @package Limpieza
# @brief Clase Procesador, clase especializada para realizar el procesamiento del lenguaje natural.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

import spacy
import es_core_news_sm
from spacy.lang.es.stop_words import STOP_WORDS


class Procesador:

    ## @brief Constructor de Procesador.
    def __init__(self):
        ## Variable privada, librería cargada en variable para realizar las operaciones.
        self.__nlp = es_core_news_sm.load()
    
    ## @brief Devuelve las palabras vacías de la librería.
    # @return [Array] Palabras vacías de la librería de Spacy.
    def get_palabras_vacias(self):
        return STOP_WORDS
    
    ## @brief Tokeniza la cadena, a parte, elimina los signos de puntuación y las palabras vacías de una cadena/sentencia.
    # @param sentencia [String] Cadena a limpiar.
    # @return [Array] DPalabras vacías de la librería de Spacy.
    def eliminar_palabras_vacias(self, sentencia):
        doc = self.__nlp(sentencia)
        sentencia_limpia = [token for token in doc if not token.is_stop and not token.is_punct]
        return sentencia_limpia
    
    ## @brief Elimina palabras (tokens) iguales.
    # @param tokens [Array] Array de tokens.
    # @return [Array] Array de tokens sin elementos repetidos.
    def eliminar_duplicados(self, tokens):
         return list(dict.fromkeys(tokens))

    ## @brief Lematiza (convierte a su palabra raíz) cada uno de los tokens
    # @param tokens [Array] Array de tokens.
    # @return [Array] Array de tokens lematizados
    def lematizar(self, tokens):
        lemas=[]
        for token in tokens:
            lemas.append(token.lemma_)
        return lemas

    ## @brief Método toString de la clase.
    # @return [String]
    def __str__(self):
        return "Objeto para la limpieza de sentencias del lenguaje natural"
    
