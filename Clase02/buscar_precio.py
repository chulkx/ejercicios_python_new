# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:23:28 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# Ejercicio 2.7 
# =============================================================================

def buscar_precio(fruta):
    check = 0
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            if row[0] == fruta:
                precio = row[1]
                check = 1
    if check == 1:
        print(f'El precio de un cajon de {fruta} es de :', precio)
    else:
        print(f'{fruta} no se encuentra en el listado')


# =============================================================================
# a = buscar_precio('Frambuesa')
# b = buscar_precio('Kale')
# 
# # El precio de un cajon de Frambuesa es de : 34.35
# # 
# # Kale no se encuentra en el listado
# =============================================================================

# =============================================================================
# Busqueda de frutas llamando a la funcion en la consola.
#
# a = buscar_precio('Manzana')
# Manzana no se encuentra en el listado
# 
# a = buscar_precio('Naranja')
# El precio de un cajon de Naranja es de : 106.28
# =============================================================================
                
