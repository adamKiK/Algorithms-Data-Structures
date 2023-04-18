# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:22:21 2023

@author: POLUSER
"""

def bubble_sort(x):
    for i in range(len(x)):
        changed = False
        for j in range(0,len(x)-i-1):
            if x[j+1] < x[j]:
                temp_val = x[j]
                x[j] = x[j+1]
                x[j+1] = temp_val
                changed = True
        if changed != True:
            break
    return x

print(bubble_sort([2, 8, 9, 37, 17, 4, 46, 32, 13, 23, 48, 31, 43, 10, 14, 20, 6, 5, 40, 35]))