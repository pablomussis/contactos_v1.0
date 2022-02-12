#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
 - MÓDLULO PARA IMPRIMIR LA INTERFAZ DE USUARIO POR LINEA DE COMANDO: C.L.I.

 - Migración de Python 2.7 a la versión 3.7.3.
 - Marzo de 2019 Versión 1.0
 - U.I. en C.L.I. - Script en Python 3.7.3 como A. B. M. con base de datos en SQlite3
 - Sobre el sistema de base GNU/Debian 10.
 - PABLO MUSSIS
'''

def ImprimirMenu():
	# Ingresamos una cadena de caracteres a la variable menu:
	menu = '''LISTADO DE CONTACTOS \n\n
			SELECCIONE UNA OPCIÓN: \n\n
			1. CONSULTA
			2. MODIFICACIÓN
			3. ALTA
			4. BAJA
			5. SALIR \n\n'''

	# Imprimimos las opciones de la aplicación
	print ('\n' * 2, '\t' * 4, ('=' * 50), '\n' * 2)
	print ('\t' * 4, menu)
	print ('\t' * 4, ('=' * 50))
