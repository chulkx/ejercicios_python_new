#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:32:37 2021

@author: chulke
"""
#ejercicio 8.4
import datetime


def licencia():
    sale = datetime.datetime.strptime('26 septiembre, 2020', '%d %B, %Y')
    
    vuelve = sale + datetime.timedelta(days=200)
    
    print(vuelve)