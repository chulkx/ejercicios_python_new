#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 02:29:40 2021

@author: chulke
"""

def medidas_hoja_A(N):
    if N == 0:
        dimensiones = (841, 1189)
        return dimensiones
    else:
        dimensiones = (medidas_hoja_A(N-1)[1]//2, medidas_hoja_A(N-1)[0])
    return dimensiones

#a = medidas_hoja_A(3)