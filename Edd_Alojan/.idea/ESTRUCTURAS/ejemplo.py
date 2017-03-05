__author__ = 'Samuel'

from flask import Flask, request, Response
from Estruct_Lineal import *

#------------------- Conexion Flask Lista_Metodos ------------------
app = Flask("EDD_codigo_ejemplo")
a = Metodo_Lista()
#Metodo Agregar a la lista
@app.route('/metodoWeb', methods=['POST'])
def hello():
	parametro = str(request.form['dato'])
	a._Inserta_Nodo(parametro)
	#dato2 = str(request.form['dato2'])
	a._Mostrar()
	a.grafica_Lista()
	#return  'Hola ' + str(parametro) + ' saludos!'i
	return 'Agregar Exito'

#Metodo Borrar
@app.route('/web_met_b', methods=['POST'])
def Elim_webL():
	borr_l = str(request.form['dat'])
	a._Eliminar_N(borr_l)
	a._Mostrar()
	a.grafica_Lista()
	return 'Exito delete'

#Metodo Buscar
@app.route('/web_met_bu', methods=['POST'])
def Bus_webL():
	bus_l = str(request.form['dat_bu'])
	a._Buscar(bus_l)
	a._Mostrar()
	a.grafica_Lista()
	return 'Encontrar Cadena'


#------------------- Conexion Flask Cola_Metodos ------------------
#Metodo Meter/Enqueue
b = Metodo_Cola()
@app.route('/web_Enque', methods=['POST'])
def Enque():
	cad_m = int(str(request.form['c_dat']))
	b._Enqueue(cad_m)
	b.Mostrar_C()
	b.Graficar_Cola()
	return 'Exito Agregado'

#Metodo Sacar/queue
@app.route('/web_Que', methods=['POST'])
def Deque():
	b.Queue()
	b.Mostrar_C()
	b.Graficar_Cola()
	return 'Eliminar Exito'



#-------------------- Conexion Flask Pila_Metodos--------------------
c = Metodo_Pila()
#Metodo meter en Pila
@app.route('/web_pila', methods=['POST'])
def Pila_M():
	cad_P = int(str(request.form['dat_met']))
	c.Meter(cad_P)
	c.Mostrar_P()
	c.Graficar_Pila()
	return 'Agregardo Digito'

#Metodo sacar en Pila
@app.route('/web_pila', methods=['POST'])
def Elimin_P():
	c.Sacar()
	c.Mostrar_P()
	c.Graficar_Pila()
	return 'Digito eliminado Pila'

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

#---------------------------------------------------------------------
#---------------- FIN DEL WEB SERVICE FLASK --------------------------















# @app.route("/e")
# def hellof():
# 	return "Hello World2!"

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
# class Usuario():
#     def __init__(self, password, correo, nombre):
#         self.nombre = nombre
#         self.password = password
#         self.correo = correo
