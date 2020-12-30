# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:22:13 2020

@author: PRIYAMATE
"""

#2. Generate a 4X3 matrix of random numbers using numpy. Reshape the matrix to 2X6 matrix.

import numpy as np

l_array = np.arange(12)
print(l_array)
new = np.reshape(l_array,(4,3) ) 
print("4x3 : ",new)
new_array = np.reshape(l_array,(2,6))
print("2x6 :",new_array)