#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:05:56 2021

@author: chulke
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

def album_incompleto(A):
    b = False
    for i in A:
        if i == 0:
            b = True
            break
    return b

def comprar_figu(figus_total):
    n = random.randint(1, figus_total)
    return n

def cuantas_figus(figus_total):
    nuevo = crear_album(figus_total)
    cont = 0
    while album_incompleto(nuevo) == True:
        figu = comprar_figu(figus_total)
        nuevo[figu-1] += 1
        cont += 1
    return cont

def repeticion(n = 50, figus_total = 6):
    album = [cuantas_figus(figus_total) for i in range(n)]
    promedio = np.mean(album)
    return promedio

def experimento_figus(n_repeticiones, figus_total):
    prom = repeticion(n_repeticiones, figus_total)
    return prom 
        
#Ahora con paquetes

def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(1, figus_total) for i in range(figus_paquete)]
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    nuevo = crear_album(figus_total)
    cont = 0
    llenado = 0
    while album_incompleto(nuevo) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            nuevo[i-1] += 1
        cont += 1
    return cont

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    nuevo = crear_album(figus_total)
    historia = []
    llenado = 0
    while album_incompleto(nuevo):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            nuevo[paquete.pop()-1] = 1
        llenado = (nuevo>0).sum()
        historia.append(llenado)
    return historia

def repeticiones(repe, figus_total, figus_paquete):
    promedio = np.mean([cuantos_paquetes(figus_total, figus_paquete) for i in range(repe)])
    return promedio

# plt.hist(calcular_historia_figus_pegadas(670, 5), bins=3)
plt.show()
plt.plot(calcular_historia_figus_pegadas(670, 5))

# a = album_incompleto(crear_album(2))
# h = cuantas_figus(670)
# g = repeticion()
# k = experimento_figus(1000, 670)
# j = cuantos_paquetes(670, 5)
# l = repeticiones(1000, 670, 5)
