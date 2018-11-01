#!/usr/bin/env python3
import numpy as np 
import math

def modulus( y ):
    m=0
    for yi in y:
        m = m+yi^2
    return math.sqrt(m)

def obj_function1(x, qno):
    f1x = 0.5
    f2x=0.5
    gx=0
    for xi in x[:2]:
        gx = gx+((xi-0.5)*(xi-0.5)-math.cos(20*math.pi*(xi-0.5)))
    for i in range(1):
        f1x = f1x * x[i]
        f2x = f2x * (1-x[i])
    gx = modulus(x[2:])+gx
    gx = gx*100
    f1x = f1x*(1+gx)
    f2x = f2x*(1+gx)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx
    
def obj_function(x, qno):
    f1x=x*x
    f2x=(x-2)*(x-2)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    print(fx.shape)
    return fx 