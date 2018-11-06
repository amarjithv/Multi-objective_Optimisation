#!/usr/bin/env python3
import numpy as np
import scipy as scp
import enum
from pygmo import *
import matplotlib.pyplot as plt
from pareto import non_dominated_sorting
from problem import DTLZ2
from pareto import find_rank


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

def find_worst(ranks, crowd_d):
    worst = 0
    for i in range(ranks.shape[0]):
        if ranks[i] > ranks[worst]:
            worst = i
        elif ranks[i]==ranks[worst]:
            if crowd_d[i]>crowd_d[worst]:
                worst = i
    return worst

def improvise_solution(memory):
    new_solution = np.zeros(no_of_var)
    for i in range(no_of_var):

        uniform_distribution = np.random.random_sample()
        if uniform_distribution < hmcr:
            j = int(uniform_distribution*memory.shape[0])+1
            new_solution[i] = memory[j, i]
            if uniform_distribution < par:
                delta = (np.random.random_sample()*2 - 1) * bw
                new_solution[i] = new_solution[i] + delta
        else:
            new_solution[i] = lower_bound + np.random.random_sample()*(upper_bound-lower_bound)#edit
    return new_solution


def harmonic_search2():    
    #Memory Initialization
    hm = np.random.rand(hms, no_of_var)*(upper_bound1-lower_bound1)+lower_bound1
    new_soln = np.zeros(no_of_var)
    function_value = np.zeros((hms, M))
    
    for i in range(hms):
        function_value[i] = DTLZ2(hm[i], question_no)#define the function
    
    rank = non_dominated_sorting(function_value)
    
    for iterator in range(mi):
        
        rank = non_dominated_sorting(function_value)
        hm2=np.zeros((hms, no_of_var))
    
        for i in range(hm.shape[0]):
           hm2[i]=improvise_solution(hm)
    
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
    return hm, function_value

def harmonic_search_1():
    #Memory Initialization
    hm = np.random.rand(hms, no_of_var)*(upper_bound1-lower_bound1)+lower_bound1
    function_value = np.zeros((hms, M))
    
    #hm[5] = [0, 0]
    
    for i in range(hms):
        function_value[i] = DTLZ2(hm[i], question_no)#define the function
    
    rank = non_dominated_sorting(function_value)
    for iterator in range(mi):
        rank = non_dominated_sorting(function_value)
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
        cd = crowding_distance(function_value) 
        worst_soln_index = find_worst(rank, cd)
        new_sol_fval = DTLZ2(new_soln, question_no)
        new_sol_rank = find_rank(function_value, new_sol_fval)
        if new_sol_rank < rank[worst_soln_index]:
            hm[worst_soln_index] = new_soln
            function_value[worst_soln_index] = new_sol_fval
    return hm, function_value
