class Lector:
    
    def __init__(self):
        self.contenido_ = ""

    def get_contenido(self):
        return self.contenido_
    
    def set_contenido(self,contenido):
        self.contenido_ = contenido
    
    def is_empty_contenido(self):
        if self.contenido_ != "":
            return False
        else:
            return True

    def imprimir(self):
        print (self.contenido_)

    def __str__(self):
        return "Tipo: Ninguno "




    
