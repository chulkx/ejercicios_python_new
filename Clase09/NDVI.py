#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:20:04 2021

@author: chulke
"""

import numpy as np
import os
import fnmatch
import sys
import pandas as pd
from scipy import stats as st
from mpl_toolkits.axes_grid1 import make_axes_locatable
# import gdal
from matplotlib import pyplot as plt

# def ejercicio_inicial():
#     data = []
#     for root, dirs, files in os.walk(os.path.join('..', 'Data', 'clip')):
#         for name in files:
#             if fnmatch.fnmatch(name, '*.npy'):
#                 data.append(np.load(os.path.join(root, name)))
#     for d in data:
#         plt.imshow(d, vmin = -0.5, vmax = 5)
#         # plt.hist(d.flatten(), bins = 100)

def crear_img_png(carpeta, banda):
    '''Ejercicio 9.15'''
    for root, dirs, files in os.walk(carpeta):
        for name in files:
            if name == banda:
                
                plt.figure(figsize=(8, 5))
                a = np.load(os.path.join(root, name))
                
                media = (a.cumsum())/len(a)
                mediana = np.median(a)
                moda = st.mode(a)
                vmin = np.percentile(a.flatten(), mediana)
                vmax = np.percentile(a.flatten(), 100 - mediana)
                
                plt.title(name, fontsize = 10)
                ax = plt.gca()
                im = plt.imshow(a, vmin = vmin, vmax = vmax)
                
                divider = make_axes_locatable(ax)
                cax = divider.append_axes('right', size='5%', pad=0.05)
                plt.colorbar(im, cax = cax)
                
                plt.savefig(name+'.png')
                
def crear_hist_png(carpeta, banda, bins):
    for root, dirs, files in os.walk(carpeta):
        for name in files:
            if name == banda:
                plt.figure()
                a = np.load(os.path.join(root, name))
                plt.hist(a.flatten(), bins = bins)
                plt.title(name, fontsize = 10)
                plt.show()

def todas(carpeta):
    for root, dirs, files in os.walk(carpeta):
        for name in files:
            # crear_img_png(carpeta, name)
            crear_hist_png(carpeta, name, 100)

todas('../Data/clip')
# crear_img_png('../Data/clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy')

# crear_hist_png('../Data/clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy', 100)
