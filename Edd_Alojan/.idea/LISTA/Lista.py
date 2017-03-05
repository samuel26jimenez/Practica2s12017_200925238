__author__ = 'Samuel'

class Lista():
    global cad     #cadena a ingresar
    cad = ""
    global sigL;       #puntero siguiente lista
    sigL = None


    def __init__(self, cadena):
        self.cad = cadena;

    def __set__(self, cadena):
        self.cad = cadena;

    def __gt__(self):
        return self.cad;