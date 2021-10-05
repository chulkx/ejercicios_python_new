#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:49:08 2021

@author: chulke
"""

import os
import fnmatch
import sys

def archivos_png(directorio):
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if fnmatch.fnmatch(name, '*.png'):
                print(name)
            
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        archivos_png(sys.argv[1])