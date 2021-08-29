# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:05:44 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

#%%
# =============================================================================
# Lo proximo se define correctamente al escribirlo en el interprete
# =============================================================================
def saludar(nombre):
    'Saludar a alguien' #es lo que se muestra al hacer saludar(help).
    edad = int(input(f'ingresá tu edad {nombre}: '))
    print(f'Hola {nombre}, tienes {edad} años')
    
#%%


edad = int(input(f'ingresá tu edad {nombre}: '))