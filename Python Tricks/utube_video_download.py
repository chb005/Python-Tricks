# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:29:17 2020

@author: CHIRAG BHATT
"""

#first of all you need to install:-pip install --upgrade youtube_dl


import youtube_dl,os

chb = {}

path = 'D:/eutube'

os.mkdir(path)

os.chdir(path)

link = 'https://www.youtube.com/watch?v=gssVCnqTRp8'

with youtube_dl.YoutubeDL(chb) as y:
    print("Video Downloading Progresses..."+link)
    y.download([link])
    
print("Video Successfuly Downloaded")