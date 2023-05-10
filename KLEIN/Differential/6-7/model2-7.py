from gurobipy import *

import math 

env = Env("Model2_7.log")
filename = 'model2_diff_klein7.lp'
m = read(filename,env)  
obj = m.getObjective()
m.Params.timeLimit = 100000.0
m.optimize()
time = int(m.Runtime)
time = math.floor(time)
textfile = 'klein_model2-7.txt'
file = open(textfile,'w+')
file.write(str(time) + " seconds \n")
for v in m.getVars():
    if v.x == 1:
        print(v)
        file.write(str(v) + "\n")
file.close()