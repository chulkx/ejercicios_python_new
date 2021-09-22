#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:23:22 2021

@author: chulke
"""
# Ejercicio 6.14

def donde_insertar(lista, x):
    ''' Recibe una lsita ordenada y un elemento.
    Busca el elemento en la lista y devuelve su posicion.
    Si no esta en la lista devuelve la posicion en la que 
    se puede insertar dicho elemento sin modificar el 
    orden de la lista'''
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der:
        medio = (izq + der) // 2
        posi = medio
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio -1
        else:
            izq = medio +1
    if pos == -1:
        if lista[posi] > x:
            pos = posi
        else:
            pos = posi + 1
    return pos

# Ejercicio 6.15

def insertar(lista, x):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der:
        medio = (izq + der) // 2
        posi = medio
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio -1
        else:
            izq = medio +1
    lista_final = lista
    if pos == -1:
        if lista[posi] > x:
            pos = posi
        else:
            pos = posi + 1
        lista_final = lista[:pos]+[x]+lista[pos:]
    return pos