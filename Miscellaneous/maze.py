# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:49:05 2019

@author: Asish Yadav
"""
import math

count = 0

def distance (p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def next_point (p):
    p1 = [p[0],p[1]-1]
    p2 = [p[0]-1,p[1]]
    p3 = [p[0],p[1]+1]
    p4 = [p[0]+1,p[1]]
    d1 = 10000
    d2 = 10000
    d3 = 10000
    d4 = 10000
    points = [p1,p2,p3,p4]
    if p[1]-1 >= 0:
        d1 = distance(p1,end_point)
    if p[0]-1 >= 0:
        d2 = distance(p2,end_point)
    if p[1]+1 < num_columns:
        d3 = distance(p3,end_point)
    if p[0]+1 < num_rows:
        d4 = distance(p4,end_point)
    d = [d1,d2,d3,d4]
    dmin = min(d)
    index = 1000
    for i in range(4):
        if d[i] == dmin:
            index = i
    ran_point = points[index]
    return count+=1    

num_rows = 4
num_columns = 4
matrix = [[0, 0, 0, 0],[1, 1, 0, 1],[0, 0, 0, 0],[0, 0, 0, 0]]
start_point = [3,0]
end_point = [0,0]
ran_point = start_point

if matrix[start_point[0]][start_point[1]] == 1:
    print ("Start point itself is blocked")
    
if matrix[end_point[0]][end_point[1]] == 1:
    print ("Choose a valid destination")
    
print (next_point(start_point))    