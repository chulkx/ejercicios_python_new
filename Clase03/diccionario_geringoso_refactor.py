# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:21:42 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def generar_geringoso(lista):
    vowels = 'aeiouAEIOUáéíóú'
    rules = [('u','a'), ('u','e'), ('u','i'),('u','o'), ('o','i'), ('o','u'),
             ('i','a'), ('i','e'), ('i','o'),('i','u'), ('e','i'), ('e','u'),
             ('a','i'), ('a','u')]
    dicc = {}
    #lista = ['banana', 'manzana', 'mandarina', 'ZANAHORIA']
    for word_orig in lista:
        i = 0
        new_word = ''
        upper = False
        if word_orig.isupper():
            word = word_orig.lower()
            upper = True
        else:
            word = word_orig
        for letter in word:
            if i == len(word)-1:
                context = (word[i], '')
            else:
                context = (word[i], word[i+1])
            if letter in vowels and context not in rules:
                if letter.islower():
                    new_word += letter.replace(letter, (letter + 'p' + letter))
                else:
                    new_word += letter.replace(letter, (letter + 'P' + letter))
            else:
                new_word += word[i]
            i += 1
        if upper:
            word = word.upper()
            new_word = new_word.upper()
            dicc[word] = new_word
        else:
            dicc[word] = new_word
    return dicc
    print(dicc)

# =============================================================================
# in [9]: lista = ['banana', 'manzana', 'mandarina', 'ZANAHORIA']
# 
# in [10]: lista
# Out[10]: ['banana', 'manzana', 'mandarina', 'ZANAHORIA']
# 
# d =generar_geringoso(lista)
# 
# d
# Out[12]: 
# {'banana': 'bapanapanapa',
#  'manzana': 'mapanzapanapa',
#  'mandarina': 'mapandaparipinapa',
#  'ZANAHORIA': 'ZAPANAPAHOPORIAPA'}
# 
# =============================================================================
