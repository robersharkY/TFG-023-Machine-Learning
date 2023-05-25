import pandas
from Modelo.Lectura.Lector_CSV import LectorCSV

# Clase Dataset: Clase que facilita los métodos propios de un dataset.

class Dataset:

    def __init__(self):
        self.datos_ = None
        self.direccion_ = ""
        self.lector_ = LectorCSV()

    def get_direccion(self):
        return self.direccion_

    def set_direccion(self, direccion):
        self.direccion_ = direccion

    def get_columna(self, nombre_columna):
        return self.datos_[nombre_columna].tolist()

    def get_fila(self,n_fila):
        return self.datos_[n_fila].tolist()
    
    def get_valor(self, n_fila, nombre_columna):
        return self.datos_[n_fila, nombre_columna]
    
    def get_reader(self):
        return self.model_.get_reader()

    def get_datos(self):
        return self.datos_

    def set_datos(self,datos):
        self.datos_ = datos
    
    def set_reader(self, reader):
        self.model_.set_reader(reader)

    def leer_datos(self, direccion):
        self.datos_ = pandas.read_csv(direccion)
        self.set_direccion(direccion)

    def eliminar_columna(self, nombre_columna):
        if nombre_columna in self.datos_:
            del self.datos_[nombre_columna]

    def mostrar_datos(self):
        print (self.datos_)

    def __str__(self):
        return "Los datos leidos son de: "+self.direccion_
    

         