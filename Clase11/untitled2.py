#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:12:08 2021

@author: chulke
"""

def es_potencia(b, n):
    d = 0
    def es_pot(b, n, d):
        d += 1
        poten = n**d
        if (b == poten or b == n or b == 1) and n != 0:
            res = True
            return res
        else:
            if b > poten:
                res = es_pot(b, n, d)
            else:
                res = False
        return res
    return es_pot(b, n, d)

a = es_potencia(2, 0)

b = es_potencia(256,2)
c = es_potencia(64,4)
d = es_potencia(70,10)
e = es_potencia(1,2)

#%%
