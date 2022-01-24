def find_parent(x):
    global parent
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x,y):
    global parent
    X = find_parent(x)
    Y = find_parent(y)
    if X < Y:
        parent[Y] = X
    else:
        parent[X] = Y

N, M = map(int, input().split())
all_cost = 0
min_cost = 0
parent = [0]*(N)
for i in range(N):
    parent[i] = i
L = []
for i in range(M):
    a, b, c = map(int, input().split())
    L.append((c,a,b))
    all_cost += c
L.sort()
# 정렬후 크루스칼 알고리즘 실행
for l in L:
    c, a, b = l
    if find_parent(a) != find_parent(b):
        union(a,b)
        min_cost += c
print(all_cost - min_cost)



