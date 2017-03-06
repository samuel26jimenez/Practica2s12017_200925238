from string import _TemplateMetaclass

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
        tempo = 1
        while self.tempo2 != None and self.tempo2.get_cadTecla() != ingre_cad:
            tempo = tempo + 1
            self.tempo2 = self.tempo2.Lsig
        #if self.tempo2 == self.ini and self.tempo2.cad_tecla == ingre_cad:
            #tempo == 1
         #   return tempo
        if self.tempo2 !=  None and self.tempo2.cad_tecla == ingre_cad:
            print "cadena es : " + self.tempo2.cad_tecla
            return tempo
        else:
            return 0

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
        if self.esVacio() == False:
            temp = self.C_ini
            if self.C_ini.sigC != None:
                numero = self.C_ini.get_Cola()
                self.C_ini = self.C_ini.sigC
                temp = None
                return numero
            else:
                numero = self.C_ini.get_Cola()
                self.C_ini = self.C_fin = None
                return numero
        return "-"



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
            print ("Pila Vacia")
            return "-"
        else:
            t = self.P_ini
            while t.sigP != None and t.sigP != self.P_fin:
                 t = t.sigP

            if self.P_ini == self.P_fin:
                numero = self.P_ini.get_Pila()
                self.P_ini = None
                self.P_fin = None
                return numero
            else:
                numero = t.sigP.get_Pila()
                t.sigP = None
                self.P_fin = t
                return numero


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

#---------------------- MATRIZ --------------------------
class Matriz_Estruct_Dispersa:
    def __init__(self, e_mail, let, _domin):
        self._domin = _domin
        self.e_mail = e_mail
        self.let = let
        self.arrib = None
        self.abaj = None
        self.izq = None
        self.der = None
        self.atras = None
        self.delant = None

    def getDomin(self):
        return self._domin

    def setE_mail(self, e_mail):
        self.e_mail = e_mail

    def getE_mail(self):
        return self.e_mail

    def getLet(self):
        self.let



class Cuerpo_Matriz:
    def  __init__(self):
        self.i_Horiz = None
        self.i_Vert = None
        self.i = Matriz_Estruct_Dispersa("", "", "")

    def inserta(self, name, let, domin):
        newMatrizNodo = Matriz_Estruct_Dispersa(name, let, domin)

        if self.esVacioH() == True:
            newMatrizNodoH = Matriz_Estruct_Dispersa("", "", domin)
            self.i_Horiz = newMatrizNodoH

        if self.esVacioV() == True:
            newMatrizNodoV = Matriz_Estruct_Dispersa("", let, "")
            self.i_Vert =  newMatrizNodoV

#----------------- Cabezas Lineales ------------------

        x1_H = self.i_Horiz

        if self.Domin_ExisteH(domin) == True:
            while x1_H.getDomin() !=  domin:
                x1_H = x1_H.der
        else:
            newMatrizNodoH = Matriz_Estruct_Dispersa("", "", domin)
            x2 = None
            while x1_H != None and x1_H.getDomin() < domin:
                x2 = x1_H
                x1_H = x1_H.der

            if x1_H != None and x1_H.getDomin() > domin:
                if x1_H == self.i_Horiz:
                    x3 = self.i_Horiz
                    x1_H = newMatrizNodoH
                    x1_H.izq = None
                    x1_H.der = x3
                    x3.izq = x1_H
                    self.i_Horiz = x1_H
                else:
                    x3 = x1_H
                    x1_H = newMatrizNodoH
                    x2.der = x1_H
                    x1_H.der = x3
                    x3.izq = x1_H
                    x1_H.izq = x2

            else:
                x1_H = newMatrizNodoH
                x2.der = x1_H
                x1_H.izq = x2

#------------------- Puntador Cabezales Horizonte ------
        if x1_H.abaj != None:
            x4 = None
            while x1_H.abaj != None:
                x4 = x1_H
                x1_H = x1_H.abaj
                if x1_H.getLet() == let or x1_H.getLet() > let:
                    break

        if x1_H.getLet() == let:
            if x1_H.atras != None:
                while x1_H.atras != None:
                    x1_H = x1_H.atras
            x1_H.atras = newMatrizNodo
            newMatrizNodo.delant = x1_H

        elif x1_H.abaj != None and x1_H.abaj.getLet() > let:
            x5 = x1_H.abaj
            x1_H = newMatrizNodo
            x4.abaj = x1_H
            x1_H.abaj = x5
            x5.arrib = x1_H
            x1_H.arrib = x4

        elif x1_H != None and x1_H.getLet() > let:
            x5 = x1_H
            x1_H = newMatrizNodo
            x4.abaj = x1_H
            x1_H.abaj = x5
            x5.arrib = x1_H
            x1_H.arrib = x4

        else:
            x1_H.abaj = newMatrizNodo
            newMatrizNodo.arrib = x1_H

#--------------- Cabezales Verticales -----------------

        t_Vert = self.i_Vert

        if self.Letra_ExiteV(let) == True:
            while t_Vert.getLet() != let:
                t_Vert = t_Vert.abaj

        else:
            newMatrizNodoV = Matriz_Estruct_Dispersa("", let, "")
            temp3 = None
            while t_Vert != None and t_Vert.getLet() < let:
                temp3 = t_Vert
                t_Vert = t_Vert.abaj

            if t_Vert != None and t_Vert.getLet() > let:
                if t_Vert == self.i_Vert:
                    x3 = self.i_Verti
                    t_Vert = newMatrizNodoV
                    t_Vert.arrib = None
                    t_Vert.abaj = x3
                    x3.arrib = t_Vert
                    self.i_Vert = t_Vert

                else:
                    x3 = t_Vert
                    t_Vert = newMatrizNodoV
                    temp3.abaj = t_Vert
                    t_Vert.abaj = x3
                    x3.arrib = t_Vert
                    t_Vert.arrib = temp3

            else:
                t_Vert = newMatrizNodoV
                temp3.abaj = t_Vert
                t_Vert.arrib = temp3

#------------------- Puntador Cabezales Verticales  -----

        if t_Vert.der != None:
            x4 = None
            while t_Vert.der != None:
                x4 = t_Vert
                t_Vert = t_Vert.der
                if t_Vert.getDomin() == domin or t_Vert.getDomin() > domin:
                    break

        if t_Vert.getDomin() == domin and t_Vert.getE_mail() != name:
            return

        elif t_Vert.der != None and t_Vert.der.getDomin() > domin:
            x5 = t_Vert
            t_Vert = newMatrizNodo
            x4.der = t_Vert
            t_Vert.der = x5
            x5.izq = t_Vert
            t_Vert.izq = x4

        elif t_Vert != None and t_Vert.getDomin() != "" and t_Vert.getDomin() > domin:
            x5 = t_Vert
            t_Vert = newMatrizNodo
            x4.der = t_Vert
            t_Vert.der = x5
            x5.izq = t_Vert
            t_Vert.izq = x4

        else:
            t_Vert.der = newMatrizNodo
            newMatrizNodo.izq = t_Vert

    def esVacioV(self):
        if self.i_Vert == None:
            return True
        else:
            return False

    def esVacioH(self):
        if self.i_Horiz == None:
            return  True
        else:
            return False

    def Domin_ExisteH(self, _dom):
        tx = self.i_Horiz
        while tx != None:
            if tx.getDomin() == _dom:
                return True
            else:
                tx  = tx.der
        return False

    def Letra_ExiteV(self, _letr):
        tx1 = self.i_Vert
        while tx1 != None:
            if tx1.getLet() == _letr:
                return True
            else:
                tx1 = tx1.abaj
        return False

    def letra_search(self):
        if self.esVacioV() == False:
            aux = self.i_Vert
            while aux != None and aux.getLet() != let:
                aux = aux.abaj

            if aux.getLet() == let:
                print ("<--->" + aux.getLet + "<--->")
                if aux.der != None:
                    _caden = ""
                    aux = aux.der
                    while aux != None:
                        print(aux.getE_mail() + "" + aux.getDomin())
                        _caden = _caden + aux.getE_mail() + " " + aux.getDomin() + "\n"
                        if aux.atras != None:
                            aux_Otro = aux.atras
                            while aux_Otro != None:
                                print(aux_Otro.getE_mail()  + " " + aux_Otro.getDomin())
                                _caden = _caden + aux_Otro.getE_mail() + " " + aux_Otro.getDomin() + "\n"
                                aux_Otro = aux_Otro.atras
                        aux = aux.der

                    return _caden

    def search_Domin(self, domin):
        if self.esVacioH() == False:
            aux = self.i_Horiz
            while aux != None and aux.getDomin() != domin:
                aux = aux.der

            if aux.getDomin() == domin:
                print( aux.getDomin() )
                if aux.abaj != None:
                    cadena = ""
                    aux = aux.abaj
                    while aux != None:
                        print(aux.getE_mail() + aux.getLet())
                        cadena = cadena + aux.getE_mail() + aux.getDomin() + "\n"
                        if aux.atras != None:
                            aux_otro = aux.atras
                            while aux_otro != None:
                                print(aux_otro.getE_mail() + aux_otro.getE_mail())
                                cadena = cadena + aux_otro.getE_mail() + aux_otro.getE_mail() + "\n"
                                aux_otro = aux_otro.atras
                            aux = aux.abaj
                        return cadena

    def Suprimir_Dominio(self, nom, let, domin):
        temp_Horizon = self.i_Horiz
        temp_Vertic = self.i_Vert
        x1 = x2 = None

        while temp_Horizon != None and temp_Horizon.getDomin() != domin:
            x1 = temp_Horizon
            temp_Horizon = temp_Horizon.der

        while temp_Vertic != None and temp_Vertic.getLet() != let:
            x2 = temp_Vertic
            temp_Vertic = temp_Vertic.abaj

        if temp_Horizon != None and temp_Vertic != None and temp_Horizon.getDomin() == domin and temp_Vertic.getLet() == let:

            while temp_Horizon != None and temp_Horizon.getLet() != let:
                x3 = temp_Horizon
                temp_Horizon = temp_Horizon.abaj

            while temp_Vertic != None and temp_Vertic.getDomin() != domin:
                x4 = temp_Vertic
                temp_Vertic = temp_Vertic.der

            if temp_Horizon != None and temp_Horizon.atras != None:
                while temp_Horizon.atras != None and temp_Horizon.getE_mail() != nombre:
                    x3 = temp_Horizon
                    temp_Horizon = temp_Horizon.atras

            if temp_Vertic != None and temp_Vertic.atras != None:
                while temp_Vertic.atras != None and temp_Vertic.getE_mail() != nom:
                    x4 = temp_Vertic
                    temp_Vertic = temp_Vertic.atras

            #---------------------- Delete Cabezales horizontales -----------

            if temp_Horizon != None and temp_Horizon.getE_mail() == nom:
                if x3 != None and  x3.getE_mail() == "":
                    if temp_Horizon.atras != None:
                        x3.abaj = temp_Horizon.atras
                        temp_Horizon.atras.arriba = x3
                        if temp_Horizon.abaj != None:
                            temp_Horizon.atras.abaj = temp_Horizon.abaj
                            temp_Horizon.abaj.arrib = temp_Horizon.atras
                    elif temp_Horizon.abaj != None:
                        x3.abaj = temp_Horizon.abaj
                        temp_Horizon.abaj.arrib = x3
                    else:
                        x3.abaj = None
                        if x1 != None and x3.der != None:
                            x1.der = x3.der
                            x3.der.izq = x1
                            x3 = None
                        elif x1 != None:
                            x1.der = None
                            x3 = None
                        elif x3.der != None:
                            x3.der.izq = None
                            self.i_Horiz = x3.der
                            x3 = None
                        else:
                            x3 = self.i_Horiz = None

                elif x3 != None:
                    if temp_Horizon.delant != None:
                        if temp_Horizon.atras != None:
                            x3.atras = temp_Horizon.atras
                            temp_Horizon.atras.adelant = x3
                        else:
                            x3.atras = None
                    elif temp_Horizon.atras != None:
                        x3.abaj = temp_Horizon.atras
                        if temp_Horizon.abaj != None:
                            temp_Horizon.atras.abaj = temp_Horizon.abaj
                            temp_Horizon.abaj.arrib = temp_Horizon.atras
                        temp_Horizon.atras.arriba = x3
                    elif temp_Horizon.abaj != None:
                        x3.abaj = temp_Horizon.abaj
                        temp_Horizon.abaj.arrib = x3
                    else:
                        x3.abaj = None

            #----------------------------------- Eliminar Nodos de Cabezales Vertical--------
            if temp_Vertic != None and temp_Vertic.getE_mail() == nom:
                if x4 != None and x4.getE_mail() == "":
                    if temp_Vertic.atras != None:
                        x4.der = temp_Vertic.atras
                        temp_Vertic.atras.izq = x4
                        if temp_Vertic.der != None:
                            temp_Vertic.atras.der = temp_Vertic.der
                            temp_Vertic.der.izq = temp_Vertic.atras
                    elif temp_Vertic.der != None:
                        x4.der = temp_Vertic.der
                        temp_Vertic.der.izq = x4
                    else:
                        x4.der = None
                        if x2 != None and x4.abaj != None:
                            x2.abaj = x4.abaj
                            x4.abaj.arrib = x2
                            x4 = None
                        elif x2 != None:
                            x2.abaj = None
                            x4 = None
                        elif x4.abaj != None:
                            x4.abaj.arrib = None
                            self.i_Vert = x4.abaj
                            x4 = None
                        else:
                            x4 = self.i_Vert = None
                elif x4 != None:
                    if temp_Vertic.delant != None:
                        if temp_Vertic.atras != None:
                            x4.atras = temp_Vertic.atras
                            temp_Vertic.atras.delant = x4
                        else:
                            x4.atras = None
                    elif temp_Vertic.atras != None:
                        x4.der = temp_Vertic.atras
                        if temp_Vertic.der != None:
                            temp_Vertic.atras.der = temp_Vertic.der
                            temp_Vertic.der.izq = temp_Vertic.atras
                        temp_Vertic.atras.izq = x4
                    elif temp_Vertic.der != None:
                        x4.der = temp_Vertic.der
                        temp_Vertic.der.izq = x4
                    else:
                        x4.der = None

    def Graficar_Dispersa(self):
        if self.esVacioH() == True or self.esVacioV() == True:
            return
        else:
            fichero_escrib = open("dispersa_edd.dot", "w")
            fichero_escrib.write("digraph G{\n")
            Horizon_temp = self.i_Horiz
            Vertica_temp = self.i_Vert
            fichero_escrib.write("\"ini\"[label = \"Ini\", style = filled, shape=box]\n")
            fichero_escrib.write("\"ini\" -> \"n" + str(Vertica_temp.getLet()) + "\"\n")
            while Vertica_temp != None:
                fichero_escrib.write("\"n" + str(Vertica_temp.getLet()) + "\"[label = \"" + str(Vertica_temp.getLet()) + "\", style = filled, shape=box]\n")
                if(Vertica_temp.abaj != None):
                    fichero_escrib.write("\"n" + str(Vertica_temp.getLet()) + "\" -> \"n" + str(Vertica_temp.abaj.getLet()) + "\"[rankdir=UD];\n")
                    fichero_escrib.write("\"n" + str(Vertica_temp.abaj.getLet()) + "\" -> \"n" + str(Vertica_temp.getLet()) + "\"\n")

                if (Vertica_temp.der != None):
                    fichero_escrib.write("\"n" + str(Vertica_temp.der.getLet()) + "," + str(
                        Vertica_temp.der.getE_mail()) + "," + str(
                        Vertica_temp.der.getDomin()) + "\"[label = \"" + str(
                        Vertica_temp.der.getE_mail()) + "\", style = filled, shape=circle]\n")
                    fichero_escrib.write("\"n" + str(Vertica_temp.getLet()) + "\" -> \"n" + str(Vertica_temp.der.getLet()) + ","+ str(Vertica_temp.der.getE_mail()) +","+ str(Vertica_temp.der.getDomin()) + "\"[constraint=false];\n")
                    fichero_escrib.write("\"n" + str(Vertica_temp.der.getLet()) + ","+ str(Vertica_temp.der.getE_mail()) +","+ str(Vertica_temp.der.getDomin()) + "\" -> \"n" + str(Vertica_temp.getLet()) + "\"[constraint=false];\n")
                    fichero_escrib.write("{rank=same; \"n" + str(Vertica_temp.getLet()) + "\"  \"n" + str(Vertica_temp.der.getLet()) + ","+ str(Vertica_temp.der.getE_mail()) +","+ str(Vertica_temp.der.getDomin()) + "\"}\n")
                    fichero_escrib.write("{rank=same; \"n" + str(Vertica_temp.der.getLet()) + ","+ str(Vertica_temp.der.getE_mail()) +","+ str(Vertica_temp.der.getDomin()) + "\"  \"n" + str(Vertica_temp.getLet()) + "\"}\n")
                    AUXtempVerti = Vertica_temp.der


                    while (AUXtempVerti.der != None):
                        fichero_escrib.write("\"n" + str(AUXtempVerti.der.getLet()) + ","+ str(AUXtempVerti.der.getE_mail()) +","+ str(AUXtempVerti.der.getDomin()) +"\"[label = \"" + str(AUXtempVerti.der.getE_mail()) + "\", style = filled, shape=circle]\n")
                        fichero_escrib.write("\"n" + str(AUXtempVerti.getLet()) + ","+ str(AUXtempVerti.getE_mail()) +","+ str(AUXtempVerti.getDomin()) + "\" -> \"n"
                                   + str(AUXtempVerti.der.getLet()) + ","+ str(AUXtempVerti.der.getE_mail()) +","+ str(AUXtempVerti.der.getDomin()) + "\"[constraint=false];\n")
                        fichero_escrib.write("\"n" + str(AUXtempVerti.dere.getLet()) + ","+ str(AUXtempVerti.der.getE_mail()) +","+ str(AUXtempVerti.der.getDomin())
                                   + "\" -> \"n" + str(AUXtempVerti.getLet()) + ","+ str(AUXtempVerti.getE_mail()) +","+ str(AUXtempVerti.getDomin()) + "\"[constraint=false];\n")
                        fichero_escrib.write("{rank=same; \"n" + str(AUXtempVerti.getLet()) + ","+ str(AUXtempVerti.getE_mail()) +","+ str(AUXtempVerti.getDomin()) + "\" \"n" + str(AUXtempVerti.der.getLet())
                                   + ","+ str(AUXtempVerti.der.getE_mail()) +","+ str(AUXtempVerti.der.getDomin()) + "\"}\n");
                        fichero_escrib.write("{rank=same; \"n" + str(AUXtempVerti.der.getLet()) + ","+ str(AUXtempVerti.der.getE_mail()) +","+ str(AUXtempVerti.der.getDomin()) + "\" \"n"
                                   + str(AUXtempVerti.getLet()) + ","+ str(AUXtempVerti.getE_mail()) +","+ str(AUXtempVerti.getDomin()) + "\"}\n");
                        AUXtempVerti = AUXtempVerti.der
                Vertica_temp = Vertica_temp.abaj


            fichero_escrib.write("\"ini\" -> \"n" + str(Horizon_temp.getDomin()) + "\"\n")
            fichero_escrib.write("{rank=same; \"ini\"  \"n" + str(Horizon_temp.getDomin()) + "\"}\n")
            while Horizon_temp != None:
                fichero_escrib.write("\"n" + str(Horizon_temp.getDomin()) + "\"[label = \"" + str(Horizon_temp.getDomin()) + "\", style = filled, shape=box]\n")
                if (Horizon_temp.der != None):
                    fichero_escrib.write("\"n" + str(Horizon_temp.getDomin()) + "\" -> \"n" + str(Horizon_temp.der.getDomin()) + "\"\n")
                    fichero_escrib.write("\"n" + str(Horizon_temp.der.getDomin()) + "\" -> \"n" + str(Horizon_temp.getDomin()) + "\"\n")
                    fichero_escrib.write("{rank=same; \"n" + str(Horizon_temp.getDomin()) + "\"  \"n" + str(Horizon_temp.der.getDomin()) + "\"}\n")
                    fichero_escrib.write("{rank=same; \"n" + str(Horizon_temp.der.getDomin()) + "\"  \"n" + str(Horizon_temp.getDomin()) + "\"}\n")

                if (Horizon_temp.abaj != None):
                    fichero_escrib.write("\"n" + str(Horizon_temp.getDomin()) + "\" -> \"n" + str(Horizon_temp.abaj.getLet()) + ","+ str(Horizon_temp.abaj.getE_mail()) +","+ str(Horizon_temp.abaj.getDomin()) + "\"[rankdir=UD];\n")
                    fichero_escrib.write("\"n" + str(Horizon_temp.abaj.getLet()) + ","+ str(Horizon_temp.abaj.getE_mail()) +","+ str(Horizon_temp.abaj.getE_mail()) + "\" -> \"n" + str(Horizon_temp.getDomin()) + "\"\n")
                    AUXtempHorizont = Horizon_temp.abaj

                    while (AUXtempHorizont.abaj != None):
                        fichero_escrib.write("\"n" + str(AUXtempHorizont.getLet()) + ","+ str(AUXtempHorizont.getE_mail()) +","+ str(AUXtempHorizont.getDomin()) + "\" -> \"n"
                                   + str(AUXtempHorizont.abaj.getLet()) + ","+ str(AUXtempHorizont.abaj.getE_mail()) +","+ str(AUXtempHorizont.abaj.getDomin()) + "\"[rankdir=UD];\n")
                        fichero_escrib.write("\"n" + str(AUXtempHorizont.abaj.getLet()) + ","+ str(AUXtempHorizont.abaj.getE_mail()) +","+ str(AUXtempHorizont.abaj.getDomin())
                                   + "\" -> \"n" + str(AUXtempHorizont.getLet()) + ","+ str(AUXtempHorizont.getE_mail()) +","+ str(AUXtempHorizont.getDomin()) + "\"\n")

                        AUXtempHorizont = AUXtempHorizont.abaj

                Horizon_temp = Horizon_temp.der

            fichero_escrib.write("}")
            fichero_escrib.close()
            os.system("dot -Tjpg dispersa_edd.dot > dispersa_edd.jpg")















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






mat = Cuerpo_Matriz()
mat.inserta("primero","p","gmail.com")
mat.inserta("segundo", "s", "hotmail.com")
mat.Graficar_Dispersa()


