#!/usr/bin/env python

"""
Created on Tue Sep 21 20:02:25 2021

@author: chulke
"""
# Ejercicio 9.3 - 9.4

import sys
import lote
import formato_tabla
from fileparse import parse_csv


    
# Funcion leer_camion modificada Clase 9
def leer_camion(nombre_archivo):
    '''Lee un archivo csv usando el modulo fileparse.
    Devuelve una lista de instancias de la clase Lote importada'''
    
    with open(nombre_archivo) as iterable:
        camion_dicts = parse_csv(iterable, types = [str, int, float], has_headers = True)
        
        '''Creo las instancias de la clase Lote'''
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

# Funcion leer_precios modificada
def leer_precios(nombre_archivo):
    '''Lee un archivo csv usando el modulo fileparse.'''
    with open(nombre_archivo) as iterable:
        precios = parse_csv(iterable, types = [str, float], has_headers = False)
        precios = dict(precios)
    return precios

# Funcion que genera la lista para el informe
def hacer_informe(camion, precios):
    '''Genera la lista para el informe'''
    lista = []
    for lot in camion:
        precio_venta = precios[lot.nombre]
        cambio = precio_venta - lot.precio
        t = (lot.nombre, lot.cajones, lot.precio, cambio)
        lista.append(t)
    return lista

# # Funcion que imprime el informe en consola
# def imprimir_informe(informe):
#     '''Imprime el informe'''
#     print('    Nombre    Cajones     Precio     Cambio')
#     print('---------- ---------- ---------- ----------')
#     for nombre, cajones, precio, cambio in informe:
#         precio = f'${f"{precio:.2f}"}'
#         print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

'''Redefino la funcion imprimir_informe para que funcione con formato_tabla'''
def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas con
    (nombre, cajones, precio, diferencia)
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
    
    
# Funcion que hace el llamado al resto de funciones
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    '''Funcion de alto nivel que llama al resto de funciones'''
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    '''creo el formateador'''
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)

def f_principal(param):     #el 7.4
    if len(param) != 4:     #compruebo los parametros enviados (4 elementos en la lista)
        raise SystemExit(f'Uso adecuado: {param[0]} ' 'archivo_camion archivo_precios')
    nombre_archivo_camion = param[1]
    nombre_archivo_precios = param[2]
    formato = param[3]
    informe_camion(nombre_archivo_camion, nombre_archivo_precios, formato)


if __name__ == '__main__':
    f_principal(sys.argv)
        


