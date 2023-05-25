import pandas
from Modelo.Lectura.Lector import Lector 

# Clase LectorCSV: Clase específica para leer archivos CSV mediante la librería panda.

class LectorCSV(Lector):

    def __init__(self):
        super().__init__()

    def leer(self, direccion):
        self.set_contenido(pandas.read_csv(direccion, encoding = "utf-8"))

    def __str__(self):
        return "Tipo: CSV"

