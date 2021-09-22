#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:25:47 2021

@author: chulke
"""

#usando ciclos
# def sumar_enteros(desde, hasta):
#     '''Calcula la sumatoria de los números entre desde y hasta.
#        Si hasta < desde, entonces devuelve cero.

#     Pre: desde y hasta son números enteros
#     Pos: Se devuelve el valor de sumar todos los números del intervalo
#         [desde, hasta]. Si el intervalo es vacío se devuelve 0
#     '''
#     total = 0
#     i = 0
#     for i in range(desde, hasta+1):
#         total += i
#     return total

#sin usar ciclos, implementando el uso de numeros triangulares
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    desde = desde - 1
 
    return hasta*(hasta+1)/2 - desde*(desde+1)/2