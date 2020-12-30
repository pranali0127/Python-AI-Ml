# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:50:15 2020

@author: PRIYAMATE
"""

#5. Generate a 1D array and reverse it using numpy slicing.
 
import numpy as np
x = np.arange(11)
print("original array : ",x)
print("Reversed array : ", np.flip(x))