# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:09:29 2021

@author: Gustavo

@mail: gustavogodoy85@gmail.com
"""

def propagar(v):

    for i in range(len(v)-1):            
        if v[i] == 0 and v[i+1] == 1:
            j = i
            while j>=0 and v[j] == 0:
                v[j] = 1
                j -= 1
        if v[i] == 1:
            if v[i+1] == 0:
                v[i+1] = 1 
    return v

def main():
    l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, -1, 0, 0]  
    print(l1)
    a = propagar(l1)
    print(a)
    l2 = [ 0, 0, 0, 1, 0, 0]
    print(l2)
    b = propagar(l2)
    print(b)
    l3 = [0, 0, 1, -1, 0, -1, 0, 0, 0, 1, -1]
    print(l3)
    c = propagar(l3)    
    print(c)