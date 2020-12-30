# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:15:54 2020

@author: PRIYAMATE
"""

#7. Generate a 2D matrix of size 5X5. Delete it’s 2nd row and insert a new row in its place containing
#only NaN values.

import numpy as np

x = np.arange(25)
x = np.reshape(x,(5,5))
print("x :",x)
#removing second row
#x_del = np.delete(x, 1, 0)
#print("X after deleting second row :",x_del )
#inserting new row
#y = [None,None,None,None,None]
#print(y)

#inserting y as new row
#x_new = np.vstack((x_del , y))
#print("X after adding new row :",x_new)


x[1] = np.array([9,9,9,9,9])
print("X after adding new row :",x)