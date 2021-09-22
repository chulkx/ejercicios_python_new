# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:34:49 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos



# Ejercicio 4.3 Busqueda de un elemento
def buscar_u_elemento(lista, elem):
    i = len(lista)-1
    for i in range(len(lista)-1, -1, -1): #asi recorro la lista desde el final hasta el inicio
        if lista[i] == elem:
            return i
        
    return -1
        
# Ejercicio 4.4 Búsqueda de máximo y mínimo
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
        

#modificacion ejercicio 6.13, 
def busqueda_lineal_lordenada(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        elif z > e:
            break
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    cont = 0
    while izq <= der:
        cont += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, cont


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

    
    