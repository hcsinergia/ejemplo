#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
import gtk
import gtk.glade
import sqlite3
import re

import MySQLdb
#import pyodbc

#--Se establece la conexion con sqlite3----------------
conexion 				= sqlite3.connect("agenda.db")
conexion.text_factory 	= str
conexion.row_factory	= sqlite3.Row
cursor 					= conexion.cursor()
#------------------------------------------------------

#--Se establece la conexion con Mysql----------------
conexion 				= sqlite3.connect("test.db")
conexion.text_factory 	= str
conexion.row_factory	= sqlite3.Row
cursor 					= conexion.cursor()
#------------------------------------------------------

#--Se establece la conexion con MS SQLSERVERy----------------
conexion 				= sqlite3.connect("test.db")
conexion.text_factory 	= str
conexion.row_factory	= sqlite3.Row
cursor 					= conexion.cursor()

#"Server= CNU93230JV\\SQLEXPRESS;Database=DFC;User ID=sa;Password=123456;"


#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.17\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456')
#Driver = Easysoft ODBC-SQL Server

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.11\SQLEXPRESS;Database=DFC;User ID=sa;Password=123456')
#cnxn = pyodbc.connect("Driver={SQL Server};Server='192.168.0.17\SQLEXPRESS',Database='DFC',User ID='sa',Password='123456'") 





#import pyodbc
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.20\SQLEXPRESS;DATABASE=DFC;UID=sa;Password=123456')

#conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=testserver\mssql2008;DATABASE=eoffice;UID=erp;PWD=123;') 
#cnxn = 	pyodbc.connect(host='192.168.0.20\SQLEXPRESS',
#						user='sa',
#						password='123456',
#						database='DFC')

#TrustedConnection=Yes")
#cursor = cnxn.cursor()
#cursor.execute("select apellido from agente where id = 2")
#rows = cursor.fetchall()
#for row in rows:
#    print row.user_id, row.user_name

#    print "No he podido conectar con base de datos SQLServer!"
    
    # Cerramos cursor y conexión.
#print "Cerrando conexiones!"
#cnxn.close()


#[MSSQL-PYTHON]
#Driver                  = Easysoft ODBC-SQL Server
#Server                  = my_machine\SQLEXPRESS
#User                    = my_domain\my_user
#Password                = my_password
# If the database you want to connect to is the default
# for the SQL Server login, omit this attribute
#Database                = Northwind




import pymssql
conn = pymssql.connect(host='192.168.0.20\SQLEXPRESS', user='sa', password='123456', database='DFC')

cur = conn.cursor()
#cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
#cur.executemany("INSERT INTO persons VALUES(%d, %s)", \
#    [ (1, 'John Doe'), (2, 'Jane Doe') ])
#conn.commit()  # you must call commit() to persist your data if you don't set autocommit to True

cur.execute('select * from agente where id = 2')
row = cur.fetchone()
while row:
    print "ID=%d, Name=%s" % (row[0], row[1])
    row = cur.fetchone()

# if you call execute() with one argument, you can use % sign as usual
# (it loses its special meaning).
#cur.execute("SELECT * FROM persons WHERE salesrep LIKE 'J%'")

conn.close()























#------------------------------------------------------





class Agenda:
	def __init__(self):
		
		#Configuramos las variables para nuestra ventana-------
		self.wTree 	= gtk.glade.XML("agenda.glade")
		#------------------------------------------------------
		
		#Configuramos los eventos mediante un diccionario de señales--
		dict = {"on_window1_delete_event":self.cerrar,
				"on_nombre_changed":self.nombreM,
				"on_apellido_changed":self.apellidoM,
				"on_buscar_clicked":self.buscar,
				"on_celular_changed":self.numCelular,
				"on_contactos_cursor_changed":self.copiaContactos,
				"on_agregar_clicked":self.agregar,
				"on_todos_clicked":self.todos2,
				"on_atras_clicked":self.todos3,
				"on_siguiente_clicked":self.todos4,
				"on_modificar_clicked":self.modificar,
				"on_borrar_clicked":self.borrar}
		self.wTree.signal_autoconnect(dict)		
		#------------------------------------------------------
		
		#Configuramos las variables de widget------------------
		self.id 		= self.wTree.get_widget("id")
		self.nombre 	= self.wTree.get_widget("nombre")
		self.apellido 	= self.wTree.get_widget("apellido")
		self.codigo 	= self.wTree.get_widget("codigo")
		self.celular 	= self.wTree.get_widget("celular")
		self.email 		= self.wTree.get_widget("email")
		self.contactos 	= self.wTree.get_widget("contactos")
		self.label		= self.wTree.get_widget("label")
		self.nombre.grab_focus()
		self.tree()
		self.blanco()
		self.fCodigo()
		self.todos(1)
		#------------------------------------------------------















	#Creamos la columna para contactos ---------------------
	def tree(self):
		self.llenatree("Id",0)
		self.llenatree("Nombre",1)
		self.llenatree("Apellido",2)
		self.llenatree("Celular",3)
		self.llenatree("Email",4)
		self.lista = gtk.ListStore(str, str, str, str,str)
		self.contactos.set_model(self.lista)		
	#-------------------------------------------------------
	
	#Método para llenar el treeview con sus respectivas columnas -------------------
	def llenatree(self, titulo, columnId):
		column = gtk.TreeViewColumn(titulo, gtk.CellRendererText(), text = columnId)
		column.set_resizable(True)		
		column.set_sort_column_id(columnId)
		self.contactos.append_column(column)
	#-------------------------------------------------------------------------------
	#Método para visualizar el contacto recién ingresado---------------------------
	def contacto(self,id):
		self.lista.clear()
		cursor.execute("SELECT * FROM contactos WHERE id = '"+id+"'")
		query = cursor.fetchall()
		[self.lista.append([x['id'],x['nombre'],x['apellido'],x['celular'],x['email']]) for x in query]
	#----------------------------------------------------------------------------------------------------	
	
	#Método para visualizar en el treeview los contactos.. dependera de la cantidad de contactos-----------
	def todos(self,num):
		self.lista.clear()
		self.num = num
		self.num2 = self.num + 9
		self.label.set_text("Contactos "+str(self.num)+" hasta "+str(self.num2)+"")
		cursor.execute("SELECT * FROM contactos WHERE id BETWEEN "+str(self.num)+" and "+str(self.num2)+"")
		query = cursor.fetchall()
		if query == []:
			self.error("No se encuentran mas datos")
			self.blanco()
		else:
			[self.lista.append([x['id'],x['nombre'],x['apellido'],x['celular'],x['email']]) for x in query]
	#--------------------------------------------------------------------------------------------------------		
	#Métodos para visualizar treeview de contactos. todos, atras y siguiente.	
	#Permite visualizar de 10 en 10 los resultados de sqlite3 de la tabla contactos.
	def todos2(self, *args):
		self.todos(1)
	
	def todos3(self, *args):
		if self.num == 1:
			num = 1
		else:
			num = self.num - 10
		self.todos(num)
	
	def todos4(self, *args):
		self.todos(self.num + 10)
	#--------------------------------------------------------------------------	

			
		
	#Método para colocar los widgets en blanco----------------------
	def blanco(self):
		self.id.set_text("0")
		self.nombre.set_text("")
		self.apellido.set_text("")
		self.celular.set_text("")
		self.email.set_text("")	
	#----------------------------------------------------------------
	
	#Método para llenar lista desplegable código---------------------
	def fCodigo(self):
		cursor.execute("SELECT * FROM codigos ORDER BY id")
		query = cursor.fetchall()
		[self.codigo.append_text(str(x['codigo'])) for x in query]
		self.codigo.set_active(0)
	#---------------------------------------------------------------
	
	#Método para llenar los contactos---------------------------------------------------------
	def buscar(self, widget):
		self.lista.clear()
		sql="SELECT * FROM contactos WHERE id > 0 "#nos permite asignar nuevos AND a la consulta.
		if self.nombre.get_text() == "" and self.apellido.get_text() == "" and self.email.get_text() == "":
			self.lista.clear()
		else:
			if self.nombre.get_text() != "":
				sql+="AND nombre LIKE '"+self.nombre.get_text()+"%'"
			if self.apellido.get_text() != "":
				sql+="AND apellido LIKE '"+self.apellido.get_text()+"%'"
			if self.email.get_text() != "":
				sql+="AND email LIKE '"+self.email.get_text()+"%'"
			cursor.execute(sql)
			query = cursor.fetchall()
			if query != []:
				self.lista.clear()
				[self.lista.append([x['id'],x['nombre'],x['apellido'],x['celular'],x['email']]) for x in query]
			else:
				self.aviso("No existe el contacto...")
				self.blanco()
				self.lista.clear()
	#-------------------------------------------------------------------------------------------------------		
	
	#Método para que solo puedan introducirse mayúsculas en nombre -----------------------------------	
	def nombreM(self, *args):
		self.nombre.set_text(self.nombre.get_text().upper()) 
	#-----------------------------------------------------------------------------------------------
	
	#Método para que solo puedan introducirse números en el celular -----------------------------------	
	def numCelular(self, *args):
		self.celular.set_text(("".join([i for i in self.celular.get_text() if i in "0123456789"]))) 
	#-----------------------------------------------------------------------------------------------	
	
	#Método para que solo puedan introducirse mayúsculas en el apellido---	
	def apellidoM(self, *args):
		self.apellido.set_text(self.apellido.get_text().upper())
	#--------------------------------------------------------------------	
		
	#Método para llenar los campos que vienen de contactos
	def copiaContactos(self, widget):
		i, j = self.contactos.get_selection().get_selected()
		self.idcontactos = i.get_value(j,0)
		self.id.set_text(str(self.idcontactos))
		cursor.execute("SELECT * FROM contactos WHERE id = '"+self.idcontactos+"'")
		query = cursor.fetchone()
		self.nombre.set_text(str(query['nombre']))
		self.apellido.set_text(str(query['apellido']))
		self.celular.set_text(str(query['celular'][4:]))
		self.email.set_text(str(query['email']))
		cursor.execute("SELECT id FROM codigos WHERE codigo = '"+query['celular'][:4]+"'")
		query2 = cursor.fetchone()
		self.codigo.set_active(int(query2['id']-1))
	#-----------------------------------------------------	

	#Método para agregar/moficar contactos-----------------------------------------------
	def agregar_modificar(self, tipo):
		if tipo == 1:
			sql 	= "INSERT INTO contactos (nombre,apellido,celular,email)\
					  VALUES('"+self.nombre.get_text()+"','"+self.apellido.get_text()+"',\
					  '"+self.codigo.get_active_text()+""+self.celular.get_text()+"','"+self.email.get_text()+"')"
			mensaje = "¿Está seguro que desea agregar a "+self.nombre.get_text()+" "+self.apellido.get_text()
			sql2 	= "SELECT MAX(id) as var FROM contactos"
			self.valCel = self.fValCel()
			
			
		if tipo == 2:
			sql 	= "UPDATE contactos SET\
					  nombre = '"+self.nombre.get_text()+"', apellido = '"+self.apellido.get_text()+"',\
					  celular = '"+self.codigo.get_active_text()+""+self.celular.get_text()+"',email = '"+self.email.get_text()+"'\
					  WHERE id = '"+self.id.get_text()+"'"
			mensaje = "¿Está seguro que desea moficar a "+self.nombre.get_text()+" "+self.apellido.get_text()
			sql2 	= "SELECT id as var FROM contactos WHERE id = '"+self.id.get_text()+"'"
			self.valCel = 0
				
		cantidadCelular = len(self.celular.get_text())
		#Expresión regular para colocar un correo válido
		if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',self.email.get_text().lower()):
			valCorreo = 1
		else:
			valCorreo = 0
		if self.nombre.get_text() == "" or self.apellido.get_text() == "" or self.email.get_text() == "" or self.celular.get_text() == ""  or len(self.celular.get_text()) < 7 or valCorreo == 0 or self.valCel == 1:
			self.error(" No se puede agregar/modificar ya que \n Algún campo está en blanco \n El correo es inválido \n El celular tiene menos de 7 digitos\n Ya existe el número telefónico")
		else:
			
			dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
			gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO,mensaje)
			if dialog.run() == gtk.RESPONSE_YES:
				cursor.execute(sql)
				if cursor.rowcount < 1:
					self.error("Error al modificar debe seleccionar el contacto de la lista")
				else:
					conexion.commit()
					cursor.execute(sql2)
					query = cursor.fetchone()
					self.contacto(str(query['var']))
					self.id.set_text(str(query['var']))
					dialog.destroy()
			else:
				self.aviso("No hay cambios...")
				dialog.destroy()
	#---------------------------------------------------------------------------
	#Métodos para identificar en el método agregar_modificar si se insertan o se modifican contactos
	def agregar(self, *args):
		self.agregar_modificar(1)
	
	def modificar(self, *args):
		self.agregar_modificar(2)
	#-------------------------------------------------------------------------------------------------
	
	#Método para borrar contactos---------------
	def borrar(self, *args):
		if int(self.id.get_text()) == 0:
			self.error("Para borrar necesita seleccionar un contacto de la lista")
		else:
			mensaje = "¿Está seguro que desea borrar al contacto "+self.nombre.get_text()+" "+self.apellido.get_text()+""
			sql = "DELETE FROM contactos WHERE id = '"+self.id.get_text()+"'"
			dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
			gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO,mensaje)
			if dialog.run() == gtk.RESPONSE_YES:
				cursor.execute(sql)
				if cursor.rowcount < 1:
					self.error("Error al borrar al contacto ")
				else:
					conexion.commit()
					dialog.destroy()
					self.todos(1)
					self.blanco()
			else:
				self.aviso("No hay cambios...")
				dialog.destroy()
			
	#-------------------------------------------
	#Método para validar que no se repitan los celulares.
	def fValCel(self):
		cursor.execute("SELECT celular FROM contactos")
		query = cursor.fetchall()
		listaCel = [x['celular'] for x in query]
		celcomp = self.codigo.get_active_text()+self.celular.get_text()
		if celcomp in listaCel:
			valCel = 1
		else:
			valCel = 0
		return valCel
			
	#Método que nos indica si queremos cerrar la ventana-----------------------
	def cerrar(self, *args):
		dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
		gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO,"¿Está seguro que desea salir?")
		if dialog.run() == gtk.RESPONSE_YES:
			ret = gtk.main_quit()
		else:
			ret = 1
			dialog.destroy()
		return ret
	#---------------------------------------------------------------------------

	#Método para que aparezca un diálogo de advertencia-------------------------------
	def aviso(self, mensaje, *args):
		dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
		gtk.MESSAGE_WARNING, gtk.BUTTONS_OK,mensaje)
		dialog.run()
		dialog.destroy()
	#----------------------------------------------------------------------------------
	
#Método para que aparezca un diálogo de error------------------------------
	def error(self, mensaje, *args):
		dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
		gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,mensaje)
		dialog.run()
		dialog.destroy()
	#----------------------------------------------------------------------------------
	
	#Método para que aparezca un diálogo de información (querys)-------------------------------
	def informacion(self, mensaje, *args):
		dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,\
		gtk.MESSAGE_INFO, gtk.BUTTONS_OK,mensaje)
		dialog.run()
		dialog.destroy()
	#----------------------------------------------------------------------------------
	
	


if __name__ == "__main__":
	agenda = Agenda()
	gtk.main()
