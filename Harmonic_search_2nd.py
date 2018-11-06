#!/usr/bin/env python3
import numpy as np
import scipy as scp
import enum
from pygmo import *
import matplotlib.pyplot as plt
from pareto import non_dominated_sorting
from problem import DTLZ2
from pareto import find_rank
def find_worst(ranks, crowd_d):
    worst = 0
    for i in range(ranks.shape[0]):
        if ranks[i] > ranks[worst]:
            worst = i
        elif ranks[i]==ranks[worst]:
            if crowd_d[i]<crowd_d[worst]:
                worst = i
    return worst

    
#Ennumerate
class Objectives(enum.Enum):
    maximize = 1
    minimize = 0

#problem_statement
upper_bound = 1
lower_bound = 0
upper_bound1 = 1
lower_bound1 = 0
question_no = 1 

#Parameter configuration
hmcr = 0.95
hms = 100
mi = 100
par = 0.1
bw = 0.01*(upper_bound-lower_bound)
no_of_var = 2
objective = 0
M = 2

#Memory Initialization
hm = np.random.rand(hms, no_of_var)*(upper_bound1-lower_bound1)+lower_bound1
#hm[5]=[11, 11]
new_soln = np.zeros(no_of_var)
function_value = np.zeros((hms, M))

#hm[5] = [0, 0]

for i in range(hms):
    function_value[i] = DTLZ2(hm[i], question_no)#define the function

rank = non_dominated_sorting(function_value)
print(rank)
import sys
#sys.exit()
plt.plot(hm[:,0],hm[:,1],'ro')
plt.show()
#plotting
fig = plt.figure(2)
ax=fig.add_subplot(111)
y=np.arange(hms)
hv=hypervolume(hm)
r=[11,11]
h=hv.compute(r)
k=[]
k.append(h)
print(h)
while(mi>0):
#    col = np.where(hm==new_soln,'b','r').flatten()
#    ax.scatter(hm[:,1],hm[:,0],c=col,s=25,linewidth=0)
#    plt.draw()
#    plt.pause(0.001)
    rank = non_dominated_sorting(function_value)
    hm2=np.zeros((hms, no_of_var))
    for iterator in range(hm.shape[0]):

        for i in range(no_of_var):
    
            uniform_distribution = np.random.random_sample()
            if uniform_distribution < hmcr:
                j = int(uniform_distribution*hms)+1
                new_soln[i] = hm[j, i]
                if uniform_distribution < par:
                    delta = (np.random.random_sample()*2 - 1) * bw
                    new_soln[i] = new_soln[i] + delta
            else:
                new_soln[i] = lower_bound + np.random.random_sample()*(upper_bound-lower_bound)#edit
        hm2[iterator]=new_soln

    function_value2 = np.zeros((hms, M))
    for i in range(hms):
        function_value2[i] = DTLZ2(hm2[i], question_no)#define the function
    

    hmu=np.zeros((2*hms, no_of_var))
    hmu[:hms]=hm
    hmu[hms:]=hm2
    
    function_value_union = np.zeros((2*hms, M))
    function_value_union[:hms] = function_value
    function_value_union[hms:] = function_value2

    rank_union = non_dominated_sorting(function_value_union)
    cd = crowding_distance(function_value_union)

    sorted_indices = np.lexsort((cd, rank_union))
    hm = hmu[sorted_indices[:hms]]
    function_value = function_value_union[sorted_indices[:hms]]
    rank = rank_union[sorted_indices[:hms]]
    mi=mi-1
print(rank)

#plt.plot(hm[:,0], hm[:, 1],'ro')
plt.show()

a=[]
for i in range(hms):
    if(rank[i]==1):
        a.append(hm[i])
plt.plot(hm[:,1],hm[:,0],'bo')
plt.show()
a=np.array(a)
plt.plot(a[:,0],a[:,1],'ro')
plt.show()
hv=hypervolume(hm)
h=hv.compute(r)
k.append(h)
print(k)
print(hm)
plt.plot(function_value[:,0],function_value[:,1], 'ro')
plt.show()
