def find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


N, M = map(int, input().split())
result = []
parent = [0]*(N+1)
edges = []
for i in range(1,N+1):
    parent[i] = i
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
# 크루스칼 알고리즘 시작
for cost, a, b in edges:
    # 사이클 발생
    if find(parent, a) == find(parent, b):
        continue
    union(parent, a, b)
    result.append(cost)
print(sum(result) - max(result))
