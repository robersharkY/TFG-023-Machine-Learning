## @brief Clase Main, se utiliza para iniciar el programa
# @author Roberto Carlos García Cruz
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023
import os
from Controlador.Controlador import Controlador

class Main:

    controlador = Controlador()
    controlador.iniciar()