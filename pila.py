#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:49:10 2021

@author: chulke
"""

class Pila:
    
    def __init__(self):
        self.variables = []
    
    def apilar(self, objeto):
        self.variables.append(objeto)
    
    def desapilar(self):
        return self.variables.pop(-1)
    
    def esta_vacia(self):
        return len(self.variables) == 0
    
def f():
    x = 50
    a = 20
    print("En f, x vale ", x)
    
def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)
    
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")
    
pila_de_llamadas= Pila()
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
estado['próxima_linea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)

