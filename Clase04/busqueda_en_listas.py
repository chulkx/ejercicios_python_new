# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:34:49 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""
#%% Ejercicio 4.3 Busqueda de un elemento
def buscar_u_elemento(lista, elem):
    i = len(lista)-1
    for i in range(len(lista)-1, -1, -1): #asi recorro la lista desde el final hasta el inicio
        if lista[i] == elem:
            return i
        
    return -1
        
#%% Ejercicio 4.4 Búsqueda de máximo y mínimo
def maximo(lista):
    try:
        m = lista[0]
        for e in lista:
            if e > m :
                m = e
        return m
    except IndexError:
        print('La cadena ingresada no puede ser vacía')

def minimo(lista):
    try:
        m = lista[0]
        for e in lista:
            if e < m:
                m = e
        return m
    except IndexError:
        print('La cadena ingresada no puede ser vacía')
        
def main():
    a = buscar_u_elemento([1,2,3,2,3,4],1)
    print(a)
    b = buscar_u_elemento([1,2,3,2,3,4],2)
    print(b)
    c = buscar_u_elemento([1,2,3,2,3,4],3)
    print(c)
    d = buscar_u_elemento([1,2,3,2,3,4],5)
    print(d)
    print('--------------------')
    
    e = maximo([1,2,7,2,3,4])
    print(e)
    f = maximo([1,2,3,4])
    print(f)
    g = maximo([-5,4])
    print(g)
    h = maximo([-5,-4])
    print(h)

    
    