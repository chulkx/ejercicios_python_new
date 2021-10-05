#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:10:37 2021

@author: chulke
"""

import datetime as dt

def dias_habiles(inicio, final, feriados):
    '''
    Parameters
    ----------
    inicio : fecha de inicio con formato dd/mm/YYYY
    final : fecha final con formato dd/mm/YYYY
    feriados : lista con las fechas de los feriados en formato dd/mm/YYYY

    Returns
    -------
    laboral : Lista con las fechas laborables desde inicio hasta final
    '''
    
    ini = dt.datetime.strptime(inicio, '%d/%m/%Y')  #dia inicial
    fin = dt.datetime.strptime(final, '%d/%m/%Y')   #dia final
    no_lab = feriados.copy()    #copia de la lista de feriados para trabajar
    rango = fin - ini           #cantidad de dias por ver
   
    #ahora genero la lista cumpliendo las condiciones
    laboral = [(ini + dt.timedelta(days=dia)).strftime('%d/%m/%Y') for dia in range(rango.days+1) 
               if (ini + dt.timedelta(days=dia)).weekday() != 5 
               and (ini + dt.timedelta(days=dia)).weekday() != 6 
               and (ini + dt.timedelta(days=dia)).strftime('%d/%m/%Y') not in no_lab]
    
    return laboral

def test():
    print('Prueba sin feriados')
    a = dias_habiles('20/09/2020', '10/10/2020', [])
    print(a)
    print('')
    print('Prueba con feriados')
    b = dias_habiles('20/09/2020', '31/12/2020', ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020'])
    print(b)
    
if __name__ == '__main__':
    test()