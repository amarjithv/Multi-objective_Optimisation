#!/usr/bin/env python3
import numpy as np
import scipy as scp
import enum
from pareto import non_dominated_sorting
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

    
#Ennumerate
class Objectives(enum.Enum):
    maximize = 1
    minimize = 0

#problem_statement
upper_bound = 10
lower_bound = -10
question_no = 1 

#Parameter configuration
hmcr = 0.8
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

#hm[5] = [0, 0]

for i in range(hms):
    function_value[i] = obj_function(hm[i], question_no)#define the function


while(mi>0):
    for i in range(no_of_var):

        uniform_distribution = np.random.random_sample()
        print(uniform_distribution)
        if uniform_distribution < hmcr:
            j = int(uniform_distribution*hms)+1
            print(j)
            new_soln[i] = hm[j, i]
            if uniform_distribution < par:
                delta = (np.random.random_sample()*2 - 1) * bw
                new_soln[i] = new_soln[i] + delta
        else:
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