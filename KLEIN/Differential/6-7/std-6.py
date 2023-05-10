from gurobipy import *

import math 

env = Env("std-6.log")
filename = 'std_diff_klein6.lp'
m = read(filename,env)  
obj = m.getObjective()
m.Params.timeLimit = 100000.0
m.optimize()
time = int(m.Runtime)
time = math.floor(time)
textfile = 'std-6.txt'
file = open(textfile,'w+')
file.write(str(time) + " seconds \n")
for v in m.getVars():
    if v.x == 1:
        print(v)
        file.write(str(v) + "\n")
file.close()