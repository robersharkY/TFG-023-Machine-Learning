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
    def __init__(self):
        self.dataset_entrenamiento_ = Dataset()
        self.dataset_prueba_ = Dataset()
        self.procesador_ = Procesador()
        self.clasificador_ = ClasificadorML()
        self.columna_extracto = "EXTRACTO"
        self.columna_tematica = "TEMATICA"

    def leer_dataset_entrenamiento(self,direccion_entrenamiento):
        self.dataset_entrenamiento_ = Dataset()
        self.dataset_entrenamiento_.leer_datos(direccion_entrenamiento)
    
    def leer_dataset_prueba(self,direccion_prueba):
        self.dataset_prueba_ = Dataset()
        self.dataset_prueba_.leer_datos(direccion_prueba)
    
    def get_datos_entrenamiento(self):
        return self.dataset_entrenamiento_.get_datos()
    
    def get_datos_pruebas(self):
        return self.dataset_prueba_.get_datos()
    
    def get_array_variables(self):
        return [self.clasificador_.get_n_tematicas(), self.clasificador_.get_alfa(), self.columna_extracto, self.columna_tematica]

    def set_variables(self,array_variables,vista):
        if array_variables[0].isnumeric() and array_variables[0] != "":
            numero = int(array_variables[0])
            if numero < 1 and numero > 10:
                vista.mostrar_ventana_mensaje("El número de temáticas debe ser entre 1 y 10")
            else:
                self.clasificador_.set_n_tematicas(numero)
        else:
            vista.mostrar_ventana_mensaje("Debe introducir un dato numérico")

        if re.match(r'^-?\d+(?:\.\d+)$', array_variables[1]) and array_variables[1] != "":
            numero = float(array_variables[1])
            if numero < 0 and numero > 1:
                vista.mostrar_ventana_mensaje("El alfa debe ser entre 0 y 1")
            else:
                self.clasificador_.set_alfa(numero)
        else:
            vista.mostrar_ventana_mensaje("Debe introducir un dato numérico")
            
        if array_variables[2] != "":
            self.columna_extracto = array_variables[2]
        else:
            vista.mostrar_ventana_mensaje("Debe introducir un nombre de columna")

        if array_variables[3] != "":
            self.columna_tematica = array_variables[3]
        else:
            vista.mostrar_ventana_mensaje("Debe introducir un nombre de columna")


    def seleccionar_bag_words(self,tipo):
        if tipo == "CV":
            self.clasificador_.set_bag_words(CountVectorizer(binary = True))
        else:
            self.clasificador_.set_bag_words(TfidfVectorizer(binary = True))
    
    def seleccionar_algoritmo(self,tipo):
        if tipo == "SVC-Lineal SVC":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(SVC(kernel='linear',probability=True))
        elif tipo == "SVC-SVR":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(SVC(kernel='rbf',probability=True))
        elif tipo == "SVC-Nu SVC":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(NuSVC(kernel='linear',probability=True))
        elif tipo == "TR-Decision Tree":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(DecisionTreeClassifier())
        elif tipo == "TR-Extra Tree":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(ExtraTreeClassifier())
        elif tipo == "NB-Multinomial":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(MultinomialNB())
        elif tipo == "NB-Gaussian":
            self.clasificador_ = ClasificadorAR()
            self.clasificador_.set_modelo(GaussianNB())
        elif tipo == "NB-Bernoulli":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(BernoulliNB())
        elif tipo == "ENS-Random Forest":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(RandomForestClassifier())
        elif tipo == "ENS-Gradient Boost":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(GradientBoostingClassifier())
        elif tipo == "ENS-Ada Boost":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(AdaBoostClassifier())
        elif tipo == "KNN-K-Neighbors":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(KNeighborsClassifier(n_neighbors = 4))
        elif tipo == "NEU-MLP":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(MLPClassifier())
        elif tipo == "DIS-Quadratic Discriminant":
            self.clasificador_ = ClasificadorAR()
            self.clasificador_.set_modelo(QuadraticDiscriminantAnalysis())
        elif tipo == "DIS-Linear Discriminant":
            self.clasificador_ = ClasificadorAR()
            self.clasificador_.set_modelo(LinearDiscriminantAnalysis())
        elif tipo == "LM-SGD":
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(SGDClassifier(loss='log_loss'))
        else:
            self.clasificador_ = ClasificadorML()
            self.clasificador_.set_modelo(LogisticRegression())

    def limpiar_datasets(self):
        self.limpiar_sentencias(self.dataset_entrenamiento_)
        self.limpiar_sentencias(self.dataset_prueba_)
    
    def estan_limpios_datasets(self):
        df_entrenamiento = self.dataset_entrenamiento_.get_datos()
        df_prueba = self.dataset_prueba_.get_datos()
        self.dataset_entrenamiento_
        for index, row in df_prueba.iterrows():
            if not isinstance(row[self.columna_extracto], list):
                return False
        for index, row in df_entrenamiento.iterrows():
            if not isinstance(row[self.columna_extracto], list):
                return False
        return True
    
    def limpiar_sentencias(self,dataset):
        df = dataset.get_datos()
        for index, row in df.iterrows():
            if not isinstance(row[self.columna_extracto], list):
                tokens = self.procesador_.eliminar_palabras_vacias(row[self.columna_extracto])
                tokens = self.procesador_.eliminar_duplicados(tokens)
                tokens = self.procesador_.lematizar(tokens)
                df.at[index,self.columna_extracto] = tokens
        dataset.set_datos(df)

    def entrenamiento(self):
        self.clasificador_.set_dataset(self.dataset_entrenamiento_.get_datos())
        tipo = self.clasificador_.get_modelo().__str__()
        return self.clasificador_.entrenar_modelo(self.columna_extracto,self.columna_tematica)

    def clasificar(self):
        self.verificar_dataframe()
        tipo = self.clasificador_.get_modelo().__str__()
        predicciones = self.clasificador_.clasificar_sentencias(self.dataset_prueba_.get_datos(),self.columna_extracto)

        for index, row in self.dataset_prueba_.get_datos().iterrows():
           self.dataset_prueba_.get_datos().at[index,self.columna_tematica] = ', '.join(str(item) for item in predicciones[index])
        
        
    def verificar_dataframe(self):
        df = self.dataset_prueba_.get_datos()
        if self.columna_tematica not in df:
            df[self.columna_tematica] = None
        self.dataset_prueba_.set_datos(df)

        
        
        
