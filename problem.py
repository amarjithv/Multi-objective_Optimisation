#!/usr/bin/env python3
import numpy as np 
import math
from math import cos, pi, sin
def modulus( y ):
    m=0
    for yi in y:
        m = m+yi^2
    return math.sqrt(m)

def DTLZ1(x, qno):
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
    
def schaffer(x, qno):
    f1x=x*x
    f2x=(x-2)*(x-2)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx

def DTLZ2(x, m):
    gx=(x[0]-0.5)**2+(x[1]-0.5)**2
    f1x=(1+gx)*cos(x[0]*pi*0.5)
    f2x=(1+gx)*sin(x[0]*pi*0.5)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx 

def DTLZ3(x, m):
    gx=0
    for xi in x[:2]:
        gx = gx+((xi-0.5)*(xi-0.5)-math.cos(20*math.pi*(xi-0.5)))
    f1x=(1+gx)*cos(x[0]*pi*0.5)
    f2x=(1+gx)*sin(x[0]*pi*0.5)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx 

def DTLZ4(x, m):
    gx=(x[0]-0.5)**2+(x[1]-0.5)**2
    f1x=(1+gx)*cos(x[0]**100*pi*0.5)
    f2x=(1+gx)*sin(x[0]**100*pi*0.5)
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx 
   
def DTLZ7(x, m):
    gx=1+(9/modulus(x))*(x[0]+x[1])
    hx=m-(f1x/(1+gx))*(1+sin(3*pi*f1x))
    f1x=x[0]
    f2x=(1+gx)*hx
    fx = []
    fx.append(f1x)
    fx.append(f2x)
    fx = np.array(fx)
    return fx 
