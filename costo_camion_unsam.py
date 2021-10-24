#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# costo_camion.py

#%% ejercicio 7.5
import informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    costo_total = 0
    for registro in camion:
        costo_total += registro['cajones']*registro['precio']
    return costo_total

def f_principal(argumentos):
    costo = costo_camion(argumentos[1]) 
    print(f'Costo total: {costo}')
#%%    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






















