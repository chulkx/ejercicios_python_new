#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:48:44 2021

@author: chulke
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            return True
        elif lista[medio] < e:  #uso la parte derecha
            res = bbinaria_rec(lista[medio:], e)
        else:                   #uso la parte izquierda
            res = bbinaria_rec(lista[:-medio], e)
        
    return res


#a = bbinaria_rec([1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17], 15)