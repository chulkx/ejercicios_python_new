# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:31:01 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""
# solucion_de_errores.py
# Ejercicio de errores en el código

#%% Ejercicio 3.1 Semántica

# Esta función devuelve un True o un False evaluando solo el primer elemento del string.
# Esto sucede ya que si el primer elemento no es una 'a' entonces entra en el else y el 
# return nos devuelve False y la función termina.
# Una posible solución es la presentada a continuación, donde se agregaron las coincidencias con A y á.
# Ademas se agrego una comprobación de que el ingreso al else sea válido solo para el último elemento 
# del string ingresado.


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'á' or expresion[i] == 'A':
            return True
        else:
            if i == n-1:
                return False
        i += 1

# Otra solución podria ser la siguiente
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a' or expresion[i] == 'á' or expresion[i] == 'A':
#             return True
#         i += 1
#     return False

a = tiene_a('UNSAM 2020')
b = tiene_a('abracadabra')
c = tiene_a('La novela 1984 de George Orwell')
d = tiene_a('No existe el simbolo en el string')
print(a,b,c,d)

#%% Ejercicio 3.2 Sintaxis

# #Primer error encontrado: falta ':' en la primera linea, donde se define la función
# def tiene_a(expresion)
#                       ^
# SyntaxError: invalid syntax
# #Segundo error encontrado: falta ':' en la declaración del while
# while i<n
#          ^
# SyntaxError: invalid syntax

# #Tercer error encontrado: hay un error en la condición del if (usa = en lugar de ==), se esta usando
# #un operador de asignación en lugar del operador de comparación
# if expresion[i] = 'a'
#                 ^
# SyntaxError: invalid syntax

# #Cuarto error:  falta ':' en la declaración del if 
# if expresion[i] == 'a'
#                       ^
# SyntaxError: invalid syntax

# #Quinto error: esta mal escrito el bolleano False.
# return Falso

# NameError: name 'Falso' is not defined

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%% Ejercicio 3.3 Tipos

# Primer error: si se ingresa un numero y no un string no podemos aplicar el metodo len()


def tiene_uno(expresion):
    expresion = str(expresion)#linea agregada para solucionar el caso particular
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%% Ejercicio 3.4 Alcances

# Primer error: la función suma no esta devolviendo nada.

def suma(a,b):
    c = a + b
    return c #linea agregada

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%% Ejercicio 3.5 Pisando memoria

# El problema en este ejercicio es que al ser la variable encabezado un diccionario, sus  keys
# no se pueden repetir, por lo que al usar siempre las mismas keys se van cambiando sus valores
# en cada iteración del for fila in filas:.
# Puedo soucionarlo de dos maneras. Creando la estructura del diccionario dentro del ciclo antes mencionado
# o limpiando la misma luego de haber agregado el diccionario a la lista camion.

# Salida de datos original:
#     [{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]

# =============================================================================
# Opción 1
# =============================================================================

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     #registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro = {
#                 encabezado[0] : fila[0],
#                 encabezado[1] : int(fila[1]),
#                 encabezado[2] : float(fila[2])
#             }
#             camion.append(registro)
#     return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)


# Salida de datos:
#     [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
#      {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
#      {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
#      {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
#      {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
#      {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]

# =============================================================================
# Opcion 2
# =============================================================================

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
            
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#             registro = {}
#     return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)

# Salida de datos:
#     [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
#      {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
#      {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
#      {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
#      {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
#      {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
#      {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]


