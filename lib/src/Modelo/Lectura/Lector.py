## @package Lectura
# @brief Clase Lector, clase padre de la cual pueden salir distintos tipos de lectores (CSV, JSON, étc.), contiene funciones básicas.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

class Lector:

    ## @brief Constructor de Lector.
    def __init__(self):
        self.contenido_ = ""

    ## @brief Devuelve el contenido leído.
    # @return [String] Contenido leído por la variable "self.contenido_".
    def get_contenido(self):
        return self.contenido_
    
    ## @brief Actualiza el valor del contenido leído.
    # @param contenido [String] Contenido a actualizar en la variable "self.contenido_".
    def set_contenido(self, contenido):
        self.contenido_ = contenido
    
    ## @brief Detecta si el contenido es vacío.
    # @return [Boolean] Devuelve True si la variable "self.cotenido_" esta vacía, False sino lo está. 
    def esta_vacio(self):
        if self.contenido_ != "":
            return False
        else:
            return True
    
    ## @brief Imprime el contenido de la variable "self.contenido_"
    def imprimir(self):
        print (self.contenido_)

    ## @brief Método toString de la clase."
    # @return [String]
    def __str__(self):
        return "Tipo: Ninguno "




    
