# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:40:59 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# costo_camion.py clase 6 usando la funcion leer_camion() del modulo informe_funciones.py
# =============================================================================
from informe_funciones import leer_camion


def costo_camion(ruta_archivo):
    '''
    Lee un archivo usando la funcion leer_camion()
    del modulo informe_funciones

    Parameters
    ----------
    ruta_archivo : ruta del archivo csv

    Returns
    -------
    prod = costo total

    '''
    camion = leer_camion(ruta_archivo)
    prod = 0.0
    for elemento in camion:
        try:
            prod += int(elemento['cajones'])*float(elemento['precio'])
        except ValueError:
            print(f'Valor erroneo para la clave {elemento["nombre"]}')
    return prod

def test():
    costo = costo_camion('../Data/camion.csv')
    print('Costo Total: ', costo)