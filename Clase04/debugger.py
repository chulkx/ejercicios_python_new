# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:11:43 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""
#%% Ejercicio 4.1


def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #Esta linea modifica la lista ingresada
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

#%% Ejercicio 4.2

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
        return camion
camion = leer_camion('../Data/camion.csv')
pprint(camion)