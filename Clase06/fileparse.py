
import csv

def parse_csv(nombre_archivo, select = None, types = [str, int, float], has_headers = True):
    '''
    Parsea un archivo csv en una lista de registros.
    Se puede seleccionar solo un subconjunto de las columnas, 
    determinando el parametro select, que debe ser una lista de nombres
    de las columnas a considerar.
    '''
    with open(nombre_archivo, encoding=('utf8')) as f:
        
        filas = csv.reader(f)
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
        for fila in filas:
            if not fila:    #salteo las filas vacias
                continue
            if types:       #determino el tipo de dato de salida segun corresponda
                fila = [func(val) for func, val in zip(types, fila)] 
            if indices:     #elijo las columnas que paso como parametro
                fila = [fila[index] for index in indices]
            if has_headers: #si hay header armo los dicc
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:           #si no hay header armo las tuplas
                registro = tuple(fila)
                registros.append(registro)
    return registros
