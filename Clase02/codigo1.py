# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:04:25 2021

"""

cadena = 'jamón'
capadepenapa = ''
for c in cadena:
        capadepenapa = capadepenapa + c
        if c == 'a':
            capadepenapa = capadepenapa + 'pa'
        elif c == 'e':
            capadepenapa = capadepenapa + 'pe'
        elif c == 'i':
            capadepenapa = capadepenapa + 'pi'
        elif c == 'o':
            capadepenapa = capadepenapa + 'po'
        if c == 'u':
            capadepenapa = capadepenapa + 'pu'
        print (capadepenapa)
        
# =============================================================================
# Buenas estimade.
# El ejercicio funciona, pero la salida con la sentencia print(capadepenapa)
# deberia estar fuera del ciclo for para que no imprima el proceso de formacion
# de capadepenapa, sino solamente su resultado final.
#
# Otra observación es que está demasiado limitado
# a lo pedido en la consigna y no tiene en cuenta otras cadenas de ingreso. Por
# ejemplo, si se ingresara la cadena 'Cualquiera', la salida seria
# "Cupuapalqupuipieperapa", la cual tiene un error al agregar la silaba 'pu' 
# luego de la letra u que sucede a la letra q. Lo mismo sucederia en palabras
# con diptongos, y no se agregarian las silabas correspondientes si la cadena 
# tuviera palabras con tilde o dieresis.
# Si bien el planteo del ejercicio no pedia contemplar las
# distintas posibilidades (diptongos, tildes, dieresis, etc.) es una buena
# forma de mejorar y aprender intentar que cada ejercicio sea lo mas
# completo posible. 
# =============================================================================
