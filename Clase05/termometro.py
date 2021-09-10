#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:07:47 2021

@author: chulke
"""
import numpy as np
import random

def medir_temp(n=1):
    for i in range(n):
        t = round(random.normalvariate(37.5, 0.2), 2)
    return t

def resumen_temp(n=999):
    res = []
    for i in range(n):
        temp = medir_temp()
        res.append(temp)
    maximo = max(res)
    minimo = min(res)
    prom = round(sum(res)/n, 2)
    if n%2!=0:
        mediana = sorted(res)[round(n/2)-1]
    else:
        mediana = (sorted(res)[round(n/2)] + sorted(res)[round(n/2)-1])/2
        mediana = round(mediana, 2)
    out = (maximo, minimo, prom, mediana)
    np.save('../Data/temperaturas', res)
    return out


def test():
    a = resumen_temp()
    print(a)
    
