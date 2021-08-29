# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:40:59 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# costo_camion.py enumerate
# =============================================================================

import csv
def costo_camion(ruta_archivo):    
    f = open(ruta_archivo)
    prod = 0.0
    rows = csv.reader(f)
    header = next(f) #aqui me sirvio xq use la funcion de next para saltearme una fila
                     #pero deberia ser next(rows)
    for i, row in enumerate(rows, start=1):
        try:
            prod += int(row[1])*float(row[2])
        except ValueError:
            print(f'Fila {i}: no pude interpretar: {row}')
    return prod
#costo = costo_camion('../Data/camion.csv')
costo = costo_camion('../Data/missing.csv')
print('Costo Total: ', costo)