#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sudo aptitude install unixodbc unixodbc-dev freetds-dev tdsodbc python-dev

import pygtk
import gtk
#~ import gtk.glade

import re

import sqlite3
import MySQLdb
import pyodbc


#--Se establece la conexion con sqlite3----------------NO ESTA ANDANDO
#~ Conexion	= sqlite3.connect("gestion.db")
#~ micursor 	= Conexion.cursor()
#~ micursor.execute("SELECT id, apellido, nombre1, nombre2, legajo FROM gestion.agente" )
# seleccionamos elemento con el ID indicado por el usuario
#~ num_reg 	= micursor.rowcount # contamos número de elementos
#~ print num_reg
#~ rows 	= micursor.fetchall()
#~ for row in rows:
	#~ print row[0], row[1], row[2], row[3]
	
	
#~ Conexion 				= sqlite3.connect("gestion.db")
#~ Conexion.text_factory 	= str
#~ Conexion.row_factory	= sqlite3.Row
#~ cursor 					= Conexion.cursor()
#~
#~ cur.execute('SELECT id, apellido, nombre1, nombre2, legajo FROM agente')
#~ row = cur.fetchone()
#~ while row:
    #~ print "id=%d, apellido=%s, nombre1=%s, nombre2=%s, legajo=%s" % (row[0], row[1], row[2], row[3])
    #~ row = cur.fetchone()
#------------------------------------------------------


#~ #--Se establece la conexion con Mysql----------------Probado OK
#~ Conexion = MySQLdb.connect(host="localhost", user="root", passwd = "123456", db= "clientes")
# conectamos a la base de datos
#~ micursor = Conexion.cursor()
#~ micursor.execute("SELECT NYAPE, DIRECCION, TELEFONO FROM clientes.clientes limit 100" )
# seleccionamos elemento con el ID indicado por el usuario
#~ num_reg = micursor.rowcount # contamos número de elementos
#~ print num_reg
#~ rows = micursor.fetchall()
#~ for row in rows:
	#~ print row[0], row[1], row[2]
#------------------------------------------------------

#Probado conecta ok y lista agentes desde server gdtbase ------------------

#string virtual
#cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.0.24\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456;')

#string en ARBA
	#cnxn = pyodbc.connect('DRIVER={FreeTDS};Server=10.25.49.117\gdtbase;Database=DFC;UID=sa;PWD=123456;TDS_Version=8.0;Port=1433;')

	#~ cursor = cnxn.cursor()
	#~ cursor.execute("SELECT apellido, nombre1 FROM agente")
	#~ rows = cursor.fetchall()
	#~ for row in rows:
		#~ print row.apellido, row.nombre1
#-----------------------------------------------------------------------


#--Se establece la conexion con Mysql----------------Probado OK -- desarrollo paralelo
Conexion = MySQLdb.connect(host="localhost", user="root", passwd = "123456", db= "clientes") # conectamos a la base de datos
Conexion.text_factory 	= str

micursor = Conexion.cursor()
#~ micursor.execute("SELECT id, apellido, nombre1, nombre2, legajo FROM agente" ) # seleccionamos elemento con el ID indicado por el usuario
#~ num_reg = micursor.rowcount # contamos número de elementos
#~ print num_reg
#~ rows = micursor.fetchall()
#~ for row in rows:
	#~ print row[0], row[1], row[2]
	

	
class Gestion(object):
	
	def __init__(self):
	
	# Se carga el archivo glade con la ventana
		objsW = gtk.Builder()
		objsW.add_from_file('vistas/pruebaPantalla1.glade')

		# Se recuperan los widget a usar (no son necesarios todos)
		self.winMain = objsW.get_object('winMain')
		self.tree
		self.todos(1)
		# acceder al boton
		#self.button1 = objsW.get_object('butoon1')

		# Se asocian las senales del archivo glade a metodos de la clase
		objsW.connect_signals(self)
		self.winMain.show()
			
	def on_winMain_destroy(self, widget):
		#esto cierra todas las ventanas de la aplicacion
		gtk.main_quit()

		#Configuramos las variables para nuestra ventana-------
		self.winMain 	= gtk.glade.XML("pruebaPantalla1.glade")

	#Creamos la columna para contactos ---------------------
	def tree(self):
		self.llenatree("id",0)
		self.llenatree("nombre",1)
		self.llenatree("apellido1",2)
		self.llenatree("apellido2",3)
		self.llenatree("legajo",4)
		self.lista = gtk.ListStore(str, str, str, str,str)
		self.treeview1.set_model(self.lista)		
	#-------------------------------------------------------
	
	#Método para llenar el treeview con sus respectivas columnas -------------------
	def llenatree(self, titulo, columnId):
		column = gtk.TreeViewColumn(titulo, gtk.CellRendererText(), text = columnId)
		column.set_resizable(True)		
		column.set_sort_column_id(columnId)
		self.treeview1.append_column(column)
	#-------------------------------------------------------------------------------
	
	#Método para visualizar en el treeview los contactos.. dependera de la cantidad de contactos-----------
	def todos(self,num):
		self.lista.clear()
		self.num = num
		self.num2 = self.num + 9
		self.label.set_text("Contactos "+str(self.num)+" hasta "+str(self.num2)+"")
		cursor.execute("SELECT id, apellido, nombre1, nombre2, legajo FROM agente "+str(self.num)+" and "+str(self.num2)+"")
		query = cursor.fetchall()
		if query == []:
			self.error("No se encuentran mas datos")
			self.blanco()
		else:
			[self.lista.append([x['id'],x['nombre'],x['apellido'],x['legajo'],x['email']]) for x in query]
	
	
	
if __name__ == "__main__":
	gestion = Gestion()
	gtk.main()
