## @package Datos
# @brief Clase Dataset, actúa como dataset para el almacenamiento de datos y para facilitar su mantenimiento.
# @author Roberto Carlos García Cruz.
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

import pandas
from Modelo.Lectura.Lector_CSV import LectorCSV

class Dataset:

    ## @brief Constructor de Dataset.
    def __init__(self):
        self.__datos = None
        self.__direccion = ""
        self.__lector = LectorCSV()

    ## @brief Devuelve la dirección del archivo leído.
    # @return [String] Dirección del archivo donde se han obtenido los datos.
    def get_direccion(self):
        return self.__direccion

    ## @brief Actualiza el valor de la dirección del archivo a leer.
    # @param direccion [String] dirección a actualizar en la variable "self.direccion_".
    def set_direccion(self, direccion):
        self.__direccion = direccion

    ## @brief Devuelve la columna indicada del dataset de datos.
    # @param nombre_columna [String] Nombre de la columna a leer del dataset de datos.
    # @return [Array] Datos obtenidos de la columna del dataset mencionado.
    def get_columna(self, nombre_columna):
        return self.__datos[nombre_columna].tolist()

    ## @brief Devuelve la fila indicada del dataset de datos.
    # @param n_fila [Integer] Número de la fila a leer del dataset de datos.
    # @return [Array] Datos obtenidos de la fila del dataset mencionado.
    def get_fila(self,n_fila):
        return self.__datos[n_fila].tolist()

    ## @brief Devuelve los datos de la fila  y columna indicada del dataset de datos.
    # @param n_fila [Integer] Número de la fila a leer del dataset de datos.
    # @param nombre_columna [String] Nombre de la columna a leer del dataset de datos.
    # @return [Array] Datos obtenidos de la fila y columna del dataset mencionado.
    def get_valor(self, n_fila, nombre_columna):
        return self.__datos[n_fila, nombre_columna]
    
    ## @brief Devuelve el dataset creado por la librería panda.
    # @return [Panda Dataset] Dataset creado por la librería panda.
    def get_datos(self):
        return self.__datos

    ## @brief Actualiza el dataset creado por la librería panda.
    # @param datos [Panda Dataset] dataset a actualizar en la variable "self.datos_".
    def set_datos(self,datos):
        self.__datos = datos

    ## @brief Actualiza el dataset creado por la librería panda.
    # @param datos [Panda Dataset] dataset a actualizar en la variable "self.datos_".
    def leer_datos(self, direccion):
        self.__datos = pandas.read_csv(direccion)
        self.set_direccion(direccion)
    
    ## @brief Elimina la columna del dataset que se pase por parámetro.
    # @param nombre_columna [String] Nombre de la columna a eliminar en el dataset.
    def eliminar_columna(self, nombre_columna):
        if nombre_columna in self.datos_:
            del self.__datos[nombre_columna]

    ## @brief Imprime el dataset de la variable "self.datos_"
    def mostrar_datos(self):
        print (self.__datos)

    ## @brief Método toString de la clase.
    # @return [String]
    def __str__(self):
        return "Los datos leidos son de: "+self.__direccion
    

         