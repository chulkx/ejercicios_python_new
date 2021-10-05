#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:36:02 2021

@author: chulke
"""

#Ejercicio 8.6

import os
import sys
import datetime as dt
import fnmatch

def procesar_nombre(ruta_archivo, name):
    ''' 
    Recibe una ruta de archivo y el nombre actual del mismo sin la extension png.
    Determina las nuevas fechas de modificacion y acceso.
    Devuelve al nuevo nombre a usar, y las nuevas fechas de modificacion y acceso.
    '''
    fecha = ruta_archivo[len(ruta_archivo)-12:len(ruta_archivo)-4]  #determino el string para obtener la fecha
    
    ''' Genero los objetos datetime para devolverlos en el return '''
    fecha_acceso = dt.datetime(year = int(fecha[0:4]), 
                               month = int(fecha[4:6]), 
                               day = int(fecha[6:]))
    fecha_modif = dt.datetime(year = int(fecha[0:4]), 
                              month = int(fecha[4:6]), 
                              day = int(fecha[6:]))
    
    ''' Genero el nuevo nombre con eo que guardar el archivo '''
    nuevo_nombre = name[:-13]+'.png'
    
    return nuevo_nombre,fecha_acceso, fecha_modif
    


def procesar(dir_orig, dir_nuevo):
    '''
    Recibe las rutas de la ubicacion actual de los archivos y la ubicacion nueva.
    Usa la funcion procesar_nombre() para determinar el nuevo nombre y las fechas de modificacion y acceso.
    Crea la nueva carpeta donde iran los archivos movidos.
    Borra las carpetas que quedaron vacias.
    '''
    dir_actual = os.getcwd()
    
    '''Creacion del nuevo directorio. '''
    try:
        os.mkdir(dir_nuevo)
    except OSError:
        pass
    
    os.chdir(dir_actual)
    
    '''Recorre el arbol del directorio para encontrar los archivos '''
    for root, dirs, files in os.walk(dir_orig):
        for name in files:
            if fnmatch.fnmatch(name, '*.png'):  #verifica si el nombre del archivo es del tipo *.png
                nuevo_nombre, f_acceso, f_modif = procesar_nombre(os.path.join(root, name), name)   #Llamado a la funcion procesar_nombre()
                os.rename(os.path.join(root, name), os.path.join(dir_nuevo, nuevo_nombre))  #Mueve los archivos cambiando sus nombres
                ts_acceso = f_acceso.timestamp()    #timestamp para fecha de acceso y modificacion
                ts_modifi = f_modif.timestamp()
                os.utime(os.path.join(dir_nuevo, nuevo_nombre), (ts_acceso, ts_modifi)) #Modificacion de los stats del archivo
    
    '''Recorre nuevamente el arbol en busca de los directorios que quedaron vacios y los elimina '''
    for root, dirs, files in os.walk(dir_orig):
        if files == [] and dirs == []:
            print('Directorios vacios eliminados --> ' + root)  #informa por pantalla las rutas de los directorios vacios eliminados
            os.rmdir(root)
    return

if __name__ == '__main__':
    if len(sys.argv) == 3:
        procesar(sys.argv[1], sys.argv[2])

