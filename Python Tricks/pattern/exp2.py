# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:21:57 2020

@author: CHIRAG BHATT
"""

lines = int(input("Enter the number of rows "))

for num in range(1,lines+1):
    for i in range(1,num+1):
        print(i, end=" ")
    
    print(" ")