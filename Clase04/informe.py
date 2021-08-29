# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:22:33 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

#%% Ejercicio 2.18 Balances
# Ejercicio 3.9 la funcio ZIP

import csv
#from pprint import pprint

def leer_camion(ruta_archivo):
    camion = []
    with open(ruta_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = (next(rows))
        costo_total = 0.0
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                record['cajones'] =  int(record['cajones'])
                record['precio'] = float(record['precio'])
                costo_total += record['cajones']*record['precio']
            except AttributeError:
                print (f'Fila {i}: no pude interpretar: {row}')
            camion.append(record)
        return camion
        
# camion = leer_camion('./Data/camion.csv')
# pprint(camion)

def leer_precios(ruta_archivo):
    #check = 0
    precios = {}
    with open(ruta_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        for line in file:
            try:
                precios[line[0]] = float(line[1])
            except IndexError:
                print('Warning: some error in leer_precios')          
        return precios
# precios = leer_precios('./Data/precios.csv')
# pprint(precios)

def balance(precios, camion):
    # costo, camion = leer_camion(costo_camion)
    # precios = leer_precios(precios_venta)
    # # print(precios)
    # # print(precios)
    # #com = 0.0
    camion = camion
    precios = precios
    costo = 0.0
    vta = 0.0
    for row in camion:
        cajon = int(row['cajones'])
        precio_ = float(row['precio'])
        costo += cajon * precio_
    for i in camion:
        if i['nombre'] in precios.keys():
            vta += float(precios[i['nombre']])*int(i['cajones'])
            #com += float(i['precio'])*int(i['cajones'])    
    
    res = round(vta - costo, 2)
    
    print(f'''
          Ventas:\t\t\t ${vta}
          Resto:\t\t\t ${res}
          ''')
    #print(f'Costo del camion:\t ${com}\nVentas: \t\t\t ${vta}\nResto: \t\t\t\t ${res}')
    return res


def main():
    precio = leer_precios('../Data/precios.csv')
    camion = leer_camion('../Data/camion.csv')
    informe = balance(precio, camion)
    print(informe)

