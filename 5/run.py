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
        stack,moves = ([l.strip('\n') for l in t.split('\n')] for t in list(f.read().split('\n\n')))

s = [[] for _ in range(len(stack[:-1][0][1::4]))]
for l in stack[:-1]:
    [s[i].insert(0,c) for i,c in enumerate(l[1::4]) if c != ' ']
s2 = [l.copy() for l in s]

for l in moves[:-1]:
    i,f,t = map(int,l.split(' ')[1::2])
    s[t-1] += [s[f-1].pop() for _ in range(i)]

for l in moves[:-1]:
    i,f,t = map(int,l.split(' ')[1::2])
    s2[t-1]+=s2[f-1][-i:]
    s2[f-1]=s2[f-1][:-i]

[print(x[-1],end='') for x in s]
print()
[print(x[-1],end='') for x in s2]

# # Processs #
# o = [''] * len(d.keys())
# for i,l in d.items():
#     o[i-1] = l[0]
# print(''.join(o))

# o = [''] * len(d2.keys())
# for i,l in d2.items():
#     o[i-1] = l[0]
# print(''.join(o))

