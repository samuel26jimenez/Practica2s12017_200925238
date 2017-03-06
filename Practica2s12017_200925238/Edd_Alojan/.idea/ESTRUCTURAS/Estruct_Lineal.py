__author__ = 'Samuel'
#---------------------------LISTA-------------------------------
from flask import Flask, request, Response
import os
app = Flask("Estruct_Lineal")


class Lista_Nodo:
    def __init__(self, cad_tecla):
        self.cad_tecla = cad_tecla
        self.Lsig = None

    def set_cadTecla(self, cad_tecla):
        self.cad_tecla = cad_tecla

    def get_cadTecla(self):
        return self.cad_tecla


class Metodo_Lista:
    def __init__(self):
        self.ini = None
        self.ult = None

    def esVacio(self):
        if self.ini == None:
            return True
        else:
            return False

    def _Inserta_Nodo(self, cadenas):
        _nvo_Nodo = Lista_Nodo(cadenas)
        if self.esVacio()== True:
            self.ini = self.ult = _nvo_Nodo
        else:
            self.ult.Lsig = _nvo_Nodo
            self.ult = self.ult.Lsig
            #_nvo_Nodo.Lsig = self.ini;
            #self.ini = _nvo_Nodo;

    def _Eliminar_N(self, cad_ena):
       # Lsig = Lista_Nodo(cad_ena)
        if self.esVacio() == True:
            print "Lista Vacia"
        else:
            self.borr = Lista_Nodo
            self.borr = self.ini
            self.aux = None
            while(self.borr != None and self.borr.cad_tecla != cad_ena):
                self.aux = self.borr
                self.borr = self.borr.Lsig
            if self.borr == None:
                print "No existe Dato"
            else:
                if self.borr.cad_tecla == cad_ena:
                    #self.aux = Lista_Nodo
                    if self.borr == self.ini:
                        self.ini = self.ini.Lsig
                    else:
                        self.aux.Lsig = self.borr.Lsig
                    #self.borr = None
                else:
                    if self.aux == None:
                        self.aux = self.borr.Lsig
                        self.ini = self.borr.Lsig
                        self.borr = None

    def _Mostrar(self):
        self.temporal = self.ini
        while(self.temporal != None):
            print self.temporal.get_cadTecla()
            self.temporal = self.temporal.Lsig

    def _Buscar(self, ingre_cad):
        self.tempo2 = Lista_Nodo
        self.tempo2 = self.ini
        while self.tempo2.get_cadTecla() != ingre_cad and self.tempo2 != None:
            self.tempo2 = self.tempo2.Lsig
        if self.tempo2 !=  None and self.tempo2.cad_tecla == ingre_cad:
            print "cadena es : " + self.tempo2.cad_tecla

    def search(self, cadena):
        if self.esVacio() == False:
            aux = self.ini
            while aux != None and aux.get_cadTecla() != cadena:
                aux = aux.Lsig

            if  aux != None and aux.get_cadTecla() == cadena:
                print "cadena: "+ aux.get_cadTecla()
            else:
                print "Cadena No Existe"

    def grafica_Lista(self):
        if self.esVacio() == True:
            return
        else:
            archivo = open("grafica_lista.dot","w")
            archivo.write("digraph G{\n")
            tempo = self.ini
            i = 0
            while tempo != None:
                archivo.write("\"Node"+str(i)+"\"[label = \""+tempo.get_cadTecla()+"\" style=filled]\n")
                if tempo.Lsig != None:
                    archivo.write("\"Node"+str(i)+"\" -> \"Node"+str(i+1)+"\"")
                i = i + 1
                tempo = tempo.Lsig

            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_lista.dot > grafica_lista.png")

#-------------------------- COLA ----------------------------
#global sigC
class Cola_Nodo:

    def __init__(self, numC):
        self.numC = numC
        self.sigC = None

    def set_Cola(self, enteroC):
        self.numC = enteroC

    def get_Cola(self):
        return self.numC

class Metodo_Cola:
    def __init__(self):
        self.C_ini = None
        self.C_fin = None

    def _Enqueue(self, mete_num):
        nvo_Nodo = Cola_Nodo(mete_num)
        if self.esVacio() == True:
            self.C_ini = self.C_fin = nvo_Nodo
        else:
            self.tempo3 = self.C_ini
            while(self.tempo3 != None):
                self.tempo3 = self.tempo3.sigC
            self.tempo3 = nvo_Nodo
            self.C_fin.sigC = self.tempo3
            self.C_fin = self.C_fin.sigC
            nvo_Nodo.sigC = None

    def Queue(self):
        if self.esVacio() == True:
            temp = self.C_ini
            if self.C_ini.sigC != None:
                self.C_ini = self.C_ini.sigC
                temp = None
            else:
                self.C_ini = self.C_fin = None



    def esVacio(self):
        if self.C_ini == None:
            return True
        else:
            return False

    def Mostrar_C(self):
        self.aux = self.C_ini
        while(self.aux != None):
            print self.aux.get_Cola()
            self.aux = self.aux.sigC

    def Graficar_Cola(self):
        if self.esVacio() == True:
            return
        else:
            escri_C = open("graf_C.dot","w")
            escri_C.write("digraph G{\n")
            tempo_C = self.C_ini
            while tempo_C != None:
                escri_C.write("\"Node" +  str(tempo_C.get_Cola()) + "\"[label =\""+ str(tempo_C.get_Cola())+ "\", style = filled, fillcolor = \"#FF4000\"]\n")
                if tempo_C.sigC != None:
                    escri_C.write("\"Node" + str(tempo_C.get_Cola()) + "\" -> \"Node" +  str(tempo_C.sigC.get_Cola())+ "\"\n")
                tempo_C = tempo_C.sigC
            escri_C.write("}\n")
            escri_C.close()
            os.system("dot -Tpng graf_C.dot > graf_C.png")

#---------------------------- PILA --------------------------------

class Pila_Nodo:
    def __init__(self, numP):
        self.numP = numP
        self.sigP = None

    def set_Pila(self, enteroP):
        self.numP = enteroP

    def get_Pila(self):
        return self.numP

class Metodo_Pila:

    def __init__(self):
        self.P_ini = None
        self.P_fin = None

    def Meter(self, ingrec_Num):#Meter
        nvo_Nodo = Pila_Nodo(ingrec_Num)
        if self.esVacio() == True:
            self.P_ini = self.P_fin = nvo_Nodo
        else:
            tempo3 = self.P_ini
            while(tempo3 != None):
                tempo3 = tempo3.sigP
            tempo3 = nvo_Nodo
            self.P_fin.sigP = tempo3
            self.P_fin = self.P_fin.sigP
            nvo_Nodo.sigP = None


    def Sacar(self):#sacar
        if self.esVacio() == True:
            print "Pila Vacia"
        else:
            t = self.P_ini
            while t.sigP != None and t.sigP != self.P_fin:
                 t = t.sigP

            if self.P_ini == self.P_fin:
                self.P_ini = None
                self.P_fin = None
            else:
                t.sigP = None
                self.P_fin = t


    def Mostrar_P(self):
        ver = self.P_ini
        while (ver != None):
            print ver.get_Pila()
            ver = ver.sigP


    def esVacio(self):
        if self.P_ini == None:
            return True
        else:
            return False

    def Graficar_Pila(self):
        if self.esVacio() == True:
            return
        else:
            archivo_Pila = open("graf_Pila.dot","w")
            archivo_Pila.write("digraph G{\n")
            tempo_P = self.P_ini
            while tempo_P != None:
                archivo_Pila.write("\"Node" +  str(tempo_P.get_Pila()) + "\"[label =\""+ str(tempo_P.get_Pila())+ "\", style = filled, fillcolor = \"#FF4000\"]\n")
                if tempo_P.sigP != None:
                    archivo_Pila.write("\"Node" + str(tempo_P.get_Pila()) + "\" -> \"Node" +  str(tempo_P.sigP.get_Pila())+ "\"\n")
                tempo_P = tempo_P.sigP
            archivo_Pila.write("}\n")
            archivo_Pila.close()
            os.system("dot -Tpng graf_Pila.dot > graf_Pila.png")


# class Menu:
#     a = Metodo_Lista()
#     b = Metodo_Cola()
#     c = Metodo_Pila()
#     opcion = 0
#     while(opcion != 1):
#         print "----LISTA---"
#         print "1.- Salir"
#         print "2.- Agregar"
#         print "3.- Buscar"
#         print "4.- Eliminar"
#         print "----COLA----"
#         print "5.- Insertar_Cola"
#         print "6.- Eliminar_d_Cola"
#         print "----PILA----"
#         print "7.- Insertar_Pila"
#         print "8.- Eliminar_d_Pila"
#         print '---- Graficar ----'
#         print '9.- Grafica_Lista'
#         print '10.- Grafica_Cola'
#         print '11.- Grafica_Pila'
#         print '12.- Grafica_Dispersa'
#         opcion = int(raw_input("ingresar valor "))
#         if opcion == 1:
#             exit()
#         if opcion == 2:
#             print "Ingresar Cadena"
#             cadena = raw_input()
#             a._Inserta_Nodo(cadena)
#             a._Mostrar()
#         if opcion == 3:
#             print "Ingresar cadeba a Buscar"
#             cadena3 = raw_input()
#             #a._Buscar(cadena3)
#             a.search(cadena3)
#             a._Mostrar()
#         if opcion == 4:
#             print "Eliminar Cadena"
#             cadena4 = raw_input()
#             a._Eliminar_N(cadena4)
#             a._Mostrar()
#         if opcion == 5:
#             print "Insertar Num Cola"
#             cadena5 = int(raw_input())
#             b._Enqueue(cadena5)
#             b.Mostrar_C()
#         if opcion == 6:
#             print "Eliminar Nodo Cola"
#             b.Queue()
#             b.Mostrar_C()
#         if opcion == 7:
#             print "Insertar Num Pila"
#             valor_ingresa = int(raw_input())
#             c.Meter(valor_ingresa)
#             c.Mostrar_P()
#         if opcion == 8:
#             print "Eliminar num Pila"
#             c.Sacar()
#             c.Mostrar_P()
#         if opcion == 9:
#             print "Grafica_Lista"
#             a.grafica_Lista()
#         if opcion == 10:
#             print "Grafica_Cola"
#             b.Graficar_Cola()
#         if opcion == 11:
#             print "Grafica_Cola"
#             c.Graficar_Pila()
#









