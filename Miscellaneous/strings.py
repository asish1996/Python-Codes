# -*- coding: utf-8 -*-
"""

@author: Neha Thakur
"""

dicti = {1:'bed', 2:'bath' , 3:'bedbath' , 4:'and' , 5:'beyond'}
arr = []
string = "bedbathandbeyond"
p = 0
for i in range(len(string)):
    for key in dicti:
        if string[p:i+1] == dicti[key]:
            arr.append(string[p:i+1])
            p = i+1
print (arr)            