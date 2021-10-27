#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:07:54 2021

@author: chulke
"""

def posiciones(a,b):
    pos = []
    def _posiciones(a,b):
        if a == '':
            return pos
        else:
            index = a.find(b)
            if pos == []:
                pos.append(index)
            else:
                pos.append(index+pos[-1]+len(b))
            _posiciones(a[index+len(b):], b)
            return pos
    
    x = _posiciones(a, b)
    return x
    
    
    
a = posiciones('Un tete a tete con Tete', 'te') # -> [3, 5, 10, 12, 21]