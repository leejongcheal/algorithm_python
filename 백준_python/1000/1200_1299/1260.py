import sys
from collections import deque
sys.setrecursionlimit(10**8)
V = {}
V1 = {}
L = {}
N,M,start = map(int,input().split())
for i in range(M):
    a = list(map(int,input().split()))
    V[a[0]] = V.get(a[0],0)
    V[a[1]] = V.get(a[1],0)
    if L.get(a[0]) is None:
        L[a[0]] = []
    if L.get(a[1]) is None:
        L[a[1]] = []
    L[a[0]].append(a[1])
    L[a[1]].append(a[0])
V1 = V.copy()
for l in L.keys():
    L[l].sort()
result = []
 #  DFS실행


def DFS(index):
    global L
    global V
    if V[index] == 1:
        return
    V[index] = 1
    result.append(index)
    for a in L.get(index,[]):
        DFS(a)


DFS(start)
for a in result:
    print("%d"%a,end=" ")
print()
 # BFS실행
result = []
queue = deque()
queue.append(start)
while(queue):
    idx = queue.popleft()
    if V1[idx] == 1:
        continue
    V1[idx] = 1
    result.append(idx)
    for i in L.get(idx,[]):
            queue.append(i)
for a in result:
    print("%d"%a,end=" ")
print()
