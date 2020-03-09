import sys
sys.setrecursionlimit(10**8)


def check(l):
    global V
    global L
    global M
    global N
    if l in V:
        return -1
    if l[0] <= 0 or l[0] > N:
        return -1
    if l[1] <= 0 or l[1] > M:
        return -1
    if l in L:
        return 1
    else:
        return -1


def dfs(l,idx):
    global V
    global L
    # 상하좌우 순서
    idx += 1
    V.append(l)
    if check([l[0]+1,l[1]]) == 1:
        idx += dfs([l[0]+1,l[1]],0)
    if check([l[0]-1,l[1]]) == 1:
        idx += dfs([l[0] - 1, l[1]],0)
    if check([l[0],l[1]-1]) == 1:
        idx += dfs([l[0], l[1]-1],0)
    if check([l[0],l[1]+1]) == 1:
        idx += dfs([l[0],l[1]+1],0)
    return idx


N,M,K = map(int,input().split())
L = []
V = []
result = []
for i in range(K):
    L.append(list(map(int,input().split())))
for i in L:
    if check(i) == 1:
        result.append(dfs(i,0))
# print(result)
print(max(result))

