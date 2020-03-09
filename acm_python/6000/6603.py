from collections import deque
import sys
sys.setrecursionlimit(10**8)


def DFS(q,i):
    global L
    i += 1
    if len(q) == 6:
        print(" ".join(map(str,q)))
    elif i == len(L):
        return
    while i < len(L):
        DFS(q[:]+[L[i]], i)
        i += 1


name = sys.stdin.read().splitlines()
res = []
for idx in range(len(name)-1):
    L = list(map(int, name[idx].split()))
    n = L[0]
    L = L[1:]
    DFS([], -1)
    print()
