# -*- coding: utf-8 -*-
"""
mundo.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""

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
                #print('A -1')


    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            
            '''Reproduccion Leones'''
            if animal.es_leon() and animal.puede_reproducir():
                animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
                animales_cercanos_repr = [(a,b) for (a,b) in animales_cercanos if b.es_leon()]
                if  animales_cercanos_repr:
                    animales_cercanos_repr = random.choice(animales_cercanos_repr)[-1]
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
                animales_cercanos_repr = [(a,b) for (a,b) in animales_cercanos if b.es_antilope()]
                if  animales_cercanos_repr:
                    animales_cercanos_repr = random.choice(animales_cercanos_repr)[-1]
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
        if False:        # Original en False
            res += '\nEspecie   Posicion   años  energia   sexo   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()




''' Codigo de la defifnicion de la clase Animal modificado'''


class Animal(object):
    """docstring for Animal"""
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = random.choice(['M', 'H'])       # Modificado
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
        self.es_reproductore = False    # Modificacion
        # pass

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if vecinos:
            #animal = random.choice(vecinos)
            animal = vecinos            # Modificacion
            if lugares_libres:
                animal.tener_cria()
                self.tener_cria()
                pos = random.choice(lugares_libres)

        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):  #lugares libres distancia 1
        '''Modificar para que Antilope se escape'''
        pos = None
        if self.es_antilope() and lugares_libres:
            #guardo los vecinos con dist 3 de x que estan ocupados
            vecindad = []
            for x in lugares_libres:
                for pos, animal in Tablero.posiciones_vecinas_con_ocupantes_3(m.tablero, x):
                    vecindad.append((pos, animal, x))

            #vecindad = [ (pos, animal, x) for (pos, animal, x) in Tablero.posiciones_vecinas_con_ocupantes_3(m.tablero, x) for x in lugares_libres]
            no_ir = []  #voy a guardar las posiciones que titnen leones al lado
            for a in vecindad:
                if a[1].es_leon():
                    no_ir.append(Tablero.posiciones_vecinas_con_ocupantes(m.tablero, a[2]))
            ir = random.choice(lugares_libres)
            while ir in no_ir:
                ir = random.choice(lugares_libres)

            pos = ir
                
        elif lugares_libres:
            pos = random.choice(lugares_libres)

        return pos

    def fila_str(self):         # Modificado para visualizar el sexo del animal
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}  {self.sexo:>3s}       {self.es_reproductore!s:<5}"

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

    def prob_caceria_ok(self):
        if self.edad < self.edad_maxima*20/100 or self.edad >= self.edad_maxima*80/100:
            prob = random.randrange(20)/100
        else:
            prob = random.randrange(21, 100)/100
        return prob

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            compas = len([ (pos, animal) for (pos, animal) in animales_vecinos if animal.es_leon()])
            
            if presas_cercanas: # y hay presas cerca
                #probabilidades de comer
                presa = random.choice(presas_cercanas)
                '''Vecindad: buscar como llamar al mundo creado sin usar m'''
                vecindad = Tablero.posiciones_vecinas_con_ocupantes(m.tablero, presa[0])
                compas_presa = len([ (pos, animal) for (pos, animal) in vecindad if animal.es_antilope() ])
               
                a = self.prob_caceria_ok()
                b = presa[-1].prob_escape_ok()
                
                if compas_presa > compas :              #si hay mas Antilopes que Leones
                    a = a - (compas_presa - compas)/100 # baja la prob de caceria ok
                    b = b + (compas_presa - compas)/100 # aumenta la prob de escape ok
                else:
                    a = a + (compas - compas_presa)/100
                    b = b - (compas - compas_presa)/100
                
                if a*( 1 - b) > 0.5:
                    super(Leon, self).alimentarse()
                    #(pos, animal) = random.choice(presas_cercanas)
                    pos = presa[0]
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

    def prob_escape_ok(self):
        if self.edad > self.edad_maxima*20/100 or self.edad >= self.edad_maxima*80/100:
            prob = random.randrange(20)/100
        else:
            prob = random.randrange(21, 100)/100
        return prob

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)


if __name__ == '__main__':

    import time
    m = Mundo(10, 10, 5, 3, debug=False)

    for i in range(20):
        m.pasar_un_ciclo()
        time.sleep(1)
        print(i +1)
        print(m)