## @package Limpieza
# @brief Clase LectorCSV, clase hija de la clase Lector, lee archivos CSV mediante la librería panda.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

import spacy
import es_core_news_sm
from spacy.lang.es.stop_words import STOP_WORDS

# Clase Procesador: Clase para realizar el procesamiento del lenguaje natural.

class Procesador:

    def __init__(self):
        self.nlp_ = es_core_news_sm.load()

    def get_palabras_vacias(self):
        return STOP_WORDS
    
    def eliminar_palabras_vacias(self, sentencia):
        doc = self.nlp_(sentencia)
        sentencia_limpia = [token for token in doc if not token.is_stop and not token.is_punct]
        return sentencia_limpia
    
    def eliminar_duplicados(self, tokens):
         return list(dict.fromkeys(tokens))
    
    def lematizar(self, tokens):
        lemas=[]
        for token in tokens:
            lemas.append(token.lemma_)
        return lemas
    
    def __str__(self):
        return "Objeto para la limpieza de sentencias del lenguaje natural"
    
