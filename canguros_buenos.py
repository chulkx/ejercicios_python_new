#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:20:23 2021

@author: chulke
"""

class Canguro:
    def __init__(self, nombre, contenido = []):
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy()
        
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
        
    def __str__(self):
        lista = [self.nombre + ' tiene: ']
        for o in self.contenido_marsupio:
            s = f'{" "*10} {str(o):<s}'
            lista.append(s)
        return '\n'.join(lista)


# # canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """

# class Canguro:
#     """Un Canguro es un marsupial."""
    
#     def __init__(self, nombre, contenido=None): 
    # ''' El error esta al intentar iniciar argumento opcional con una lista vacia,
    # ya que usa para cada instancia el mismo puntero, y al modificar la lista de 
    # cualquier instancia de la clase todas las demas instancias se veran modificadas.
    # Encontre dos maneras de reparar el bug. La primera es la escrita debajo (en el
    # codigo del ejercicio. La otra es trabajar con una copia del argumento)
    # '''
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         if contenido is None:
#             contenido = []
#         self.nombre = nombre
#         self.contenido_marsupio = contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)