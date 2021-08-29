# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:54:38 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# 4.5 Arbolado porteño y comprensión de listas
# Ejercicio 4.16 - 4.17

import csv
def leer_arboles(nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
    arboleda = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        rows = csv.reader(f)
        header = next(rows)
        # for row in rows:
        #     dicc = dict(zip(header, row))
        #     arboleda.append(dicc)
        arboleda = [{nombre: valor for nombre, valor in zip(header, row)} for row in rows]
    
    H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    h = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    
    return arboleda

def medidas_de_especies(especies, arboleda):
    me = {nombre: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == nombre] for nombre, arbol in zip(especies, arboleda)}
    return me

def main():
    ar = leer_arboles()
    # print(ar[1:3])
    # print(ar)
    # print(len(ar))
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    me = medidas_de_especies(especies, ar)
    for key in me:
        print(key, len(me[key]))

