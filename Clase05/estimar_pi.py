#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:30:23 2021

@author: chulke
"""
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def aprox_pi():
    a = False
    punto = generar_punto()
    vector = punto[0]**2 + punto[1]**2
    if vector < 1:
        a = True
    return a

def estimar_pi(n=100000):
    p_circ = sum([aprox_pi() for i in range(n)])
    pi_aprox = (p_circ*4/n)
    print(pi_aprox)

estimar_pi()