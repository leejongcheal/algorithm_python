def find_parent(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    A = find_parent(parent, a)
    B = find_parent(parent, b)
    if A > B:
        parent[A] = B
    else:
        parent[B] = A


v, e = map(int, input().split())
# 초기화및 세팅
parent = [0]*(v+1)
edges = []
result = 0
for i in range(1,v+1):
    parent[i] = i
# 간선 정보 입력 받고 sort()
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
# 간선들에 대해서 사이클? 아니면 추가
for edge in edges:
    cost, a, b = edge
    # 사이클 생기는 경우 무시
    if find_parent(parent,a) == find_parent(parent, b):
        continue
    # 신장 트리에 추가
    union_parent(parent, a, b)
    result += cost
print(result)
