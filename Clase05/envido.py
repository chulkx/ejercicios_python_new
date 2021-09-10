#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:07:47 2021

@author: chulke
"""

import random
from collections import Counter

def dar():
    valores = [1,2,3,4,5,6,7,10,11,12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(str(valor), palo) for valor in valores for palo in palos]
    mano = random.sample(naipes, 3)
    return mano

def envido():
    mano = dar()
    # mano = [('4', 'oro'), ('6', 'oro'), ('2', 'oro')]  #mano de prueba
    malas = ['10','11','12']
    sumador = []
    mismo = Counter()
    total = 0
    for i in mano:          #busco el palo que se repite
        mismo[i[1]] += 1
    palo_mentira = mismo.most_common(1)[0][0]
    if mismo.most_common(1)[0][1] == 1:     #si todas son de distinto palo elijo la mayor
        total = int(mano[0][0])
        for i in mano:
            if int(i[0]) > total:
                total = int(i[0])
    elif mismo.most_common(1)[0][1] == 2: #Si hay dos del mismo palo las sumo
        total = 20
        for i in mano:
            if i[1] == palo_mentira:
                if i[0] in malas:
                    total += 0
                else:
                    total += int(i[0])
    elif mismo.most_common(1)[0][1] == 3: #si hay 3 del mismo palo elijo la mejor combinación
        for i in mano:
            if i[0] in malas:
                sumador.append(0)
            else:
                sumador.append(int(i[0]))
        total = 20 + (sorted(sumador, reverse=True)[0] + sorted(sumador, reverse=True)[1])
            
    return total

def prob_env(n = 10000):        #calculo las probabilidades de obtener 31, 32, 33
    p_31 = len([envido() for i in range(n) if envido() == 31])
    prob_31 = p_31/n
    p_32 = len([envido() for i in range(n) if envido() == 32])
    prob_32 = p_32/n
    p_33 = len([envido() for i in range(n) if envido() == 33])
    prob_33 = p_33/n
    return prob_31, prob_32, prob_33

def test():
    a = prob_env()
    print(a)
    