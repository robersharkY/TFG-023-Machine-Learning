## @package Lectura
# @brief Clase LectorCSV, clase hija de la clase Lector, lee archivos CSV mediante la librería panda.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

import pandas
from Modelo.Lectura.Lector import Lector

class LectorCSV(Lector):

    ## @brief Constructor de LectorCSV.
    def __init__(self):
        super().__init__()
    
    ## @brief Lee el contenido del archivo csv indicado.
    # @param direccion [String] Dirección del archivo a leer.
    def leer(self, direccion):
        self.set_contenido(pandas.read_csv(direccion, encoding = "utf-8"))
    
    ## @brief Método toString de la clase."
    # @return [String]
    def __str__(self):
        return "Tipo: CSV"

