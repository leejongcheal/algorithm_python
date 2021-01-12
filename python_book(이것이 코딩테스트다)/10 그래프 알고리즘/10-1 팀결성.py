def parent_find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = parent_find(parent, parent[x])
    return parent[x]


def parent_union(parent, a, b):
    A = parent_find(parent, a)
    B = parent_find(parent, b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


N, M = map(int, input().split())
parent = [0]*(N+1)
result = []
for i in range(N+1):
    parent[i] = i
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        parent_union(parent, a, b)
    elif c == 1:
        if parent_find(parent, a) == parent_find(parent, b):
            result.append("YES")
        else:
            result.append("NO")
for r in result:
    print(r)