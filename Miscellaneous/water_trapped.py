# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:47:02 2019

@author: Asish Yadav
"""

ele = [3,0,1,3,0,5]
temp_num = ele[0]
if temp_num > ele[-1]:
    temp_num = ele[-1]
    
units = 0
for i in range(len(ele)-1):
    if ele[i] < temp_num:
        units+= temp_num - ele[i]
print (units)        
