from Modelo.Clasificacion.Clasificador import Clasificador
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, log_loss

# Clase ClasificadorAR: Clase que realiza entrenamientos y clasificaciones para datos que necesiten ser convertidos en array.
class ClasificadorAR(Clasificador):

    def __init__(self):
        super().__init__()
        
    def entrenar_modelo(self,columna_extracto,columna_tematica):
        extractos = self.dataset_[columna_extracto].astype(str)
        labels = self.dataset_[columna_tematica].astype(str)

        extractos_train, extractos_test, labels_train, labels_test = train_test_split(extractos, labels, test_size=0.20)
        extractos_train_bag = self.bag_words_.fit_transform(extractos_train)
        extractos_test_bag = self.bag_words_.transform(extractos_test)
        self.modelo_.fit(extractos_train_bag.toarray(), labels_train)
        predicciones = self.modelo_.predict(extractos_test_bag.toarray())

        precision = accuracy_score(labels_test, predicciones)
        return f"Precisión: {precision:.2%}"
    
    def clasificar_sentencias(self, dataset, columna_extracto):
        extractos = dataset[columna_extracto].astype(str)

        extractos_bag = self.bag_words_.transform(extractos)
        probabilidades_tematicas = self.modelo_.predict_proba(extractos_bag.toarray())
        return self.crear_array_tematicas(self.modelo_.classes_,probabilidades_tematicas)