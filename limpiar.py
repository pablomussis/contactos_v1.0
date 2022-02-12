#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
 - MÓDULO PARA LIMPIAR LA PANTALLA SEGÚN EL SISTEMA OPERATIVO.

 - Migración de Python 2.7 a la versión 3.7.3.
 - Marzo de 2019 Versión 1.0
 - U.I. en C.L.I. - Script en Python 3.7.3 como A. B. M. con base de datos en SQlite3
 - Sobre el sistema de base GNU/Debian 10.
 - PABLO MUSSIS
'''

import platform								# Módulo que retorna el nombre del S.Op.
import os									# Móludo que ejecuta comandos de la función system()

def Pantalla() :
	if platform.system() == 'Windows' :
		os.system('cls')					# Limpia la pantalla en Windows 
	else :
		os.system('clear')					# Limpia la pantalla en S.Op. de la familia UNIX
