# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:09:29 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def propagar(b):
    v = b.copy()    #genero una copia del original

    for i in range(len(v)-1):           #recorro la lista
        if v[i] == 0 and v[i+1] == 1:   #si el elemento es 0 y el siguiente 1
            j = i                       #indice auxiliar
            '''En el  siguiente While recorro en reversa todos las posiciones anteriores
            y las cambio de 0 a 1 (gracias al if en el que estoy ya se que todos los 
            valores anteriores son 0)'''
            while j>=0 and v[j] == 0:   #chequeo el valor de j y de la lista en la posicion j
                v[j] = 1    
                j -= 1 
        '''El siguiente if y su if anidado me permiten modificar hacia la derecha'''                 
        if v[i] == 1:                   #si es 1 y el siguiente 0 
            if v[i+1] == 0:
                v[i+1] = 1              #modifico el siguiente de 0 a 1
    return v

def main():
    # l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, -1, 0, 0]  
    # print(l1)
    # a = propagar(l1)
    # print(a)
    # l2 = [ 0, 0, 0, 1, 0, 0]
    # print(l2)
    # b = propagar(l2)
    # print(b)
    # l3 = [0, 0, 1, -1, 0, -1, 0, 0, 0, 1, -1]
    # print(l3)
    # c = propagar(l3)    
    # print(c)
    lista_1 = [ 0, 0, 0, 1, 0, 0]
    lista_2 = [ 0, 0, 0, 0, 0, -1]
    lista_3 = [ 0, 0, 0, 0, 0, 1]
    lista_4 = []
    lista_5 = [ 0 for _ in range(1000) ] + [1]
    lista_6 = [1] + [ 0 for _ in range(1000) ]
    lista_7 = [ (i% 6)//2-1 for i in range(200) ]
    lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
    
    listas = [lista_1, lista_2, lista_3, lista_4, lista_5, lista_6, lista_7, lista_8]
    
    for lista in listas:
        a = propagar(lista)
        print(a)
    print(lista_1)