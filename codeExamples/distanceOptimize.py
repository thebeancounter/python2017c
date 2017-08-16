import numpy as np
import random
import time

t = [time.time()]

def takeTime():
    global t
    t.append(time.time())
    print t[-1]-t[-2]

def d(a,b):
    s = [(i-j)**2 for i,j in zip(a,b)]
    return sum(s)**0.5

takeTime()
a = [random.randint(1,200) for i in range(10000000)]
b = [random.randint(1,200) for i in range(10000000)]
takeTime()
print d(a,b)
takeTime()

a1 = np.array(a)
b1 = np.array(b)
takeTime()
print np.linalg.norm(a1 - b1)
takeTime()


exit()

"""
def pMatrix(matrix):
    for row in matrix:
        print row

a = [[1,2,3],[4,5,6],[7,8,9]]
b = zip(*a)

pMatrix(a)
print
pMatrix(b)

c = [list(row) for row in b]
print
pMatrix(c)

d = zip(*b[1:])

print
pMatrix(d)

"""