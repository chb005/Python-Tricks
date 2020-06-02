# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:00:24 2020

@author: CHIRAG BHATT
"""

#install:-pip install pillow

from PIL import Image

chb = 'C:/Users/CHIRAG BHATT/Music/ML Playlist/python tricks/imgtopdf.jpg'
output_pdf = Image.open(chb)
output_pdf.save('C:/Users/CHIRAG BHATT/Music/ML Playlist/python tricks/imgtopdf.pdf')

