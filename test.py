# HomeWork1 Question 1.1
# Created by Dong Han
# Solving a integer program by using Python interface to Gurobi 


import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model("hw1")

# Create variables
x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=GRB.INTEGER, name="x2")

# Set objective
m.setObjective(x1 + 0.64 * x2, GRB.MAXIMIZE)

# Add constraint 1
m.addConstr(50 * x1 + 31 * x2 <= 250, "c1")

# Add constraint 2
m.addConstr(3 * x1 - 2 * x2 >= -4, "c2")

# Add constraints 3
m.addConstr(x1 >= 0, "c3")

# Add constraints 4
m.addConstr(x2 >= 0, "c4")

# Optimize model
m.optimize()

for val in m.getVars():
    print('%s %g' % (val.VarName, val.X))

print('Obj: %g' % m.ObjVal)