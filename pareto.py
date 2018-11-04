#!/usr/bin/env python3
import numpy as np
import scipy as scp
import enum

def non_dominated_sorting(values):
    n=0;
    f=1;
    ans=[]
    for i in range(values.shape[0]):
        n=1
        for j in range(values.shape[0]):
            f=1
            for k in range(values.shape[1]):
                if(i==j):
                    f=0
                    continue
                if values[j][k]>values[i][k]:
                    f=0
                    break
            if f==1:
                n=n+1
                print("\n", j)
        ans.append(n)
    ans=np.array(ans)
#    values=np.concatenate((values, ans), axis=1)
#    prev=values[0][values.shape[1]-1]
#    p=values.shape[1]-1
#    j=1
#
#    for i in range(values.shape[0]):
#        if(values[i][p]>prev):
#            j=j+1
#            prev=values[i][p]
#            values[i][p]=j
#        else:
#            values[i][p]=j
#    
    return ans
       
def find_rank(values, soln):
    n=1
    f=1
    for j in range(values.shape[0]):
        f=1
        for k in range(values.shape[1]):
            if values[j][k]>soln[k]:
                f=0
                break
        if f==1:
            n=n+1
    return n
