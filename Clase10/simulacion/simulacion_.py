# -*- coding: utf-8 -*-
"""
mundo.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""


import random


def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)


    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))
                #print('A -1')

    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            #print('animal', animal)
            
            '''Reproduccion Leones'''
            if animal.es_leon() and animal.puede_reproducir():
                animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
                #print('animales cercanos ', animales_cercanos)
                animales_cercanos_repr = [(a,b) for (a,b) in animales_cercanos if b.es_leon()]
                
                #print('animales cercanos repr ', animales_cercanos_repr)
                if  animales_cercanos_repr:
                    animales_cercanos_repr = random.choice(animales_cercanos_repr)
                    #print('despues del choice: ', animales_cercanos_repr)
                    animales_cercanos_repr = animales_cercanos_repr[-1]
                    if animales_cercanos_repr.sexo != animal.sexo:
                        animales_cercanos_repr.tener_cria()
                        #print('envio a reproducir: ', animales_cercanos_repr)
                        posicion_nacimiento = animal.reproducirse(animales_cercanos_repr, self.tablero.posiciones_libres())
                        #print('posicion nacimiento: ', posicion_nacimiento)
                        self.tablero.ubicar(posicion_nacimiento, Leon())
                        animal.tener_cria()

            '''Reproduccion Antilopes'''
            if animal.es_antilope() and animal.puede_reproducir():
                animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
                #print('animales cercanos ', animales_cercanos)
                animales_cercanos_repr = [(a,b) for (a,b) in animales_cercanos if b.es_antilope()]
                
                #print('animales cercanos repr ', animales_cercanos_repr)
                if  animales_cercanos_repr:
                    animales_cercanos_repr = random.choice(animales_cercanos_repr)
                    #print('despues del choice: ', animales_cercanos_repr)
                    animales_cercanos_repr = animales_cercanos_repr[-1]
                    if animales_cercanos_repr.sexo != animal.sexo:
                        animales_cercanos_repr.tener_cria()
                        #print('envio a reproducir: ', animales_cercanos_repr)
                        posicion_nacimiento = animal.reproducirse(animales_cercanos_repr, self.tablero.posiciones_libres())
                        #print('posicion nacimiento: ', posicion_nacimiento)
                        self.tablero.ubicar(posicion_nacimiento, Antilope())
                        animal.tener_cria()
        # pass

    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.ciclo += 1

    def pasar_un_ciclo(self):
        #print([[x, x.edad, x.energia, x.sexo, x.es_reproductore, x.reproducciones_pendientes] for x in self.tablero.elementos() if x.es_leon()])
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()


    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if True:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()




# -*- coding: utf-8 -*-
"""
tablero.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
from random import choice

class Tablero(object):
    """docstring for Tablero"""
    # constructor
    def __init__(self, filas, columnas):
        super(Tablero, self).__init__()
        self.filas = filas
        self.columnas = columnas
        self.posiciones = {}
        self.n_posiciones_libres = self.filas * self.columnas

    # modificadores
    def ubicar(self,  pos, elem):
        if not self.ocupada(pos):
            self.n_posiciones_libres -= 1
        self.posiciones[pos] = elem
        return pos in self.posiciones

    def retirar(self, pos):
        self.n_posiciones_libres += 1
        return self.posiciones.pop(pos)

    def mover(self, p_origen, p_destino):
        self.ubicar(p_destino, self.retirar(p_origen))

    # getters
    def posicion(self, pos):
        return self.posiciones[pos]

    def ocupada(self,  pos):
        return pos in self.posiciones

    def libre(self,  pos):
        return pos not in self.posiciones

    def elementos(self):
        return list(self.posiciones.values())

    def n_filas(self):
        return self.filas

    def n_columnas(self):
        return self.columnas

    # modificadores complejos
    def ubicar_en_posicion_vacia(self, elem):
        if not self.hay_posiciones_libres():
            raise RuntimeError("Estás intentado agregar algo al tablero y está lleno")

        pos = choice(self.posiciones_libres())
        self.ubicar(pos, elem)


    # consultas
    def hay_posiciones_libres(self):
        return self.n_posiciones_libres > 0
        # return len(self.posiciones) <  self.filas * self.columnas

    def posiciones_ocupadas(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.ocupada((f,c)):
                    res.append((f,c))

        return res

    def posiciones_libres(self):
        res = []
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.libre((f,c)):
                    res.append((f,c))

        return res


    def posiciones_vecinas_libre(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ p for p in res if self.libre(p)]

        return res

    def posiciones_vecinas_con_ocupantes(self, pos):
        res = self.posiciones_vecinas(pos)
        res = [ (p, self.posicion(p)) for p in res if self.ocupada(p)]

        return res

    # auxiliar
    def posiciones_vecinas(self, pos):
        desp=[(-1, -1), (-1, 0), (-1, 1),(0, 1), (1, 1), (1, 0),(1, -1), (0, -1)]

        for i in range(len(desp)):
            f = (desp[i][0] + pos[0])
            c = (desp[i][1] + pos[1])
            desp[i] = (f, c)

        desp = [ (f,c) for f,c in desp if (0<=f and f<self.filas) and (0<=c and c<self.columnas) ]

        return desp


    # impresion
    def __repr__(self):
        res = ""
        for f in range(self.filas-1,-1,-1):
            for c in range(self.columnas):
                res += f"{(str(self.posiciones[(f,c)]) if (f,c) in self.posiciones else '-'):^3}"
            res += "\n"

        return res


    def __str__(self):
        return self.__repr__()



if __name__ == "__main__":
    t = Tablero(2,3)

    for i in range(6):
        t.ubicar_en_posicion_vacia(i)


# -*- coding: utf-8 -*-
"""
animal.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
import random


class Animal(object):
    """docstring for Animal"""
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = random.choice(['M', 'H'])
        #self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.energia = self.energia_maxima
        self.es_reproductore = False
        

    def pasar_un_ciclo(self):
        self.energia -= 1 # Se puede restar si no llega a comer
        self.edad += 1
        if self.reproducciones_pendientes > 0 and self.edad >= 2: #
            self.es_reproductore = True

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo
        debería depender de la diferencia entre su nivel de energía y su energía máxima"""
        return self.energia < self.energia_maxima
        #pass

    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    def puede_reproducir(self):
        return self.es_reproductore

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria para evitar que tengamás de una cria por ciclo, etc"""
        self.reproducciones_pendientes -= 1
        self.es_reproductore = False
        # pass

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if vecinos:
            #animal = random.choice(vecinos)
            animal = vecinos
            if lugares_libres:
                animal.tener_cria()
                self.tener_cria()
                pos = random.choice(lugares_libres)

        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)

        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Leon(Animal):
    """docstring for Leon"""
    def __init__(self):
        self.energia_maxima = 6
        self.edad_maxima = 10
        super(Leon, self).__init__()
        #print('L +1 ', self.sexo)

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # y hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)

        return pos


    def __repr__(self):
        # return "León"
        return "L{}".format(self.edad)
    
    



class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        self.energia_maxima = 10
        self.edad_maxima = 6
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 3
        #print('A +1 ', self.sexo)
        
    def es_antilope(self):
        return True

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)


m = Mundo(12, 6, 5, 15, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(2)
    print(i +1)
    print(m)
