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
cals = []
total = 0
for l in data:
    if l == '\n':
        cals.append(total)
        total = 0
    else:
        cal = int(l.strip())
        total += cal

res = max(cals)
cals.sort()
res2 = sum([cals[-1],cals[-2],cals[-3]])

# Print #
print(res)
print(res2)