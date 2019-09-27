# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:55:53 2019

@author: Asish Yadav
"""

string1 = 'kitten'
string2 = 'sitting'
string3 = ''
distance = 0
for i in range(len(string1)):
    if string2[i] != string1[i]:
        distance+=1
distance += len(string2) - len(string1)
print (distance)        
        