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

for l in data:
    ass = l.strip().split(',')
    ass1 = set(range(int(ass[0].split('-')[0]),int(ass[0].split('-')[1])+1))
    ass2 = set(range(int(ass[1].split('-')[0]),int(ass[1].split('-')[1])+1))
    overlap = ass1.intersection(ass2)
    if ass1 == overlap or ass2 == overlap:
        total += 1
    if len(overlap) > 0:
        total2 += 1


res = total
res2 = total2

# Print #
print(res)
print(res2)