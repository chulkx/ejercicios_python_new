# -*- coding: utf-8 -*-
"""
mundo.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""

from animal import Leon, Antilope
from tablero import Tablero
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
                print('A -1')

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
        print([[x, x.edad, x.energia, x.sexo, x.es_reproductore, x.reproducciones_pendientes] for x in self.tablero.elementos() if x.es_leon()])
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()


    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if False:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    m = Mundo(12, 6, 5, 15, debug=True)

    import time
    for i in range(20):
        m.pasar_un_ciclo()
        time.sleep(2)
        print(i +1)
        print(m)
