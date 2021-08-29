# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:29:28 2021

@author: Gustavo Godoy
mail: gustavogodoy85@gmail.com
"""
import math

r = ''
while r == '' :
    r = input("Ingrese el radio de la esfera: ")

r = int(r, 10)

vol = (4/3)*(math.pi)*(r**3)

print("El volumen de la esfera es: ", vol)