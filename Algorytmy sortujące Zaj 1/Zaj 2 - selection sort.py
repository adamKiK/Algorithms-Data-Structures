# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:02:33 2023

@author: POLUSER
"""

def selection_sort(x):

    for i in range(len(x)):
        smallest = x[i]
        for j in range(i,len(x)):
            if x[j] < smallest:
                smallest = x[j]
                x[j] = x[i]
                x[i] = smallest
    return x
        
print(selection_sort([2, 8, 9, 37, 17, 4, 46, 32, 13, 23, 48, 31, 43, 10, 14, 20, 6, 5, 40, 35]))

# Działa ok