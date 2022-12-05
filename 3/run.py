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

# Part 1
uniques = [set.intersection(*map(set,zip(*[iter(l.strip())]*(len(l)//2)))).pop() for l in data]
total = sum([x-38 if x < 97 else x - 96 for x in map(ord,uniques)])

# Part 2
uniques = [set.intersection(*map(lambda l:set(l.strip()),ls)).pop() for ls in zip(*[iter(data)]*3)]
total2 = sum([x-38 if x < 97 else x - 96 for x in map(ord,uniques)])

res = total
res2 = total2

# Print #
print(res)
print(res2)