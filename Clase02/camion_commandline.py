# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:16:52 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

import csv
import sys

def costo_camion(ruta_archivo):
    f = open(ruta_archivo)
    prod = 0.0
    rows = csv.reader(f)
    header = next(f)
    for row in rows:
        try:
            prod += int(row[1])*float(row[2])
        except ValueError:
            print(f'Warning: {ValueError}')
    return prod

if len(sys.argv) == 2:
    ruta_archivo = sys.argv[1]
else:
    ruta_archivo = '../Data/camion.csv'
        
#costo = costo_camion('../Data/camion.csv')
costo = costo_camion(ruta_archivo)
print('Costo Total: ', costo)