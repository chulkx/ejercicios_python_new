#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:09:38 2021

@author: chulke
"""

class FormatoTabla:
    
    def encabezado(self, headers):
        '''Crea los encabezados'''
        raise NotImplementedError()
        
    def fila(self, rowdata):
        raise NotImplementedError()

        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        '''Crea los encabezados'''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
    def fila(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
        
class FormatoTablaCSV(FormatoTabla):
    '''Genera una tabla en formato CSV'''
    def encabezado(self, headers):
        print(','.join(headers))
        
    def fila(self, rowdata):
        print(','.join(rowdata))


class FormatoTablaHTML(FormatoTabla):
    def encabezado(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end = '')
        print('</tr>')
        
    def fila(self, rowdata):
        print('<tr>', end = '')
        for dat in rowdata:
            print(f'<td>{dat}</td>', end = '')
        print('</tr>')
        
        
def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Formato desconocido {nombre}')
    return formateador


def imprimir_tabla(data, cols, formato):
    for c in cols:
        print(f'{c:>10s}', end = ' ')
    print()
    print(('-'*10 + ' ')*len(cols))
    for d in data:
        for c in cols:
            print(f'{getattr(d, c):>10}', end = ' ' )
        print()
    