# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:41:23 2020

@author: CHIRAG BHATT
"""

rows = int(input("enter number of rows "))
b = 0

# range(start, stop, step)

for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')