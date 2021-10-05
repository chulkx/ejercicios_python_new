#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:18:36 2021

@author: chulke
"""
#ejercicio 8.2
# devuelve los dias faltantes hasta la proxima primavera
from datetime import datetime, date

def falta_para_primavera():
    hoy = datetime.today()
    primavera = datetime(hoy.year, 9, 21)
    
    faltan = hoy - primavera
    
    return faltan.days