#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:20:40 2021

@author: chulke
"""

import random
from collections import Counter

def cumple(n=30):
    year = 365
    people = n
    birthday = []
    b = False
    for i in range(people):
        birthday.append(random.randint(1, year))
    repetidos = Counter()
    for i in birthday:
        repetidos[i] += 1
    primero = repetidos.most_common(1)
    if primero[0][1] > 1:
        b = True
    return b
    
def buscar_coincidencias(c, p):
    coincidencias = sum([cumple(p) for i in range(c)])
    prob = coincidencias/c
    return prob
