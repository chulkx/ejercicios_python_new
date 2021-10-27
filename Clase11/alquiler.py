#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 03:17:42 2021

@author: chulke
"""

import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

_x = np.linspace(start = 0, stop = 200, num = 1000)
_y = _x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('precio_alquiler ~ superficie')
plt.plot(_x, _y, c = 'green')
plt.xlabel('Superficie')
plt.ylabel('Precio')

plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
