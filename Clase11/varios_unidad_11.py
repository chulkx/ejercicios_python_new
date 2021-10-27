#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:12:01 2021

@author: chulke
"""

# hasta*(hasta+1)/2 - desde*(desde+1)/2

'''Un número triangular cuenta objetos dispuestos en un triángulo equilátero. 
El n-ésimo número triangular es el número de puntos en la disposición triangular 
con n puntos en un lado, 
y es igual a la suma de los n números naturales de 1 a n, 
siendo por convención, el 1 el primer número triangular.
'''
# Ejercicio 11.2 - n-esimo numero triangular

def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n-1)

print(triangular(5))

#%%
'''
cuenta la cantidad de digitos de un numero dado
'''


def cant_digitos(n):
    n = str(n)
    def cant(n):
        if len(n) == 1:
            return 1
        else:
            c = 1 + cant(n[1:])
            return c
    n = cant(n)
    return n

print(cant_digitos(1000000))

#%%

# ej 11.4 - potencias

'''
Recibe dos numero, b y n, y devuelve True si b es potencia de n y False en caso contrario
'''

def es_potencia(b, n):
    d = 0
    def es_pot(b, n, d):
        d += 1
        poten = n**d
        if b == poten or b == 1:
            res = True
            return res
        else:
            if b > poten:
                res = es_pot(b, n, d)
            else:
                res = False
        return res
    return es_pot(b, n, d)

a = es_potencia(16, 2)

b = es_potencia(256,2)
c = es_potencia(64,4)
d = es_potencia(70,10)
e = es_potencia(1,2)

'''
def es_potencia(b, n):
    es_pot = False
    if n == 0:
        es_pot = False
    elif b == 1:
        es_pot = True
        return es_pot
    else:
        if b%n == 0:
            b = b//n
            es_pot = es_potencia(b, n)
            return es_pot
    return es_pot


def es_potencia(n, b):
    if n == 1:
        return True
    if n%b == 0:
        return es_potencia(n//b, b)
    else:
        return False


La condicion inicial se puede mandar a un wrapper para no chequearla en cada recursion
'''

#%%
'''
Escribí una funcion recursiva posiciones(a, b) que reciba como parámetros dos 
cadenas a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a.
'''


def posiciones(a,b):
    pos = []
    def _posiciones(a,b):
        if a == '' or len(b) > len(a):
            return pos
        else:
            index = a.find(b)
            if pos == []:
                pos.append(index)
            else:
                pos.append(index+pos[-1]+len(b))
            _posiciones(a[index+len(b):], b)
            return pos
    
    x = _posiciones(a, b)
    return x

#%%

#paridad

def es_par(n):
    if n == 1:
        return False
    else:
        return es_impar(n-1)
    pass

def es_impar(n):
    if n == 1:
        return True
    else:
        return es_par(n-1)
    pass

a = es_par(22)
b = es_impar(22)

#%%

#11.7

def maximo(lista):
    maxi = lista[0]
    def maxim(lista, maxi):
        if lista == []:
            return maxi
        elif lista[0] > maxi:
            maxi = lista[0]
        return maxim(lista[1:], maxi)
        
    maximin = maxim(lista, maxi)
    return maximin

f = maximo([2,2,4,5,3,4,5,333,9,45,1,2,3,5])
    

#%%

#11.10      Combinaciones de una lista (combinatoria)


def combinaciones(lista, k):
    '''Dada una lista de caracteres nos devuelve todas las 
    posibles combinaciones de sus elementos de longitud k'''
    if k == 1:
        comb = lista
    else:
        comb_rec = combinaciones(lista, k-1)
        comb = [e + c for e in lista for c in comb_rec]
    return comb

print(combinaciones(['a', 'b', 'c'], 3))
