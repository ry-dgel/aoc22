import numpy as np
import itertools as it

# Header #
test = False
numpy = False
if test:
    filename = "test.txt"
else:
    filename = "input.txt"

if numpy:
    data = np.genfromtxt(filename,delimiter=',')
else:
    with open(filename,'r') as f:
        data = list(f.readlines())

# Processs #
total = 0
total2 = 0



res = total
res2 = total2

# Print #
print(res)
print(res2)