import sys
from collections import deque
sys.setrecursionlimit(10**8)
V = []
V1 = []
L = []
N,M,start = map(int,input().split())
for i in range(M):
    a = list(map(int,input().split()))
    L.append(a)
    L.append(a[::-1])
 #  DFS실행


def DFS(index):
    V.append(index)
    for i in L:
        if i[0] == index:
            if i[1] not in V:
                DFS(i[1])


DFS(start)
print(V)
# BFS실행
queue = deque()
queue.append(start)
while(queue):
    idx = queue.popleft()
    if idx not in V1:
        V1.append(idx)
    for i in L:
        if i[0] == idx:
            if i[1] not in V1:
                queue.append(i[1])
print(V1)
