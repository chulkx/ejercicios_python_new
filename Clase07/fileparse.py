"""
Created on Tue Sep 21 20:02:25 2021

@author: chulke
"""

# Ejercicio 7.1

import csv

def raise_error(select, header):
    if select and header==False:
        raise RuntimeError('Para seleccionar, necesito encabezados')

def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo csv en una lista de registros.
    Se puede seleccionar solo un subconjunto de las columnas, 
    determinando el parametro select, que debe ser una lista de nombres
    de las columnas a considerar.
    '''
    raise_error(select, has_headers) #llamo a la funcion que lanza una excepcion si es el caso
    
    # with open(iterable, encoding=('utf8')) as f: #
    # filas = csv.reader(f)
    filas = csv.reader(iterable)
    if has_headers:     #si hay header busco los indices de dichas columnas
        encabezados = next(filas)
        if select:      # segun se indique en select, busco los indices de las columnas pasadas como parametro
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
    else:               #si no hay header paso como indice una lista vacia
        indices = []
    registros = []
    for j, fila in enumerate(filas, start=1):
        if not fila:    #salteo las filas vacias
            continue
        if types:       #determino el tipo de dato de salida segun corresponda
            try:
                fila = [func(val) for func, val in zip(types, fila)] 
            except ValueError as e:
                if silence_errors:      #ej 7.3
                    pass
                else:
                    print(f'Fila {j}: No pude convertir {fila}')
                    print(f'Fila {j}: Motivo: {e}')
        if indices:     #elijo las columnas que paso como parametro
            fila = [fila[index] for index in indices]
        if has_headers: #si hay header armo los dicc
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        else:           #si no hay header armo las tuplas
            registro = tuple(fila)
            registros.append(registro)
    return registros

def archivo_a_filas(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):        #ejercicio 7.6
    with open(nombre_archivo, 'rt') as f:
        camion = parse_csv(f)
        return camion
        
def test():
    algo = archivo_a_filas('../Data/missing.csv', types = [str, int, float]) #ej 7.2, 7.3

    # lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    # algo = parse_csv(lines, types=[str, int, float])
    print(algo)
    
if __name__ == '__main__':
    test()