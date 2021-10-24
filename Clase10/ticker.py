#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:19:39 2021

@author: chulke
"""

from vigilante import vigilar
import csv


def parsear_datos(lines):
    rows1 = csv.reader(lines)
    rows = ((row[index] for index in [0, 1, 2]) for row in rows1)
    linea = ((func(val) for func, val in zip([str, float, int], row)) for row in rows)
    lineas = (dict(zip(['nombre', 'precio', 'volumen'], lin)) for lin in linea)
    return lineas



def ticker(camion_file, log_file, fmt):
    
    import informe_final
    from formato_tabla import crear_formateador
    
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
        