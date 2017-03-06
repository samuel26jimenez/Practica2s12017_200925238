__author__ = 'Samuel'
#from this import cad
from Lista import Lista;
import sys

global ini
ini = None

class Metodos_Lista():
   # ini = None
    #def __init__(self):
    #    self.ini = None;

    cad = "hola mike"
    sig = None
    cabeza = Lista()

    def agregar(self, x):   #Metodo que Agrega un nodo a la lista
        print(self.cad)
        nuevo = Lista(self,"")
        nuevo.__set__(x)
        nuevo.sigL=cabeza.sigL;
        cabeza=nuevo;
            #return


    def Imprimir():
        while(aux != None):
            print("se agrego " +  aux.cad + " --> ")
            aux = aux.sigL;



    def buscar(self, val):
        #self.tempo1;                 # nodo tempo1 que recorre lista, busca el dato val.
        tempo1 = ini;
        while(tempo1.cad != val):
            tempo1 = tempo1.sigL;
        return tempo1.cad;

    def borrar(self, cad_elim):
        self.aux;
        self.borra;
        borra = self.ini;
        aux = None;
        while(borra.cad != cad_elim & tempo.sigL != None):
            aux = borra;
            borra = borra.sigL;
        if(aux == None):
            aux = borra.sigL;
            ini = borra.sigL;
            #Eliminar el puntero encontrado parecido a free() de C
        else:
            if (borra == None):
                print "Nodo no encontrado"
            else:
                aux.sigL = borra.sigL;
                #eliminar el puntero encontrado parecido a free() de C
        aux = ini;
        while(aux.sigL != None):
            print ("lista actual"  + aux.cad)
            aux = aux.sigL;

    def esVacio(self):
        if(ini == None):
            return True;
        else:
            return False;

class Menu():
    a = Metodos_Lista();
    opcion = 0;
    while(opcion != 1):
        print("1. Salir")
        print("2. Agregar")
        print("3. Buscar")
        print("4. Borrar")
        opcion = int(raw_input("ingresar Numero:" ))
        if opcion == 2:
            print "Ingresar Cadena"
            nuevo = raw_input()
            print ("Exitos " + nuevo)
            a.agregar(nuevo)
        if opcion == 3:
            print "Buscar Cadena"
            busca_cad = raw_input()
            a.buscar(busca_cad)
        if opcion == 4:
            print("Borrar Cadena")
            elimina_cad = raw_input()
            a.borrar(elimina_cad)
