# Ejercicio 6.4, 6.5
# Uso el archivo provisto ya que el mio ya estaba medianamente ordenado con funciones

# tabla_informe.py
import csv
#%%
def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        for n_fila, fila in enumerate(filas, start = 1):
            record = dict(zip(encabezados, fila))
            try:
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
                camion.append(record)
            except ValueError:
                print('Faltan datos en la línea', n_fila, 'del archivo.')

    return camion
#%%
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows):
            
#            try:
#                precios[row[0]] = float(row[1])
#            except IndexError:
#                print('En la línea', i, 'faltan datos')
            
            if row: #### en vez del try-except se puede usar un if
                precios[row[0]] = float(row[1])
    return precios
#%%

#Modificaciones clase 6

def hacer_informe(camion, precios):
    '''Genera la lista para el informe'''
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista
#%%

def imprimir_informe(informe):
    '''Imprime el informe'''
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''Funcion de alto nivel que llama al resto de funciones'''
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    imprimir_informe(informe)
    

# %%
