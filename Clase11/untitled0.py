#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:11:42 2021

@author: chulke
"""

def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

factorial(4)

#%%

def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:])
   return res

print(sumar([1,2,3,4,5,6,7,8]))