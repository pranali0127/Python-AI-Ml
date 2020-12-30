# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:53:33 2020

@author: PRIYAMATE
"""
#6. Generate a 2D matrix “M”. Use numpy to generate a new matrix “N” from “M” such that “N”
#only contains the elements of “M” which are in odd rows and even columns.


import numpy as np

M = np.arange(15)
M = np.reshape(M,(3,5))
N =[]
for i in range(3):
    for j in range(5):
        if i%2!=0 and j%2==0:
            N.append(M[i,j])

N = np.array(N)
print("M :",M)
print("N :",N)