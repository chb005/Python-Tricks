# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:23:00 2020

@author: CHIRAG BHATT
"""

import cv2

cam = cv2.VideoCapture(0)
count= 0

while (True):
    ret, frame = cam.read()
    path = 'C:/Users/CHIRAG BHATT/Music/ML Playlist/python tricks/faceimg/chb' + str(count) + '.jpg'
    print('Created image..' + path)
    cv2.imwrite(path, frame)
    count += 1
    if count>25:
        break
    cv2.imshow('chb', frame)
    k = cv2.waitKey(58) & 0xff
    if k == 89:
        break

cam.release()
cv2.destroyAllWindows()