# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:32:48 2020

@author: PRIYAMATE
"""
#4. Generate 2 matrices of any dimension as per your choice and compute their inner and outer
#product.
import numpy as np
l_array = np.arange(12)
print(l_array)
x = np.reshape(l_array,(4,3) ) 
print(" X: ",x)
y = np.reshape(l_array,(4,3))
print("Y :",y)

print("inner product :",np.inner(x,y))
print("outer product :",np.outer(x,y))

