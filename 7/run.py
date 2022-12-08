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
        data = [l.strip() for l in f.readlines()]

files = {}
for l in data:
    cmd = l[:4]
    if cmd == "$ cd":
        newd = l[5:]
        if newd == "..":
            files = files[".."]
        elif newd == "/":
            while ".." in files.keys():
                files = files[".."]
        else:
            files = files[newd]
    elif cmd == "$ ls":
        pass
    else:
        f = l.split(" ")
        if f[0] == "dir":
            files[f[1]] = {'..':files}
        else:
            files[f[1]] = int(f[0])

while ".." in files.keys():
    files = files[".."]

# Part 1
def count(files,bigs = None):
    if bigs is None:
        bigs = []
    total = 0

    for key,item in files.items():
        if key != "..":
            if type(item) == int:
                total += item
            else:
                newt, bigs = count(item,bigs)
                total += newt

    if total < 100000:
        bigs.append(total)
    return total,bigs

total, bigs = count(files)
print(sum(bigs))

# Part 2
def findsize(name,files,size=0,sizes = None):
    if sizes is None:
        sizes = []
    total = 0

    for key,item in files.items():
        if key != "..":
            if type(item) == int:
                total += item
            else:
                newt, sizes = findsize(key,item,size,sizes)
                total += newt

    if total >= size:
        sizes.append(total)
    return total,sizes

goal = 30000000 - (70000000 - total)
total,sizes = findsize("/",files,size=goal)
print(sorted(sizes)[0])

