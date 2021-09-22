# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:40:59 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# costo_camion.py clase 6 usando la funcion leer_camion() del modulo informe_funciones.py

#Actualizacion clase 7, ejercicio 7.5
# =============================================================================
import sys
from informe_final import leer_camion


def costo_camion(ruta_archivo):
    '''
    Lee un archivo usando la funcion leer_camion()
    del modulo informe_final

    Parameters
    ----------
    ruta_archivo : ruta del archivo csv
    Actualizacion que permite ingresar archivos desde el interprete de python
    como desde la terminal
    
    Returns
    -------
    costo total

    '''
    camion = leer_camion(ruta_archivo)
    prod = 0.0
    for elemento in camion:
        try:
            prod += int(elemento['cajones'])*float(elemento['precio'])
        except ValueError:
            print(f'Valor erroneo para la clave {elemento["nombre"]}')
    return prod

def f_principal(param):
    if len(param) != 2:
        raise SystemExit(f'Uso adecuado {param[0]} ' 'archivo_camion')
    camion = param[1]
    costo = costo_camion(camion)
    print('Costo total: ', costo)

if __name__ == '__main__':  #permite que el programa se corra desde la terminal
    f_principal(sys.argv)