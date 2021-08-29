# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:53:35 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def pinito(n):
    i = 1
    pin = '*'
    while i < n:        
        print(f"{f'{pin: ^10s}':^60s}")
        pin += '*'*2
        i += 1
    return i

a = pinito(15)

    