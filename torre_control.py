#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:10:00 2021

@author: chulke
"""

class Cola:
    def __init__(self):
        self.items = []
        
    def encolar(self, x):
        self.items.append(x)
        
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)
    
    def esta_vacia(self):
        return len(self.items) == 0
    
class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, avion):
        self.arribos.encolar(avion)
        
    def nueva_partida(self, avion):
        self.partidas.encolar(avion)
        
    def asignar_pista(self):
        if self.arribos.esta_vacia():
            if self.partidas.esta_vacia():
                g = 'No hay vuelos en espera'
            else:
                sale = self.partidas.desencolar()
                g = f'El vuelo {sale} despegó con éxito'
        else:
            llega = self.arribos.desencolar()
            g = f'El vuelo {llega} aterrizó con exito'
        return g

    def ver_estado(self):
        if self.arribos.esta_vacia() and self.partidas.esta_vacia():
            h = 'No hay vuelos en espera'
        else:
            h = (f'''
Vuelos esperando para aterrizar:{",".join([" "+a for a in self.arribos.items])}
Vuelos esperando para despegar:{",".join(" "+d for d in self.partidas.items)}''')
        
        return print(h)
