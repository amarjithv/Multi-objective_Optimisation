from pygmo import *
p=[[0.0, 0.5],[0.25, 0.25], [0.5, 0.0]]
hv=hypervolume(p)
r=[11,11]
h=hv.compute(r)
print(h)

from inspyred.ec.analysis import hypervolume as hpv
print(hpv(p,reference_point=r))

import numpy as np
from platypus import NSGAII, DTLZ2

# define the problem definition
problem = DTLZ2(2)

# instantiate the optimization algorithm
algorithm = NSGAII(problem)

# optimize the problem using 10,000 function evaluations
algorithm.run(10000)
# display the results
i=0
p=np.zeros((100,2))
for solution in algorithm.result:
    p[i]=np.array(solution.variables)
    i=i+1
print(i)
from pygmo import *
hv=hypervolume(p)
r=[11,11]
h=hv.compute(r)
print(h)
print(hpv(p,reference_point=r))

