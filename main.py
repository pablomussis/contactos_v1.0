#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
 - Migración de Python 2.7 a la versión 3.7.3.
 - Marzo de 2019 Versión 1.0
 - U.I. en C.L.I. - Script en Python 3.7.3 como A. B. M. con base de datos en SQlite3
 - Sobre el sistema de base GNU/Debian 10.
 - PABLO MUSSIS


Nota: 
	OK - Verificar el sistema operativo base para ejecutar el comando clear en equipos UNIX o cls en M.Windows.
	OK 70% - Modularizar tareas.
	X - Mejorar la salida de consulta en la opción 1.
'''

import limpiar as lp						# Módulo personal para limpiar la terminal UNIX o simbolo de sistemas de M.W.
import ui									# Módulo personal que imprime la U.I.: Interfaz de Usuario.
#import conexion as con						# Módulo personal que carga y pone activa la base de datos en SQLite.

import sys
import os

import sqlite3


class contacto:

	#def limpiar_pantalla(self) :
	#	os.system('clear')	# Limpia la pantalla | en Windows el comando es 'cls'
	
	lp.Pantalla()							# Limpia la pantalla (clear o cls), determina sobre que sistema operativo está corriendo el script.
	ui.ImprimirMenu()						# Imprime la UI

	
	# Función que imprime el menu a seleccionar por el usuario:
	#def imprimir_menu(self) :
		# Ingresamos una cadena de caracteres a la variable local menu:		
	#	menu = '''LISTADO DE CONTACTOS: \n\n
	#			SELECCIONE UNA OPCIÓN: \n\n
	#			1. CONSULTA
	#			2. MODIFICACIÓN
	#			3. ALTA
	#			4. BAJA
	#			5. SALIR \n\n'''

	#	print ('\n' * 2, '\t' * 4, ('=' * 50), '\n' * 2)
	#	print ('\t' * 4, menu)
	#	print ('\t' * 4, ('=' * 50))
	

	# Función que carga y pone activa la base de datos (contacto.db) con su tabla (contactos):
	def cargar_base(self) :
		# Crea, si no existe, y conecta con la base de datos en la dirección indicada:
		self.conexion = sqlite3.connect("contacto.db") #Añadir ruta del archivo "contacto.db" para que funcione correctamente
		# Con cursor manejaremos la base de datos conectada:
		self.cursor = self.conexion.cursor()
		# Con cursor.execute ejecutaremos sentencias de SQLite3 y SQL
		self.cursor.execute("CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, contacto TEXT NOT NULL)")

	#con.cargarBase()

	def leer_opcion(self) :		# Función que COMPRUEBA VALIDACION DE DATOS de entrada
		while True :
			try :
				self.opcion = int(input('\n\t\t\t\tINGRESE UNA OPCIÓN: '))
				#self.limpiar_pantalla()
				lp.Pantalla()
				if (self.opcion < 6) :
					break
			except ValueError :
				print ('\n', '\t' * 4, 'INTENTE NUEVAMENTE..!')

	def comprobar_opcion(self) :	# Función que COMPRUEBA OPCION de menu
		lp.Pantalla()
		#self.limpiar_pantalla()

		if (self.opcion == 1) :
			print ('\n', '\t' * 4, 'CONSULTA DE REGISTROS: \n')
			self.cursor.execute("SELECT * FROM contactos")
			tupla_registro = self.cursor.fetchall() # Asignación a la tupla registro

			if (tupla_registro) :	# Imprime todos los registros SI EXISTEN
				for registros in (tupla_registro) :
					print ('\t' * 4, registros)
				#hlen = len(self.cursor) / 2
				#for i, t in enumetate(zip(self.cursor, self.cursor[hlen:])) :
					#	print '({0:>2}) {2:>3}	({1}) {3:>3}'.format(i, i + hlen, * t)
			else :
				print ('\n', '\t' * 4, 'NO HAY REGISTROS A MOSTRAR ..!\n')



		elif (self.opcion == 2) :
			print ('\n', '\t' * 4, 'MODIFICACIÓN DE REGISTROS \n')
			id = int(input('\t\t\t\tINGRESE EL N° DE ID DEL REGISTRO: '))

			# Selecciona el registro único si existe:
			self.cursor.execute("SELECT nombre, contacto, id FROM contactos WHERE id = %d" %(id))
			tupla_registro = self.cursor.fetchone() # Asignación a la tupla registro

			if (tupla_registro) :
				print ('\n', '\t' * 4, tupla_registro )

				nombre = input('\n\t\t\t\tINGRESE EL NUEVO NOMBRE: ')
				contacto = input('\t\t\t\tINGRESE EL NUEVO CONTACTO: ')

				if (nombre) and (contacto) : # modificar ambos
					tupla_registro = (nombre, contacto, id)
					self.cursor.execute("UPDATE contactos SET nombre = ?, contacto = ? WHERE id = ?", tupla_registro)
				elif (nombre) and not(contacto) : # sólo modificar contacto
					tupla_registro = (nombre, id)
					self.cursor.execute("UPDATE contactos SET nombre = ? WHERE id = ?", tupla_registro)
				elif not(nombre) and (contacto) :
					tupla_registro = (contacto, id)
					self.cursor.execute("UPDATE contactos SET contacto = ? WHERE id = ?", tupla_registro)
				self.actualizar_base()
				#con.actualizarBase()
				print ('\n', '\t' * 4, 'LOS DATOS SE MODIFICARON CORRECTAMENTE..!\n')
			else:
				print ('\n', '\t' * 4, 'NO HAY REGISTROS A MODIFICAR..!')

		elif (self.opcion == 3):

			print ('\t' * 4, 'ALTA DE REGISTROS: \n')
			nombre = input('\t\t\t\tINGRESE UN NOMBRE: ')
			contacto = input('\t\t\t\tINGRESE UN CONTACTO: ')
			# Tupla (alta) que contiene los nuevos datos:
			alta = (nombre, contacto)

			# Inserta y actualiza (función actualizarBase()) los nuevos registros de la base:
			self.cursor.execute("INSERT INTO contactos (nombre, contacto) VALUES (?, ?)", alta)
			self.actualizar_base()
			#con.actualizarBase()
			print ('\n', '\t' * 4, 'LOS DATOS SE INSERTARON CORRECTAMENTE..!\n')


		elif (self.opcion == 4) :

			print ('\t' * 4, 'BAJA DE REGISTROS: \n')
			id = int(input('\t\t\t\tINGRESE ID PARA DAR LA BAJA: '))

			# Selecciona el registro único si existe:
			self.cursor.execute("SELECT * FROM contactos WHERE id = %d" %(id))

			if (self.cursor.fetchone()) :
				# Elimina y actualiza (función actualizarBase()) el registro de la base:
				self.cursor.execute("DELETE FROM contactos WHERE id = %d" %(id))
				self.actualizar_base()
				#con.actualizarBase()
				print ('\n', '\t' * 4, 'LOS DATOS SE ELIMINARON CORRECTAMENTE..!\n')
			else :
				print ('\n', '\t' * 4, 'NO HAY REGISTRO A DAR DE BAJA\n')


		elif (self.opcion == 5) :
			#self.limpiar_pantalla()
			lp.Pantalla()
			self.cerrar_base()
			#con.cerrarBase()

		ui.ImprimirMenu()
		self.leer_opcion()
		self.comprobar_opcion()

	def actualizar_base(self) :
		self.conexion.commit()
	#con.actualizarBase()

	def cerrar_base(self) :
		self.conexion.close()
		exit()
	#con.cerrarBase()

	def __init__(self) :
		#self.limpiar_pantalla()
		lp.Pantalla()
		#self.imprimir_menu()
		ui.ImprimirMenu()
		self.cargar_base()
		#con.cargarBase()
		self.leer_opcion()
		self.comprobar_opcion()

contactos = contacto()	# La clase contacto() INSTANCIA al objeto menu

