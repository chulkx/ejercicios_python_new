#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:35:04 2021

@author: chulke
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()


def graficar():
    N = 100000
    i=0
    fig = plt.figure()
    lista = []
    
    while i<12:
        caminata = randomwalk(N)
        lista.append(caminata)
        plt.subplot(2, 1, 1) # define la figura de arriba
        plt.plot(caminata)
        plt.title('12 Caminatas random')
        plt.xlabel('Tiempo')
        plt.ylabel('Distancia al origen')
        i += 1
        
    alejado = []
    for i in lista:
        alejado.append(max(abs(i)))
    index_alejado = alejado.index(max(alejado))
    index_menos_alejado = alejado.index(min(alejado))
    
    
    plt.subplot(2, 2, 3)
    plt.plot(lista[index_alejado])
    plt.title('Caminata que mas se aleja')
    ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    plt.subplot(2, 2, 4)
    plt.plot(lista[index_menos_alejado])
    plt.title('Caminata que menos se aleja')
    
    plt.show()
    
if __name__ == '__main__':
    graficar()