from functools import *
from math import *
from re import *
def tobase(x,n):
    if x == 0: return [0]
    sp = []
    x = abs(x)
    while x>0:
        sp.append(x%n)
        x//=n
    return sp[::-1]
def divisors(x):
    sp = [1,x]
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            sp.append(i)
            if i!=x//i:
                sp.append(x//i)
    return sorted(sp)
def digits(x):
    return [int(y) for y in str(x)]
def digitstoint(x, n):
    return sum([x[::-1][i]*n**i for i in range(len(x))])
def eachcount(x):
    return {y:x.count(y) for y in set(x)}











