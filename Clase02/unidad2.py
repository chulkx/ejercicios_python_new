# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:58:04 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

# =============================================================================
# # 2.2 manejo de archivos
# =============================================================================
# %%
with open('../Data/camion.csv', 'rt') as f:
    data = f.read()
    # si llamo a la variable data obtengo toda la info sin formato
    # si hago print(data) obtengo la info formateada
    # De esta manera abro todo el archivo y lo cargo en memoria, lo cual
    # solo es practico si el archivo es pequeño.
    print(data)
# %%
# Para archivos grandes es mejor trabajar cargando en memoria partes del archivo

with open('../Data/camion.csv', 'rt') as f:
    for line in f:
        print(line, end='')
# %%
with open('../Data/camion.csv', 'rt') as f:
    header = next(f).split(',')
    print(header)
    for line in f:
        row = line.split(',')
        print(row)

#%% Ejercicio 2.3
with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        print(line)
        if 'Uva' in row:
            print(row[1])
            break

# %% 
# el modulo gzip me permite abrir archivos comprimidos
# al usar este modulo si o si debo usar 'rt', sino leere cadenas de bytes
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

# =============================================================================
# 2.3 Funciones
# =============================================================================

#%% definicion de funciones

def sumcount(n):
    total = 0
    while n>0:
        total += n
        n -= 1
    return total

a = sumcount(100)

#%% excepciones
#Para el manejo de excepciones, python utiliza try-except.
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

#Con esto se dan los argumentos para que la funcion corra normalmente, y 
#en caso de que la misma arroje un error este puede ser introducido en 
#la sentencia except error, y se realiza la operacion que se deba realizar.

#%% generar excepciones
#para generar excepciones se usa el comando raise

# =============================================================================
# puede ser necesario lanzar una excepcion en nuestra funcion que no este 
# declarada en las excepciones del sistema, y luego agarrarla para hacer 
# las tareas que sean necesarias.
# =============================================================================
