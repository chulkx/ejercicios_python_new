#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 01:32:03 2021

@author: chulke
"""

# 4.5 Arbolado porteño y comprensión de listas
# Ejercicio 4.16 - 4.17

import csv
import matplotlib.pyplot as plt
import numpy as np


def leer_arboles(nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
    arboleda = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        rows = csv.reader(f)
        header = next(rows)
        # for row in rows:
        #     dicc = dict(zip(header, row))
        #     arboleda.append(dicc)
        arboleda = [{nombre: valor for nombre, valor in zip(header, row)} for row in rows]

    return arboleda

def medidas_de_especies(especies, arboleda):
    me = {nombre: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == nombre] for nombre, arbol in zip(especies, arboleda)}
    return me

#ej 5.25
def test_plot():
    arboleda = leer_arboles()
    H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.hist(H, bins=(80))

#ej 5.26
def scatter_hd():
    arboleda = leer_arboles()
    h = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    # for i in h:
    #     alt = i[0]
    #     diam = i[1]
    #     plt.scatter(diam, alt)
    data = np.array(h)
    a = [plt.scatter(h, d) for d, h in data]
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
    return h

#ej 5.27
def graficas_especies():
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    arboleda = leer_arboles()
    me = medidas_de_especies(especies, arboleda)
    colores = ['blue', 'red', 'green']
    color = 0
    diam = []
    alt = []
    for i in me:
        col = colores[color]
        for j in me[i]:
            diam.append(j[1])
            alt.append(j[0])
        plt.scatter(diam, alt, c=col, label=i, alpha=0.2)
        color += 1
    plt.legend()
    plt.xlabel('diametro (cm)')
    plt.ylabel('altura (m)')
    plt.title('Relación diámetro-alto segun especies')
    return me


def main():
    ar = graficas_especies()
    # print(ar[1:3])
    # print(ar)
    print(len(ar))
    return ar
