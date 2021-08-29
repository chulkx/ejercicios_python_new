# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:22:18 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""
import csv
from pprint import pprint
from collections import Counter
#ejercicio 3.18

def leer_parque(nombre_archivo, parque):
    park = parque.upper()
    park_list = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        header = next(file)
        for row in file:
            dicc = dict(zip(header, row))
            for k in dicc:
                if dicc[k].isnumeric():
                    dicc[k] = float(dicc[k])
            if dicc['espacio_ve'] == park:
                park_list.append(dicc)
    print(f'Parque: {parque}')
    return park_list

#ejercicio 3.19
# Devuelvo una lista con las especies dentro de un parque, segun la lista provista por la funcion leer_parque()

def especies(lista_arboles):
    spec = set()
    for i in lista_arboles:
        spec.add(i['nombre_com'])
    for n in sorted(spec):          #comentar para correr la funcion especimen_mas_inclinado y especie_promedio_mas_inclinada
        print(n)                    #comentar para correr la funcion especimen_mas_inclinado y especie_promedio_mas_inclinada
    return spec

#ejercicio 3.20
# Devuelvo un diccionario dicc_completo con todo el listado de especies y la cantidad de cada uno
# Imprimo una lista c con las 5 especies con mas ejemplares
def contar_ejemplares(lista_arboles):
    cont = Counter()
    dicc_completo = {}
    for i in lista_arboles:
        cont[i['nombre_com']] += 1
        dicc_completo[i['nombre_com']] = cont[i['nombre_com']]
    c = cont.most_common(5)
    print('{:<20} {:>10}'.format('Especies', 'Cantidad'))
    for i in c:
        print(f'{i[0]:<20} {i[1]:>10}')
    return dicc_completo

#ejercicio 3.21
# Imprimo en pantalla la especie y las alturas maximas y promedio
# Devuelvo valores de promedio y maximo para futuros usos

def obtener_alturas(lista_arboles, especie):
    #pprint(lista_arboles)
    alturas = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            alturas.append(i['altura_tot'])
    prom = sum(alturas)/len(alturas)
    maxi = max(alturas)
    print(f'Especie: {especie}')
    print(f'Altura máxima:\t\t {maxi}\nAltura promedio:\t {prom}')
    return prom, maxi

#ejercicio 3.22
# Imprimo en pantala las inclinaciones de la especie pedida segun la lista de arboles de un parque

def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            inclinacion.append(i['inclinacio'])
    print(f'Especie: {especie}')                #comentar para correr la funcion especimen_mas_inclinado y especie_promedio_mas_inclinada
    print('Inclinaciones: ',inclinacion)        #comentar para correr la funcion especimen_mas_inclinado y especie_promedio_mas_inclinada
    return inclinacion

#ejercicio 3.23
# Especie con el ejemplar mas inclinado llamando a las funciones especies() y obtener_inclinaciones()

def especimen_mas_inclinado(lista_arboles):
    spec = especies(lista_arboles)
    list_incl = []
    for i in spec:
        incl= max(obtener_inclinaciones(lista_arboles, i))
        incli = (incl, i)
        list_incl.append(incli)
    max_incl = max(list_incl)
    print(max_incl[::-1])
    
#ejercicio 3.24

def especie_promedio_mas_inclinada(lista_arboles):
    spec = especies(lista_arboles)
    list_prom_incl = []
    for i in spec:
        j = obtener_inclinaciones(lista_arboles, i)
        prom_incl = sum(j)/len(j)
        prom = (prom_incl, i)
        list_prom_incl.append(prom)
    max_prom = max(list_prom_incl)
    print(f'Especie con el promedio mas alto: {max_prom[::-1]}')


# Extras
    
def arbol_mas_alto(nombre_archivo):
    altura = 0.0
    datos = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        header = next(file)
        lista = []
        for row in file:
            dicc = dict(zip(header, row))
            for k in dicc:
                if dicc[k].isnumeric():
                    dicc[k] = float(dicc[k])
                lista.append(dicc)
        for i in lista:
            if i['altura_tot'] > altura:
                altura = i['altura_tot']
                datos = i
            else:
                altura = altura
                datos = datos
    pprint(datos)
    
    
def arboles_caidos(nombre_archivo):
    caidos = []
    ubicaciones = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        header = next(file)
        lista = []
        for row in file:
            dicc = dict(zip(header, row))
            for k in dicc:
                if dicc[k].isnumeric():
                    dicc[k] = float(dicc[k])
            lista.append(dicc)
        for i in lista:
            if i['inclinacio'] == 90:
                caidos.append(i)
    enc = ['Espacio Verde', 'Nombre', 'Latitud', 'Longitud']
    print('Listado con los Arboles caídos de BA: ')
    print('{:<25s} {:<25s} {:>20s} {:>20s}'.format(enc[0], enc[1], enc[2], enc[3]))
    for c in caidos:
        ubicaciones.append((c['espacio_ve'], c['nombre_com'], c['lat'], c['long']))
        print('{:<25.20s} {:<25.20s} {:>20.14s} {:>20.14s}'.format(c['espacio_ve'], c['nombre_com'], c['lat'], c['long']))
    return ubicaciones
    
    
def arbol_mas_inclinado(nombre_archivo):
    nocaidos = []
    inclinaciones = []
    inclinados = []
    with open(nombre_archivo, 'rt', encoding=('utf8')) as f:
        file = csv.reader(f)
        header = next(file)
        lista = []
        ubicaciones = []
        for row in file:
            dicc = dict(zip(header, row))
            for k in dicc:
                if dicc[k].isnumeric():
                    dicc[k] = float(dicc[k])
            lista.append(dicc)
        for i in lista:
            if i['inclinacio'] == 90:
                pass
            else:
                nocaidos.append(i)#genero una lista sin los arboles caidos
                inclinaciones.append(i['inclinacio'])
        incl = max(inclinaciones)
        for i in nocaidos:
            if i['inclinacio'] == incl:
                inclinados.append(i)
            
            # if abs(i['inclinacio']) >= inclinacion and abs(i['inclinacio']) != 90:
            #     inclinacion = i['inclinacio']
                
            #     inclinados.append(i)
            # else:
            #     inclinacion = inclinacion
    enc = ['Espacio Verde', 'Nombre', 'Latitud', 'Longitud']
    print('Listado con los Arboles más inclinados de BA: ')
    print('{:<25s} {:<25s} {:>20s} {:>20s}'.format(enc[0], enc[1], enc[2], enc[3]))
    for c in inclinados:
        ubicaciones.append((c['espacio_ve'], c['nombre_com'], c['lat'], c['long']))
        print('{:<25.20s} {:<25.20s} {:>20.14s} {:>20.14s}'.format(c['espacio_ve'], c['nombre_com'], c['lat'], c['long']))
    print(f'''Cantidad de arboles con máxima inclinación: {len(inclinados)}
Inclinación: {incl}''')
    
    return ubicaciones


parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'general paz')
#pprint(parque)

# # las funciones especies(), contar_ejemplares(), obtener_alturas(),  obtener_inclinaciones(), especimen_mas_inclinado(), especie_promedio_mas_inclinada()
# # requieren que la funcion leer_parque() sea llamada con anterioridad.

# especies_parque = especies(parque)


# contar_parque = contar_ejemplares(parque)

# alturas_parque_especie = obtener_alturas(parque, 'Jacarandá')

# inclinaciones = obtener_inclinaciones(parque, 'Jacarandá')
# mas_inclinado = especimen_mas_inclinado(parque) #comentar lineas 37, 38, 80 y 81
# prom_mas_inclinado = especie_promedio_mas_inclinada(parque)


# caidos = arboles_caidos('../Data/arbolado-en-espacios-verdes.csv')

# mas_inclinado = arbol_mas_inclinado('../Data/arbolado-en-espacios-verdes.csv')
