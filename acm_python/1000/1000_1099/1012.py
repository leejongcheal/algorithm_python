import sys
sys.setrecursionlimit(10**8)
V = []
m, n = 0,0
k = 0
L = []


def check(c):
    global L
    global V
    if c in L:
        if c not in V:
            return c
        else:
            return []
    else:
        return []


def DFS(l):
    global k
    global V
    V.append(l)
    k -= 1
    # print(l, V, k)
    #상하좌우
    if check([l[0], l[1] + 1]):
        DFS([l[0], l[1] + 1])
    if check([l[0], l[1] - 1]):
        DFS([l[0], l[1]-1])
    if check([l[0] - 1, l[1]]):
        DFS([l[0] - 1,l[1]])
    if check([l[0] + 1, l[1]]):
        DFS([l[0] + 1,l[1]])


y = []
t = int(input())
for q in range(t):
    m, n, k = map(int,input().split())
    # print(m,n,k)
    L = []
    V = []
    for w in range(k):
        L.append(list(map(int,input().split())))
    for l in L:
        if check(l):
            k += 1
            DFS(l)
    y.append(k)
for c in y:
    print(c)
