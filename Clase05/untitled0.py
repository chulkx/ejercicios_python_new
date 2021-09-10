#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:43:05 2021

@author: chulke
"""

###Hasta el ejercicio 5.15

import numpy as np          #importamos el módulo numpy para operar numéricamente
import random               #importamos el módulo random para obtener números "aleatorios"
import matplotlib.pyplot as plt

def crear_album(figus_total):
    albumfig=np.zeros(figus_total,dtype=np.int64)    #creamos un vector de ceros, nuestro álbum de figuritas
    
    return albumfig

# figus_total=670


def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False
    
    return



#compramos una figurita
def comprar_figu(figus_total):
    figu=random.randint(1,figus_total)  #obtenemos un número aleatorio entre 1 y la cantidad de figuritas del álbum
    
    return figu

def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    while album_incompleto(album) == True:      #mientras haya ceros en el vector álbum
        figurita=comprar_figu(figus_total)       #seguimos comprando figuritas
        album[figurita-1]+=1                    #la figurita número "i" corresponde a la posición "i-1" en el vector
    
    suma= album.sum()                            #cantidad de figuritas totales
    return suma


#Calculamos el promedio para 1000 repeticiones:

# n_repeticiones=1000
# lista=[cuantas_figus(figus_total) for i in range(n_repeticiones)]
# promedio=np.mean(lista)

#Y ahora lo hacemos con una función:

def experimento_figus(n_repeticiones, figus_total):
    lista=[cuantas_figus(figus_total) for i in range(n_repeticiones)]
    promedio=np.mean(lista)
    return promedio


# print('Hay que comprar un promedio de',experimento_figus(n_repeticiones, figus_total),'figuritas para llenar el álbum de',figus_total, 'figuritas.')

#Devuelve: Hay que comprar un promedio de 4751.221 figuritas para llenar el álbum de 670 figuritas.

#Hasta el 5.18:

# import random
# import numpy as np

#5.16_ Creamos un paquete:


# paquete=np.zeros(5,dtype=np.int64)    #creamos un vector con cinco ceros que será nuestro paquete
# for i in range(len(paquete)):               #generamos 5 figuritas por paquete
#     figurita= random.randint(1,figus_total) 
#     paquete[i]=figurita

# paquete
#5.17_ Ahora como función:

def comprar_paquete(figus_total,figus_paquete):
    paquete=[0]*figus_paquete         #creamos una lista con cinco ceros que será nuestro paquete
    for i in range(figus_paquete):                #generamos 5 figuritas por paquete
        figurita= random.randint(1,figus_total)
        paquete[i]=figurita              #asignamos cada figurita a una coordenada de la lista paquete
    
    return paquete

#5.18_ Contamos cuántos paquetes hay que comprar para llenar el álbum

def cuantos_paquetes(figus_total, figus_paquete):
    album=np.zeros(figus_total,dtype=np.int32)     #genero un álbum vacío, que es un vector de ceros
    total_paquetes=[]
    while album.min()==0:                          #mientras haya un espacio vacío en el álbum
        figpaquete=comprar_paquete(figus_total,figus_paquete)  #compro otro paquete
        total_paquetes.append(figpaquete)                      #los agrego a una lista para contar cuántos compré
        for figurita in figpaquete:                  #cada figurita del paquete
            album[figurita-1]+=1                     #corresponde a la posición "i-1" del álbum
    
    
    return len(total_paquetes)      #finalmente cuento cuántos paquetes hubo que comprar, que es lo que devuelve la función

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    nuevo = crear_album(figus_total)
    historia = []
    llenado = 0
    while album_incompleto(nuevo):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            nuevo[paquete.pop()-1] = 1
        llenado = (nuevo>0).sum()
        historia.append(llenado)
    return historia

def repeticiones(repe, figus_total, figus_paquete):
    promedio = np.mean([cuantos_paquetes(figus_total, figus_paquete) for i in range(repe)])
    return promedio


if __name__ == '__main__':
    figus_total= 670
    figus_paquete=5
    repe = 1000
    a = repeticiones(repe, figus_total, figus_paquete)
    print('comprar en promedio {a} paquetes')
    plt.plot(calcular_historia_figus_pegadas(670, 5))
    plt.show()
    
#Devuelve unos 882 paquete