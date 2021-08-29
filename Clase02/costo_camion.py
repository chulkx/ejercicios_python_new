# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:39:12 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

'''
#%% ejercicio 2.2
with open('../Data/camion.csv', 'rt') as file:
    prod = 0.0
    header = next(file)
    for line in file:
        row = line.split(',')
        prod += int(row[1])*float(row[2])
    print('Costo Total: ', prod)
    
#%% ejercicio 2.3
with open('../Data/precios.csv', 'rt') as f:
    for line in f :
        row = line.split(',')
        if row[0] == 'Naranja':
            print(f'El precio de {row[0]} es : ', row[1])

#%% ejercicio 2.4
#el modulo gzip me permite abrir archivos comprimidos
#al usar este modulo si o si debo usar 'rt', sino leere cadenas de bytes
import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end= '')
        
#%%
# =============================================================================
# Ejercicio 2.6, conversion a funcion del script del archivo costo_camion.py 
# =============================================================================
def costo_camion(ruta_archivo):
    with open(ruta_archivo) as f:
        prod = 0.0
        header = next(f)
        for line in f:
            row = line.split(',')
            prod += int(row[1])*float(row[2])
    return prod
#costo = costo_camion('../Data/camion.csv')
costo = costo_camion('../Data/missing.csv')
print('Costo Total: ', costo)

#%%
# =============================================================================
# Ejercicio 2.8, trabajando las excepciones
# =============================================================================

def costo_camion(ruta_archivo):
    with open(ruta_archivo) as f:
        prod = 0.0
        header = next(f)
        for line in f:
            try:
                row = line.split(',')
                prod += int(row[1])*float(row[2])
            except ValueError:
                print(f'Warning: {ValueError}')
    return prod
#costo = costo_camion('../Data/camion.csv')
costo = costo_camion('../Data/missing.csv')
print('Costo Total: ', costo)

#%%
# =============================================================================
# Ejercicio 2.9 modulo csv

#Use lo siguiente para comprobar como es la salida deatos al usar csv.reader()

import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
    print(row)

# =============================================================================
    
    
# =============================================================================
#     ['Lima', '100', '32.2']
#     ['Naranja', '50', '91.1']
#     ['Caqui', '150', '103.44']
#     ['Mandarina', '200', '51.23']
#     ['Durazno', '95', '40.37']
#     ['Mandarina', '50', '65.1']
#     ['Naranja', '100', '70.44']
# =============================================================================
'''
#%% Ejercicio 2.9
import csv
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
costo = costo_camion('../Data/camion.csv')
#costo = costo_camion('../Data/missing.csv')
print('Costo Total: ', costo)

# =============================================================================
# Salida de datos usando el archivo missing.csv 
#
# Warning: <class 'ValueError'>
# Warning: <class 'ValueError'>
# Costo Total:  30381.15
# =============================================================================
