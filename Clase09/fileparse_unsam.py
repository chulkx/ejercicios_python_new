#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fileparse.py

#%%
import csv

#%% ejercicio 7.6
def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select,
    que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    filas = csv.reader(lines)

    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)
    else:
        encabezados = []

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios

    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
    for n_fila, fila in enumerate(filas, start = 1):
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]
        
        try:
            if types:
            
                fila = [func(val) for func, val in zip(types, fila)]
                
            # Armar el diccionario
            if encabezados:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)

            registros.append(registro)
        
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {n_fila}: No pude convertir {fila}')
                print(f'Fila {n_fila}: Motivo: {e}')
                
    return registros

    





