# чисто в теории должно простые задачи разваливать фри
# 27 - 10
from time import *
start = time()
point = []
for s in open('27-10'):
    x,y = map(float,s.replace(',','.').split())
    point.append((x,y))
point.sort()
from sys import *
setrecursionlimit(10000)
def f(x,y):
    ans = [(x,y)]
    global point
    point.remove((x,y))
    i = 0
    while i<len(point):
        x1 , y1 = point[i]
        if ((x1-x)**2+(y1-y)**2)**0.5<=0.3:
            ans += f(x1,y1)
        else:
            i+=1
    return ans
klaster = []
while len(point)>0:
    klaster.append(f(point[0][0],point[0][1]))
cc = []
for i in range(len(klaster)):
    cx,cy = min(klaster[i], key= lambda p: sum([ ((x1-p[0])**2+(y1-p[1])**2)**0.5 for x1,y1 in klaster[i]]))
    cc.append((cx,cy))
print(cc)
print(int(sum([x for x,y in cc])/len(cc)*10000) , int(sum([y for x,y in cc])/len(cc)*10000))
print(time()-start)
# 7881 -5340