# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:16:18 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida = [e] + invertida
    return invertida
        

def main():
    a = invertir_lista([1, 2, 3, 4, 5])
    print(a)
    b = invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
    print(b)