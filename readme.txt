
# Project name: CRUD en Python 3.7.3 y SQLite 3
***
	- Desarrollo de un CRUD (C.L.I.) con Python 3.7.3 y SQLite 3 en GNU/Linux Debian 10.


## General info
***
	- Migración de Python 2.7 a la versión 3.7.3.
	- Marzo de 2019 Versión 1.0
	- U.I. en C.L.I. - Script en Python 3.7.3 como A. B. M. con base de datos en SQlite3
	- Sobre el sistema de base GNU/Debian 10.
	- PABLO MUSSIS


### Author developer
***
Pablo Mussis
	- gitlab @pablomussis
	- github @pablomussis


### Nota:
***
Nota: 
 OK - Verificar el sistema operativo base para ejecutar el comando clear en equipos UNIX o cls en M.Windows.
 OK al 70% - Modularizar tareas.
 X - Mejorar la salida de consulta en la opción 1.

### Estructura de la base de datos
***
Base: 	contacto
Tabla: 	contactos
campos 	id INTEGER PRIMARY KEY AUTOINCREMENT 
		nombre TEXT NOT NULL	(nombre completo)
		contacto TEXT NOT NULL	(email, teléfono movil, etc)

### Ejecución del programa
***
Terminal o símbolos de sistema
$ python3 main.py