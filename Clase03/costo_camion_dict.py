# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:53:27 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""
# =============================================================================
# costo_camion.py usando dict y zip
# =============================================================================
import csv
def costo_camion(ruta_archivo):
    camion = []
    f = open(ruta_archivo)
    costo_total = 0.0
    rows = csv.reader(f)
    header = next(rows)
    #print(header)
    for i, row in enumerate(rows, start=1):
        record = dict(zip(header, row))
        
        try:
            nbox = int(record['cajones'])
            price = float(record['precio'])
            costo_total += nbox * price
        except ValueError:
            print(f'Fila {i}: no pude interpretar: {row}')
        camion.append(record)
    return costo_total, camion
costo, camion = costo_camion('../Data/camion.csv')
# costo = costo_camion('../Data/missing.csv')
#costo = costo_camion('../Data/fecha_camion.csv')
print('Costo Total: ', costo)
print(camion)
