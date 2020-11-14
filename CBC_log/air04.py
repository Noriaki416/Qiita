from mip import *
m = Model("air04")
m.read("air04.mps")
m.verbose = 1
status = m.optimize()
print(status)