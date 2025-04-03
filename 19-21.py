from functools import lru_cache
from types import NoneType


#145
# from functools import *
# @lru_cache(None)
# def f(x):
#     if x>=132: return 0
#     m = [f(x+3),f(x+6),f(x*3)]
#     if 0 in m: return 1
#     if min(m)<0 : return -max([y for y in m if y<0])+1
#     return -max(m)
# n19 =min([s for s in range(1,132) if f(s)==-1])
# print(n19)
# n20 = [s for s in range(1,132) if f(s)==2][:2]
# print(n20)
# n21 = min([s for s in range(1,132) if f(s)==-2])
# print(n21)


# # kompege 6802
# from functools import lru_cache
# # from sys import setrecursionlimit
# @lru_cache(None)
# def f(x):
#     x = list(x)
#     if sum(x)>=97 : return 0
#     m = []
#     for i in range(len(x)):
#         for y in (1,3,5,7,8,12):
#             m.append(f(tuple(x[:i]+[x[i]+y]+x[i+1:])))
#     if 0 in m: return 1
#     if min(m)<0: return -max([z for z in m if z<0])+1
#     return -max(m)
# t=0
# for s in range(1,20):
#     for m in range(2,21):
#         if f(tuple([m*k for k in range(1,s+1)])) == -1:
#             t=1
#             print(s)
#             break
#     if t == 1: break
#
# t=0
# for s in range(20,0,-1):
#     for m in range(2,21):
#         if f(tuple([m*k for k in range(1,s+1)])) == 1:
#             t=1
#             print(s)
#             break
#     if t == 1: break
#
# sp = []
# for s in range(20,1,-1):
#     for m in range(20,1,-1):
#         if f(tuple([m*k for k in range(1,s+1)])) == 2:
#             print(s)
#             break
# # print(max(sp), min(sp))

# # normal version
# @lru_cache(None)
# def f(x):
#     if x>=97: return 0
#     m = [f(x+y) for y in (1,3,5,7,8,12)]
#     if 0 in m: return 1
#     if min(m)<0: return -max([z for z in m if z<0])+1
#     return -max(m)
# t = 0
# for s in range(1,100):
#     for m in range(2,21):
#         if f(sum([m*k for k in range(1,s+1)]))==-1:
#             print(s)
#             t=1
#             break
#     if t ==1 :
#         break
# t = 0
# for s in range(100,1,-1):
#     for m in range(2,21):
#         if f(sum([m*k for k in range(1,s+1)]))==1:
#             print(s)
#             t=1
#             break
#     if t ==1 :
#         break
# sp = []
# for s in range(1,100):
#     for m in range(2,21):
#         if f(sum([m*k for k in range(1,s+1)]))==2:
#             sp.append(s)
#             break
# print(max(sp), min(sp))






