# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:12:15 2023

@author: POLUSER
"""

def insertion_sort(x):
    i = 0
    while i < (len(x)-1): # Indeksowanie od zera, więc długosc listy -1
        if x[i+1] < x[i]:
            temp_val = x[i]
            x[i] = x[i+1]
            x[i+1] = temp_val
            i = 0
        else:
            i += 1
    return x


print(insertion_sort([2, 8, 9, 37, 17, 4, 46, 32, 13, 23, 48, 31, 43, 10, 14, 20, 6, 5, 40, 35]))