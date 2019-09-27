# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:34:24 2019

@author: Asish Yadav
"""

#Checker board | Placing of queen

order = 5
avoid_locs = 2*order - 1
row_position = 2
col_position = 3

temp_row = row_position
temp_col = col_position
count = 0

i = temp_row - 1
#i = 0
while i < order:
    if (temp_row <= order-1 and temp_col <= order-1):
        count+=1
        temp_row+=1
        temp_col+=1
    i = i+1
#print (count)
temp_row = row_position 
temp_col = col_position - 2
j = temp_row - 1
#j = 0
while j < order:
    #print (j)
    if (temp_row <= order-1 and temp_col <= order-1):
        #print (j)
        count+=1
        temp_row+=1
        temp_col-=1
    j = j+1

print (count)
#k = 
#while k < order:    
      