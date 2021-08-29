# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:08:59 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

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
                # print('Warning: some error in leer_precios')          
                pass
        return precios
# precios = leer_precios('./Data/precios.csv')
# pprint(precios)

def balance(precios_venta, costo_camion):
    costo = 0
    ventas = 0
    camion = leer_camion(costo_camion)
    precios = leer_precios(precios_venta)
    
    for prod in camion:
        costo += prod['cajones']*prod['precio']#costo del camion
        ventas += prod['cajones']*float(precios[prod['nombre']])
    


    saldo = round(ventas - costo, 2)

    print( f'Las ventas fueron de {ventas}')
    print( f'El costeo de la mercaderia fue de {costo}')
    
    print(f'Su saldo es de {saldo}. ')
    datos = {'saldo' : saldo, 'ventas' : ventas, 'costo' : costo}
    return datos #por si se quieren usar los datos

# Primera forma
def hacer_informe(precios, camion):
    dicc_precios = leer_precios(precios)
    lista_camion = leer_camion(camion)
    header = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    informe = []
    for j in lista_camion:
        if j['nombre'] in dicc_precios.keys():
            e = (j['nombre'], j['cajones'], j['precio'], round(float(dicc_precios[j['nombre']])-float(j['precio']), 2) )
            informe.append(e)
            
            #print('%10s %10d %10.2f %10.2f' % e)
    print('%10s %10s %10s %10s' % header)
    #print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')#otra forma de imprimir el header
    print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')
    for nombre, cajones, precio, cambio in informe:
        # print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
        # print('{:>10s} {:>10d} {:>10s} {:>10.2f}'.format(nombre, cajones, '$'+'{:.2f}'.format(precio), cambio))
        precio_ = '$'+ '{:.2f}'.format(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_:>10s} {cambio:>10.2f}')
        

 
# Segunda forma   
# def hacer_informe(precios, camion):
#     dicc_precios = leer_precios(precios)
#     lista_camion = leer_camion(camion)
#     for j in lista_camion:
#         if j['nombre'] in dicc_precios.keys():
#             dicc_informe = {
#                 'nombre' : j['nombre'],
#                 'cajones' : j['cajones'],
#                 'precio' : j['precio'],
#                 'cambio' : round(float(dicc_precios[j['nombre']]) - float(j['precio']))
#                 }
#             print('{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}'.format_map(dicc_informe))
            
# Tercera forma
# def hacer_informe(precios, camion):
#     dicc_precios = leer_precios(precios)
#     lista_camion = leer_camion(camion)
#     header = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#     for j in lista_camion:
#         if j['nombre'] in dicc_precios.keys():            
#             nombre = j['nombre']
#             cajones = j['cajones']
#             precio = j['precio']
#             cambio = round(float(dicc_precios[j['nombre']]) - float(j['precio']))
                
#             print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

    
#g = balance('../Data/precios.csv', '../Data/camion.csv')
h = hacer_informe('../Data/precios.csv', '../Data/camion.csv')
