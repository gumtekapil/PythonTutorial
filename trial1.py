import cvxpy as cvx
from cvxpy import *
import numpy as np
a=[]
b=[]
# Create two scalar optimization variables.
for i in range(10):
   x = Variable()
   y = Variable()

# Create two constraints.
   constraints = [x + y == 1,
               x - y >= 1]

# Form objective.
   obj = Minimize(square((x - y)))

# Form and solve problem.
   prob = Problem(obj, constraints)
   prob.solve()  # Returns the optimal value.
   print "status:", prob.status
   print "optimal value", prob.value
   print "optimal var", x.value, y.value
   a[i]=x.value
   b[i]=y.value



