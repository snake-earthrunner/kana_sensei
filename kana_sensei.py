#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:39:33 2020

@author: earthrunner
"""

import pandas as pd
#import pykakasi #migt need to be pip installed  #package that contains the kana signs
import random

path = "./test_the_beautiful_kana.xlsx"

data_frame_hiragana = pd.read_excel(path, header=None)

print ("I am the almighty kana sensei. I will teach you the beautuful kana signs")
print ("Type (end) if you want to quit learning!")

while True:
    print("--------------------------------------")
    random_kana = "X"
    while random_kana == "X":
        konsonant = random.randint(1, 14)
        vokal = random.randint(1, 4)
        #print (konsonant)
        #print (vokal)
        random_kana = (data_frame_hiragana.iat[konsonant, vokal])
        #print (random_kana)
    
    random_kana1 = (data_frame_hiragana.iat[konsonant, 0]).strip()
    random_kana2 = (data_frame_hiragana.iat[0, vokal]).strip()

    #print("My sound starts with: ... " + random_kana1)
    #print ("My sound ends with: ... " + random_kana2)
    print ((random_kana) + "   I sound like.... ")

    word_given = input("Type your solution: ").strip().lower()
    if word_given == "end":
        print ("See You soon!  Thanks for learning the hiragana!")
        break
    elif random_kana1 + random_kana2 == word_given:
        print ("WELL DONE")
        print ("The next kana is...")
    else:
        print("Try again...please follow the hebrun system!")
        print("The correct answer to the hiragana " + random_kana + " is: " + random_kana1 + random_kana2)
