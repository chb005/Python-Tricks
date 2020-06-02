# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:18:50 2020

@author: CHIRAG BHATT
"""

#first of all you need to install:pip install textblob(NLP library)

from textblob import TextBlob


def original_sent(text):
    nlpt=TextBlob(text)
    print("The original sentance is:",text)
    modified=nlpt.correct()
    print("The true sentance is:",modified)
    return modified

x1="plese stey avay form here"
original_sent(x1)

