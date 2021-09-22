
from fileparse import parse_csv


# Funcion leer_camion modificada
def leer_camion(nombre_archivo):
    '''Lee un archivo csv usando el modulo fileparse.'''
    camion = parse_csv(nombre_archivo, types = [str, int, float], has_headers = True)
    return camion

# Funcion leer_precios modificada
def leer_precios(nombre_archivo):
    '''Lee un archivo csv usando el modulo fileparse.'''
    precios = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    precios = dict(precios)
    return precios

# Funcion que genera la lista para el informe
def hacer_informe(camion, precios):
    '''Genera la lista para el informe'''
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista

# Funcion que imprime el informe en consola
def imprimir_informe(informe):
    '''Imprime el informe'''
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${f"{precio:.2f}"}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


# Funcion que hace el llamado al resto de funciones
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''Funcion de alto nivel que llama al resto de funciones'''
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    imprimir_informe(informe)

# informe_camion('../Data/camion.csv', '../Data/precios.csv')


