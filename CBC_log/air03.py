from mip import *
m = Model("air03")
m.read("air03.mps")
m.verbose = 1
status = m.optimize()
print(status)