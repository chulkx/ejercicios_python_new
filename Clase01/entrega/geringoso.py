# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 18:28:56 2021

@author: Gustavo
"""

# sentence = input('Por favor ingrese el texto a convertir en Geringoso: ')
# if sentence == '':
#     sentence = 'Geringoso'
sentence = 'Convirtiendo una frase del castellano al geringoso'
new_sentence = sentence.split(' ')
new_word = ''
output_sentence = ''
vowels = 'aeiouAEIOUáéíóú'
rules = [('u','a'), ('u','e'), ('u','i'),('u','o'), ('o','i'), ('o','u'),
         ('i','a'), ('i','e'), ('i','o'),('i','u'), ('e','i'), ('e','u'),
         ('a','e'),('a','i'), ('a','o'), ('a','u')]

for word in new_sentence:
    i = 0
    new_word = ''
    for letter in word:
        if i == len(word)-1:
            context = (word[i],'')
        else:
            context = (word[i],word[i+1])
        if letter in vowels and context not in rules:
            new_word += letter.replace(letter, (letter + 'p' + letter))
        else :
            new_word += word[i]
        i += 1
    output_sentence += new_word + ' '
            
print(output_sentence)

# Por favor ingrese el texto a convertir en Geringoso:
#       Convirtiendo una frase del castellano al geringoso
#       Coponvipirtiependopo upunapa frapasepe depel 
#       capastepellapanopo apal geperipingoposopo