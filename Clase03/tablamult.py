# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 20:39:13 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def tabla_mult(number):
    number = number
    header = ('0','1','2','3','4','5','6','7','8','9')
    print(f'{"":>4s} {"%4s %4s %4s %4s %4s %4s %4s %4s %4s %4s" % header}')
    print(f'{"":->55}')
    row = 0
    col = 0
    while row <= number:
        numbers = []
        num = 0
        for col in range (10):
            numbers.append(str(num))
            num += row
        numbers = tuple(numbers)
        print(f'{str(row)+":":>4s} {"%4s %4s %4s %4s %4s %4s %4s %4s %4s %4s" % numbers}')
        row += 1
    
tabla = tabla_mult(9)

#%% version nueva

def tabla_mult(number):
    for n in range (10):
        print(f'{n:4d}', end=' ')
    print(f'{"":->50}')
    row = 0
    col = 0
    while row <= number:
        num = 0
        for col in range (10):
            print(f'{num:4d}', end=" ")
            num += row
        print('')
        row += 1
    
tabla = tabla_mult(9)