# -*- coding: utf-8 -*-
"""
Spyder Editor

mail: gustavogodoy85@gmail.com
"""


# h = input("ingrese un valor de altura inicial, por defecto sera 100m: ")

# if h == '' :
#     h = 100
#     print("El valor ingresado es: ", h)
# else :
#     h = int(h, 10)
#     print("El valor ingresado es: ", h)

h = 100 
'''valor de inicio definido para obtener el resultado sin ingresar
 valores por teclado, comentar esta linea y descomentar lineas 9-16 si se
 desean ingresar valores por teclado'''

for i in range (1, 11, 1):
    h = h*3/5
    round_h = round(h, 4)
    print (i, ' ',round_h)

'''
Pruebas hechas con valores ingresados por teclado (ver codigo comentado)
ingrese un valor de altura inicial, por defecto sera 100m: 
El valor ingresado es:  100
60.0
36.0
21.6
12.96
7.776
4.6656
2.7994
1.6796
1.0078
0.6047

ingrese un valor de altura inicial, por defecto sera 100m: 50
El valor ingresado es:  50
30.0
18.0
10.8
6.48
3.888
2.3328
1.3997
0.8398
0.5039
0.3023

'''
