#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:46:57 2021

@author: chulke
"""
def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    sec_inic = [0]*n
    sec_out = [sec_inic]
    while sec_out[-1] != [1]*n:
        modificar = sec_out[-1].copy()
        sec_out.append(incrementar(modificar))
    print(sec_out)
    return sec_out
        
j = listar_secuencias(3)
print(len(j))