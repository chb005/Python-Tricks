# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:43:07 2020

@author: CHIRAG BHATT
"""

#first of all you need to install:-pip install pyqrcode
#Second of all you need to install:pip install pypng

import pyqrcode

QR_name= 'Machine Learning in Hindi'
c = pyqrcode.create(QR_name)
c.png(QR_name+'.png',scale=13)

import os

os.system(QR_name+'.png')