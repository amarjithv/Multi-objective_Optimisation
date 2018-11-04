#!/usr/bin/env python3
import numpy as np 
<<<<<<< HEAD

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

=======
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
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e
