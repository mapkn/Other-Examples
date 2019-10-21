# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:48:17 2018

@author: patemi
"""

# Reference: https://snakify.org/en/lessons/sets/


A={1,2,3}


A = set('qwerty')
print(A)



A = {1, 2, 3}
B = {3, 2, 3, 1}
print(A == B)


# Each element may enter the set only once
C = set('Hello')
print(C)


# Iteration through set
for num in C:
    print(num)
    

# Check whether an element belongs to a set
A = {1, 2, 3}
print(1 in A, 4 not in A)

# Add an element 
A.add(4)


# Check number of lements
if len(A)==4:
    print(A)