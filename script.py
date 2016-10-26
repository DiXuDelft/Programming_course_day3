import numpy
import numpy as np
def circumference(x):
    y = 2*np.pi*x
    return y

def area(x):
    y = np.pi*x**2
    return y
    
r = 2
print('The circumference is ', circumference(r))
print('The surface area is ', area(r))
