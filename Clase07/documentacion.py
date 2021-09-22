#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:57:41 2021

@author: chulke
"""

def valor_absoluto(n):
    '''Calcula el valor absoluto de un numero n
    Pre: n debe ser un numero entero
    Pos: devuelve el valor absoluto de n'''
    if n >= 0:
        return n
    else:
        return -n
    
    
def suma_pares(l):
    '''Calcula la sumatoria de los numero pares dentro de una lista.
    Pre: La lista debe estar compusta por numeros entros
    Pos: devuelve la suma de los nuemeros pares'''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res
    #invariante del cilo es res


def veces(a, b):
    '''Calcula la suma de a consigo misma b veces.
    Pre: a puede tomar cualquier valor, b debe ser un entero mayor que cero
    Pos: Devuelve la suma de a consigo misma b veces'''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #invariante del cilco es res


def collatz(n):
    '''Evalua la conjetura de Collatz para un numero n.
    Pre: n debe ser un numero entero positivo
    Pos: Devuelve la cantidad de iteraciones necesarias para alcanzar el valor 1'''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
    #invariante del ciclo es n