#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:27:09 2021

@author: chulke
"""

class Camion():
    def __init__(self, lotes):
        self.lotes = lotes
        
        
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, a):
        return self.lotes[a]
    
    def __repr__(self):
        return f'Camion({[item for item in self.lotes]})'
    
    def __str__(self):
        print(f'Camion con {len(self.lotes)} lotes:')
        lista = [(f'Lote de {j.cajones} cajones de {j.nombre}, pagados a ${j.precio} cada uno') for j in self.lotes]
        return '\n'.join(lista)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total


