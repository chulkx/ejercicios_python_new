#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:22:50 2021

@author: chulke
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)

class Rectangulo:
    def __init__(self, p1, p2):
        self.a = p1
        self.b = p2
        
        
    def base(self):
        self.base_rect = abs(self.a.x - self.b.x)
        return self.base_rect
    
    def altura(self):
        self.altura_rect = abs(self.a.y - self.b.y)
        return self.altura_rect
    
    def area(self):
        self.area_rect = self.base_rect * self.altura_rect
        return self.area_rect
    
    def rotar(self):
        v1 = Punto(max(self.a.x, self.b.x), min(self.a.y, self.b.y))
        v2 = v1.__add__(Punto(self.altura(), self.base()))
        self.a = v1
        self.b = v2
    
    def __str__(self):
        return f'({self.a}, {self.b})'
    
    def __repr__(self):
        return f'Rectangulo({self.a}, {self.b})'