#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:48:07 2021

@author: chulke
"""
import random
from collections import Counter

def tirar(n = 5):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1, 6))
    return tirada


def es_generala(tirada):
    a = tirada[0]
    b = True
    for i in tirada:
        if i != a:
            b = False
    return b


def probar_gen():
    i = 0               #defino valores iniciales
    a = tirar(5)
    nuevo = []
    nuevo_ = []
    while i<3:          #ciclo ppal
        nuevo = nuevo_ + a      #lista con la que voy a trabajar
        nuevo_ = []             #renuevo lista para agregar numero iguales
        if es_generala(nuevo):  #evaluo si es generala para salir del while
            break
        elif i != 2:
            b = Counter()
            for s in nuevo:     #genero un dicc con los valores repetidos y las cantidades de cada uno
                b[s] += 1
            comun = b.most_common(1)[0][0]  #busco el mas comun
            if b.most_common(1)[0][1] == 1:     #si todos los elemoentos son distintos
                azar = random.randint(0, 1)     #elegir si tiro todos de nuevo o si guardo un elemento
                if azar == 0:
                    nuevo_ = []
                else:
                    for s in nuevo:
                        if s == comun:
                            nuevo_.append(s)
            else:
                for s in nuevo:
                    if s == comun:      #si es = al mas comun lo agrego a la lista nuevo_
                        nuevo_.append(s)
            l = len(nuevo) - len(nuevo_)
            a = tirar(l)            #hago una nueva tirada
        elif i == 2:            #si es la ultima tirada
            nuevo_ = nuevo
        i += 1
        # print(nuevo)      #print muy util para ver las tiradas de dados
    salida = nuevo
    return salida
    

def prob_generala(N):
    G = sum([es_generala(probar_gen()) for i in range(N)])
    prob = G/N
    return prob


# def test_1(N):
#     G = sum([es_generala(tirar()) for i in range(N)])
#     prob = G/N
#     print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
#     print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
