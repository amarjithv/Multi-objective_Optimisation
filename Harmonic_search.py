#!/usr/bin/env python3
import numpy as np
import scipy as scp
import enum
<<<<<<< HEAD

from problem import obj_function
def find_worst(funct, n):
    worst = 0
    for i in range(funct.shape[0]):
        if n==1:
            if funct[i] < funct[worst]:
                worst = i
        else:
            if funct[i] > funct[worst]:
                worst = i
    return worst


=======
from pareto import non_dominated_sorting
from problem import obj_function
from pareto import find_rank
def find_worst(ranks):
    worst = 0
    for i in range(ranks.shape[0]):
        if ranks[i] > ranks[worst]:
            worst = i
    return worst

    
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e
#Ennumerate
class Objectives(enum.Enum):
    maximize = 1
    minimize = 0

#problem_statement
<<<<<<< HEAD
upper_bound = 10
lower_bound = -10
=======
upper_bound = 10^3
lower_bound = -10^3
upper_bound1 = 10^3
lower_bound1 = -10^3
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e
question_no = 1 

#Parameter configuration
hmcr = 0.8
<<<<<<< HEAD
hms = 10000
mi = 10000
par = 0.3
bw = 2
no_of_var = 3
objective = 0

#Memory Initialization
hm = np.random.rand(hms, no_of_var)*(upper_bound-lower_bound)+lower_bound
new_soln = np.zeros(no_of_var)
function_value = np.zeros(hms)
=======
hms = 250
mi = 200
par = 0.3
bw = 2
no_of_var = 1
objective = 0
M = 2

#Memory Initialization
hm = np.random.rand(hms, no_of_var)*(upper_bound1-lower_bound1)+lower_bound1
#hm[5]=[11, 11]
new_soln = np.zeros(no_of_var)
function_value = np.zeros((hms, M))
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e

#hm[5] = [0, 0]

for i in range(hms):
<<<<<<< HEAD
    function_value[i] = obj_function(hm[i], question_no)#define the function


while(mi>0):
    for i in range(no_of_var):

        uniform_distribution = np.random.random_sample()
        print(uniform_distribution)
        if uniform_distribution < hmcr:
            j = int(uniform_distribution*hms)+1
            print(j)
=======
    function_value[i] = obj_function(hm[i], question_no).flatten()#define the function

rank = non_dominated_sorting(function_value)
print(rank)
import sys
#sys.exit()

while(mi>0):
    rank = non_dominated_sorting(function_value)
    for i in range(no_of_var):

        uniform_distribution = np.random.random_sample()
        if uniform_distribution < hmcr:
            j = int(uniform_distribution*hms)+1
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e
            new_soln[i] = hm[j, i]
            if uniform_distribution < par:
                delta = (np.random.random_sample()*2 - 1) * bw
                new_soln[i] = new_soln[i] + delta
        else:
<<<<<<< HEAD
            new_soln[i] = lower_bound + uniform_distribution*(upper_bound-lower_bound)#edit

    worst_soln_index = find_worst(function_value, 1)
    if objective == 1:
        if obj_function(new_soln, question_no) > function_value[worst_soln_index]:
            function_value[worst_soln_index] = obj_function(new_soln, question_no)
            hm[i] = new_soln
    else:
        if obj_function(new_soln, question_no) < function_value[worst_soln_index]:
            function_value[worst_soln_index] = obj_function(new_soln, question_no)
            hm[i] = new_soln
    
    mi = mi - 1

if objective == 1:
    soln_index = np.argmax(function_value, axis=0)
else:
    soln_index = np.argmin(function_value, axis=0)

solution = hm[soln_index]
print(solution)
=======
            new_soln[i] = lower_bound + np.random.random_sample()*(upper_bound-lower_bound)#edit

    worst_soln_index = find_worst(rank)
    new_sol_fval = obj_function(new_soln, question_no).flatten()
    new_sol_rank = find_rank(function_value, new_sol_fval)
    if new_sol_rank < rank[worst_soln_index]:
        hm[worst_soln_index] = new_soln
        function_value[worst_soln_index] = new_sol_fval
    mi = mi - 1

print(rank)
import matplotlib.pyplot as plt
plt.plot(hm[:,0], hm[:, 1],'ro')
plt.show()

a=[]
for i in range(hms):
    if(rank[i]==1):
        a.append(hm[i])
plt.plot(a,'ro')
plt.show()
>>>>>>> bf1ad5f52f92f74a6972de86bd004d8d26f3f36e
