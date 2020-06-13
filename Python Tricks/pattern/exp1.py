# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:33:34 2020

@author: CHIRAG BHATT
"""

lines = int(input("Enter the number of rows "))

for num in range(1,lines):
    for i in range(num):
        print(num, end=" ")
    
    print(" ")