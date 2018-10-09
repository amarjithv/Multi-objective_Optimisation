#!/usr/bin/env python3
import numpy as np 

def obj_function(x, qno):
    fx=0
    if qno == 1:
        for i in range(x.shape[0]):
            fx = fx + (x[i]-1)**2
        for i in range(x.shape[0]-1):
            fx = fx - x[i]*x[i+1]
    elif qno == 2:
        for i in range(x.shape[0]):
            fx = fx + (i+1)*(x[i]**2)
    return fx

