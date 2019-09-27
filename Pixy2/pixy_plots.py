# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:02:11 2019

@author: Asish Yadav
"""

from __future__ import print_function
import sys
import numpy as np
import math
from matplotlib import pyplot as plt

if __name__=='__main__':
    input_data = "data5.txt"
    #input_data = sys.argv[1]
    
    
with open("%s" %(input_data)) as f:
    content = f.readlines()
arr = np.array(content)    
    
arr = np.delete(arr,0,0)
arr = np.delete(arr,0,0)    

xandy = []

for i in range(len(arr)-6):
    xandy.append(arr[i][14:25])

while '' in xandy:
    xandy.remove('')

x = []
y = []

for i in range(len(xandy)):
#i = 0
#while i < len(xandy):
 #   print (i)
    x.append(int(xandy[i][2:5]))
    y.append(int(xandy[i][8:11]))    

distance = []

for i in range(len(x)):
    distance.append(math.sqrt((x[i]*x[i])+(y[i]*y[i]))) 

for i in range(len(distance)):
    print('Distance moved by object from reference is:',"%0.2f" % round(distance[i],2))

plt.scatter(x,y)
    