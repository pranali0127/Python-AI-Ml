# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:38:18 2020

@author: PRIYAMATE
"""
#3. Generate two integer matrices of size 3X5 and 7X5. Concatenate the matrices along axis 0.


import numpy as np

x = np.arange(15)
x = np.reshape(x,(3,5))
y = np.arange(35)
y = np.reshape(y,(7,5))
print("X:",x)
print("Y:",y)

print("Cpncatenation of x and y along axis = 0 :",np.concatenate((x,y),axis = 0))