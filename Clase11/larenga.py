#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:44:29 2021

@author: chulke
"""

def pascal(n,k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    else:
        valor = pascal(n-1, k) + pascal(n-1, k-1)
        return valor
        
#h = pascal(5,2)