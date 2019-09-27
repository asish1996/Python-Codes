# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:16:38 2019

@author: Asish Yadav
"""

string = 'AAAABBBCCDAAABBBBZZZZUUU'
in_char = string[0]
string2 = ''
count = 0
for i in range(len(string)):
    if string[i] == in_char:
        count+=1
    else:
        string2+= str(count) + in_char
        in_char = string[i]
        count = 1
string2+= str(count) + in_char
print (string2)        