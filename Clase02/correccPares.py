# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:52:55 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

import csv
from pprint import pprint

# Defino variables necesarias
productos = []
lote = ()
costo = 0.0
venta = 0.0


def leer_camion(nombre_archivo):

    # defino variable
    costo_camion = 0.0
    venta_camion = 0.0

    # abro el archivo
    with open(nombre_archivo, "rt") as archivo:
        # tomo los datos
        filas = csv.reader(archivo)
        # tomo las cabeceras
        cabeceras = next(filas)

        # recorro el archivo y calculo el costo del camion
        for datos in filas:
            try:
                if datos[0] in produ_dic:
                    venta_camion += int(datos[1]) * float(produ_dic[datos[0]])
                costo_camion += int(datos[1]) * float(datos[2])
            except ValueError:
                print("Existen errores de datos.")

    return costo_camion, venta_camion


def leer_precios(nombre_archivo):

    # abro el archivo
    with open("../Data/precios.csv", "rt") as archivo:

        # leo el archivo
        filas = csv.reader(archivo)

        # recorro el archivo y genero un diccionario
        for datos in filas:
            try:
                lote = (datos[0], datos[1])
                productos.append(lote)
            except:
                print("Existen errores en el archivo.")
        return productos


# cargo un diccionario con los precios de venta
leer_precios("../Data/precios.csv")

# convierto la lista a diccionario para realizar las busquedas por clave
produ_dic = dict(productos)

# calculo el costo y venta del contenido del camión
costo, venta = leer_camion("../Data/camion.csv")

# calculo la diferencia
balance = round(venta - costo, 2)

# imprimo el balance segun corresponda
print("Venta : ", venta)
print("Costo : ", costo)
if balance > 0:
    print("Ganancia : ", balance)
elif balance < 0:
    print("Perdida : ", balance)
else:
    print("Salimos hechos.")