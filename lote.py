#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:54:20 2021

@author: chulke
"""

class Lote:
    def __init__(self, fruta, cajones, precio):
        self.nombre = fruta
        self.cajones = cajones
        self.precio = precio
        
    def __repr__(self):
        return f'Lote{self.nombre, self.cajones, self.precio}'
        
    def costo(self):
       return self.cajones * self.precio
   
    def vender(self, cantidad):
        self.cajones -= cantidad
        
       
        