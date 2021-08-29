# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:34:57 2021

@author: Gustavo Godoy

email: gustavogodoy85@gmail.com
"""

sentence = input('Por favor ingrese el texto a convertir en Geringoso: ')
if sentence == '':
    sentence = 'Geringoso'
word = ''
new_sentence = sentence.split(' ')
a_new_word = ''

for word in new_sentence:
    i=0
    for letter in word:

        if letter == 'a' :
            a_new_word = a_new_word + letter + 'p' + letter
        elif letter == 'e':
            a_new_word = a_new_word + letter + 'p' + letter
        elif letter == 'i':
            a_new_word = a_new_word + letter + 'p' + letter
        elif letter == 'o':
            a_new_word = a_new_word + letter + 'p' + letter
        elif letter == 'u':
            a_new_word = a_new_word + letter + 'p' + letter
        else:
            a_new_word = a_new_word + word[i]
        i += 1

    a_new_word = a_new_word + ' '

print(a_new_word)
