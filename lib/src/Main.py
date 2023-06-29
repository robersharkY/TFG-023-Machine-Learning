## @brief Clase Main, se utiliza para iniciar el programa
# @author Roberto Carlos García Cruz
# @version 1.0
# @date "%A %d-%m-%Y" 1-6-2023

from Controlador.Controlador import Controlador

class Main:

    controlador = Controlador()
    controlador.iniciar()