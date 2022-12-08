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
    data = np.genfromtxt(filename,delimiter='')
else:
    with open(filename,'r') as f:
        data = [l.strip() for l in f.readlines()][0]

print(next(i for i,_ in enumerate(data) if len(set(data[i:i+4]))==4)+4)
print(next(i for i,_ in enumerate(data) if len(set(data[i:i+14]))==14)+14)