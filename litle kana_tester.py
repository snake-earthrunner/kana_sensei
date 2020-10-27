#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:58:09 2020

@author: earthrunner
"""
import pandas as pd
#import pykakasi #migt need to be pip installed  #package that contains the kana signs
import random

path = "/Users/earthrunner/Documents/Python_scripts/test the kana ka.xlsx"

data_frame_hiragana = pd.read_excel(path)

new_data_frame_hiragana = data_frame_hiragana.set_index('laut')

hiragana_list = new_data_frame_hiragana.values.tolist() 

flattened_hiragana_list = [y for x in hiragana_list for y in x]

clean_hiragana_list = []
for sign in flattened_hiragana_list:
    if sign != "X":
        clean_hiragana_list.append(sign)

print (clean_hiragana_list)

def test():
    while True:
        allowed = ["k","s","t","n","h","m","y","r","w","g","z","d","b","p"]
        word_asked = random.choice(clean_hiragana_list)
        print (word_asked)
        word_given = input("Type your solution: ")
        if word_given == "end":
            print ("See You soon!  Thanks for learning the hiragana!")
            break
        else:
            #print([word_given[i:i+1] for i in range(0, len(word_given))])

            store = ([word_given[i:i+1] for i in range(0, len(word_given))])

            #for item in store:
                #print (str(item))

                #print (new_data_frame_hiragana.loc[store[0], store[1]])

            #if new_data_frame_hiragana.loc[store[0], store[1]] == word_asked:
                #print ("congrats you learn well")
            
            if not word_given.startswith(tuple(allowed)) == True:
                          
                print ("Hell boy,...You better get back to hiragana school! Try another hiragana now...")
               
            elif new_data_frame_hiragana.loc[store[0], store[1]] == word_asked:
                print ("congrats you learn well")
            #else: 
                #new_data_frame_hiragana.loc[store[0], store[1]] != word_asked:
                #print ("Sorry that was worng.  Keep on practicing little, cute human beeing")

test()

