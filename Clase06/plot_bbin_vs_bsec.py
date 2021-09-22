#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:41:26 2021

@author: chulke
"""

import matplotlib.pyplot as plt
import numpy as np
import random


def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x):
    ''' Recibe una lsita ordenada y un elemento.
    Busca el elemento en la lista y devuelve su posicion.
    Si no esta en la lista devuelve la posicion en la que 
    se puede insertar dicho elemento sin modificar el 
    orden de la lista'''
    izq = 0
    der = len(lista) - 1
    pos = -1
    cont = 0
    while izq <= der:
        cont += 1
        medio = (izq + der) // 2
        posi = medio
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio -1
        else:
            izq = medio +1
    return pos, cont

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]
    comps_promedio = comps_tot / k
    return comps_promedio

def graficar_bbin_vs_bseq(m=10000, k=1000):
    largos = np.arange(256) + 1
    comps_promedio_seq = np.zeros(256)
    comps_promedio_bin = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        comps_promedio_seq[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)
    
    plt.plot(largos, comps_promedio_seq, label = 'Busqueda Scuencial')
    plt.plot(largos, comps_promedio_bin, label = 'Busqueda Binaria')
    plt.xlabel('Largo Lista')
    plt.ylabel('Cantidad de Comparaciones')
    plt.title('Complejidad de la Busqueda')
    plt.ylim(0, 30)
    plt.xlim(0, 200)
    plt.legend()
    plt.show()
    
        

# m = 10000
# k = 1000

# largos = np.arange(256) +1
# comps_promedio = np.zeros(256)

# for i, n in enumerate(largos):
#     lista = generar_lista(n, m)
#     comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# plt.plot(largos, comps_promedio, label = 'Busqueda Secuencial')
# plt.xlabel('Largo Lista')
# plt.ylabel('Cantidad de Comparaciones')
# plt.title('Complejidad de la Busqueda')
# plt.legend()
# plt.show()