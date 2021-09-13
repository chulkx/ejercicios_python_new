#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:17:41 2021

@author: chulke
"""

import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temp = np.load('../Data/temperaturas.npy')
    plt.hist(temp, bins=45)
    plt.show()
    
def test():
    a = plotear_temperaturas()
    return a
    
    