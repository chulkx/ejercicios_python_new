#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:49:08 2021

@author: chulke
"""

import os

import sys


def archivos_png(directorio):
    '''Caso general
    Funcion generadora para recorrer los directorios y buscar los archivos png'''
    for root, dirs, files in os.walk(directorio):
        if dirs:
            for dirss in dirs:
                for name in files:
                    if name.endswith('.png'):
                        s,n = (os.path.join(root, dirss), name)
                        yield s, n
        else:
            # s = (name for name in files if name.endswith('.png'))
            # print(s)
            for name in files:
                if name.endswith('.png'):
                    s, n = (root, name)
                    yield s, n
                    
# def mover_archivo(directorio_v, directorio_n):    ##Terminar esta parte ejercicio 10.6
#     for a, b in archivos_png(directorio_v):
#         fecha = b[len(b)-12:len(b)-4]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for a in archivos_png(sys.argv[1]):
            print(a)




