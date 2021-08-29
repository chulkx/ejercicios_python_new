# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:06:54 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# def costo_camion(ruta_archivo):
#     import csv
#     f = open('../Data/missing.csv')
#     prod = 0.0
#     rows = csv.reader(f)
#     header = next(f)
#     for row in rows:
#         try:
#             prod += int(row[1])*float(row[2])
#         except ValueError:
#             print(f'Warning: {ValueError}')
#     return prod
# #costo = costo_camion('../Data/camion.csv')
# costo = costo_camion('../Data/missing.csv')
# print('Costo Total: ', costo)
# =============================================================================
#%% ejercicio 2.15 informe.py 

# =============================================================================
# 
# def leer_camion(ruta_archivo):
#     camion = []
#     with open(ruta_archivo) as f:
#         rows = csv.reader(f)
#         header = next(f) 
#         for row in rows:
#             try:
#                 prod = (row[0], int(row[1]), float(row[2]))
#                 camion.append((prod))
#             except:
#                 print (f'Warning: some error')
#     return camion
# cam = leer_camion('../Data/camion.csv')
# print(cam)
# 
# =============================================================================
# =============================================================================
# #%% Ejercicio 2.16 informe.py
# 
#
# import csv
# from pprint import pprint
# 
# def leer_camion(ruta_archivo):
#     camion = []
#     with open(ruta_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         header = (next(f).rstrip('\n')).split(',')
#         for row in rows:
#             product_dictionary = {}
#             try:
#                 product_dictionary[header[0]] = row[0]
#                 product_dictionary[header[1]] = int(row[1])
#                 product_dictionary[header[2]] = float(row[2])            
#             except AttributeError:
#                 print ('Warning: some error')
#             camion.append(product_dictionary)
#         return camion
# camion = leer_camion('../Data/camion.csv')
# pprint(camion)
# 
# =============================================================================
#%% Ejercicio 2.17
# =============================================================================
# Ejercicio 2.7
# def buscar_precio(fruta):
#     check = 0
#     with open('../Data/precios.csv', 'rt') as f:
#         for line in f:
#             row = line.split(',')
#             if row[0] == fruta:
#                 precio = row[1]
#                 check = 1
#     if check == 1:
#         print(f'El precio de un cajon de {fruta} es de :', precio)
#     else:
#         print(f'{fruta} no se encuentra en el listado')
#         
#         
# =============================================================================
# =============================================================================
# Ejercicio 2.17
#
#
#
# import csv
# from pprint import pprint
# 
# 
# def leer_precios(ruta_archivo):
#     check = 0
#     precios = {}
#     with open(ruta_archivo, 'rt', encoding=('utf8')) as f:
#         file = csv.reader(f)
#         for line in file:
#             try:
#                 precios[line[0]] = line[1]
#             except IndexError:
#                 print('Warning: some error')          
#         return precios
# precios = leer_precios('./Data/precios.csv')
# pprint(precios)
# =============================================================================

#%% Ejercicio 2.18 Balances

import csv
#from pprint import pprint

def leer_camion(ruta_archivo):
    camion = []
    with open(ruta_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = (next(f).rstrip('\n')).split(',')
        for row in rows:
            product_dictionary = {}
            try:
                product_dictionary[header[0]] = row[0]
                product_dictionary[header[1]] = int(row[1])
                product_dictionary[header[2]] = float(row[2])            
            except AttributeError:
                print ('Warning: some error')
            camion.append(product_dictionary)
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
                precios[line[0]] = line[1]
            except IndexError:
                print('Warning: some error')          
        return precios
# precios = leer_precios('./Data/precios.csv')
# pprint(precios)

def balance(precios_venta, costo_camion):
    costo = 0
    ventas = 0
    nombre = []
    camion = leer_camion(costo_camion)
    precios = leer_precios(precios_venta)
    
    for prod in camion:
        #print (prod)
        costo += prod['cajones']*prod['precio']#costo del camion
        #nombre.append(prod['nombre'])#lista con el nombre de las frutas descargadas
        ventas += prod['cajones']*float(precios[prod['nombre']]) #Esta linea suplanta el siguiente for
    print(nombre)
    # for i in range (len(nombre)):
    #     for fruta in precios:
    #         if fruta == nombre[i]:
    #             prod = nombre[i]
    #             ventas += prod['cajones']*float(precios[fruta])
# =============================================================================
# El for de las lineas anteriores genera una falla en el calculo, por eso agregue
# la linea         ventas += prod['cajones']*float(precios[prod['nombre']])
# al primer for, y asi la cuenta es correcta. Esto se debe a que tengo siempre la 
# misma cantidad de cajones multiplicando a los precios, lo cual es incorrecto.
# En dicho for falta agregar la componente correspondiente de la cantidad de cajones.
# 

# =============================================================================

    saldo = round(ventas - costo, 2)

    print( f'Las ventas fueron de {ventas}')
    print( f'El costeo de la mercaderia fue de {costo}')
    
    print(f'Su saldo es de {saldo}. ')
    datos = {'saldo' : saldo, 'ventas' : ventas, 'costo' : costo}
    return datos #por si se quieren usar los datos
    
    
g = balance('../Data/precios.csv', '../Data/camion.csv')
















# %%
