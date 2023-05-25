from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

# Clase Clasificador: Clase padre para clasificadores con distintas arquitecturas.
class Clasificador:

    def __init__(self):
        self.dataset_ = None
        self.bag_words_ = TfidfVectorizer(binary = True)
        self.modelo_ = SVC(kernel = "linear", probability = True)
        self.alfa_ = 0.05
        self.n_tematicas = 2

    def get_n_tematicas(self):
        return self.n_tematicas
    
    def set_n_tematicas(self, n_tematicas):
        self.n_tematicas = n_tematicas
    
    def get_alfa(self):
        return self.alfa_
    
    def set_alfa(self, alfa):
        self.alfa_ = alfa
        
    def get_bag_words(self):
        return self.bag_words_
    
    def set_bag_words(self, bag_words):
        self.bag_words_ = bag_words
    
    def get_modelo(self):
        return self.modelo_

    def set_modelo(self, modelo):
        self.modelo_ = modelo

    def set_dataset(self, dataset):
        self.dataset_ = dataset

    def crear_array_tematicas(self, clases, probabilidades):
        tematicas_sentencia = []
        for prob_sentencia in probabilidades:
            conjunto_tematicas = []
            indices_mas_probs = (-prob_sentencia).argsort()[:self.n_tematicas]
            ind_valor_maximo = indices_mas_probs[0]
            for indice in indices_mas_probs:
                if (prob_sentencia[ind_valor_maximo] - prob_sentencia[indice]) <= self.alfa_:
                    conjunto_tematicas.append(clases[indice])
            tematicas_sentencia.append(conjunto_tematicas)
        
        return tematicas_sentencia


