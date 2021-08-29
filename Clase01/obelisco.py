# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:08:18 2021

@author: Gustavo

Una mañana ponés un billete en la vereda al lado del obelisco porteño.
A partir de ahí, cada día vas y duplicás la cantidad de billetes,
apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de 
billetes sea más alta que el obelisco?
"""

grosor_billete = 0.11 * 0.001
altura_obelisco = 67.5
dia = 1
num_billetes = 1

while grosor_billete * num_billetes <= altura_obelisco:
    
    dia += 1
    num_billetes = num_billetes*2
print('Cantidad de dias hasta que la pila sea mas alta que el obelisco: ',dia)