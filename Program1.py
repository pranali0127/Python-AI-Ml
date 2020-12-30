# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:19:49 2020

@author: PRIYAMATE
"""

#1. Given a list of integers, create a numpy array from the list. The array should contain elements in
#reverse order and should be of type float.
#Sample input/output:
#input(a list): [1,2,3,4,5]
#output(a numpy array): [5.0,4.0,3.0,2.0,1.0]

import numpy as np

l= list(map(int,input("enter list ").split()))
print("list :",l)
l.reverse()
np_list = np.array(l,dtype=float)
print("np array of List :",np_list)