# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:41:08 2020

@author: PRIYAMATE
"""

#8. Generate a 2D matrix and normalize the matrix so that the elements range exactly between 0 and
#1. (What is normalization of a matrix?!. Figure it out!!)

import numpy as np

a = np.arange(0,27,3).reshape(3,3)
print(a)
row_sums = a.sum(axis=1) # array([ 9, 36, 63])
new_matrix = np.zeros((3,3))
for i, (row, row_sum) in enumerate(zip(a, row_sums)):
    new_matrix[i,:] = row / row_sum
    
print(new_matrix)