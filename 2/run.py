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
out = []
total = 0
total2 = 0
dict1 = {'A':{'X':3+1,'Y':6+2,'Z':0+3},
         'B':{'X':0+1,'Y':3+2,'Z':6+3},
         'C':{'X':6+1,'Y':0+2,'Z':3+3}}
dict2 = {'A':{'X':0+3,'Y':3+1,'Z':6+2},
         'B':{'X':0+1,'Y':3+2,'Z':6+3},
         'C':{'X':0+2,'Y':3+3,'Z':6+1}}
for l in data:
    one = l.strip().split(' ')[0]
    two = l.strip().split(' ')[1]
    
    total += dict1[one][two]
    total2 += dict2[one][two]


res = total
res2 = total2

# Print #
print(res)
print(res2)