#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:19:39 2021

@author: chulke
"""

from vigilante import vigilar
import csv


# def parsear_datos(lines):
#     rows = csv.reader(lines)
#     return rows

# def elegir_columnas(rows, indices):
#     for row in rows:
#         yield [row[index] for index in indices]
        

# def cambiar_tipo(rows, types):
#     for row in rows:
#         yield [func(val) for func, val in zip(types, row)]
        
# def hace_dicts(rows, headers):
#     for row in rows:
#         yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows1 = csv.reader(lines)
    
    # rows = elegir_columnas(rows, [0, 1, 2])
    rows = ((row[index] for index in [0, 1, 2]) for row in rows1)
    
    # rows = cambiar_tipo(rows, [str, float, int])
    linea = ((func(val) for func, val in zip([str, float, int], row)) for row in rows)
    
    # lineas = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    lineas = (dict(zip(['nombre', 'precio', 'volumen'], lin)) for lin in linea)
    
    return lineas

# def filtrar_datos(rows, nombres):
#     for row in rows:
#         if row['nombre'] in nombres:
#             yield row
            

def ticker(camion_file, log_file, fmt):
    
    import informe_final
    from formato_tabla import crear_formateador, imprimir_tabla
    
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    # rows = filtrar_datos(rows, camion)
    rows = (row for row in rows if row['nombre'] in camion)
    formato = crear_formateador(fmt)
    cols = ['Nombre', 'Precio', 'Volumen']
    formato.encabezado(cols)
    
    for row in rows:
        d = []
        for r in row:
            d.append(str(row[r]))
        formato.fila(d)


if __name__ == '__main__':
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    # rows = filtrar_datos(rows, camion)
    rows = (row for row in rows if row['nombre'] in camion)
    for row in rows:
        print(row)
        