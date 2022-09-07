# This example formulates and solves the following simple MIP model:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary

import gurobipy as gp
from gurobipy import GRB

try:

    # Create a new model
    m = gp.Model("hw1")

    # Create variables
    x1 = m.addVar(vtype=GRB.BINARY, name="x1")
    x2 = m.addVar(vtype=GRB.BINARY, name="x2")

    # Set objective
    m.setObjective(x1 + 0.64 * x2, GRB.MAXIMIZE)

    # Add constraint
    m.addConstr(50 * x1 + 31 * x2 <= 250, "c0")

    # Add constraint
    m.addConstr(3 * x1 - 2 * x2 >= -4, "c1")

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % m.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')