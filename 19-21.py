#145
from functools import *
@lru_cache(None)
def f(x):
    if x>=132: return 0
    m = [f(x+3),f(x+6),f(x*3)]
    if 0 in m: return 1
    if min(m)<0 : return -max([y for y in m if y<0])+1
    return -max(m)
n19 =min([s for s in range(1,132) if f(s)==-1])
print(n19)
n20 = [s for s in range(1,132) if f(s)==2][:2]
print(n20)
n21 = min([s for s in range(1,132) if f(s)==-2])
print(n21)
