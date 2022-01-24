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


N = int(input())
parent = [0]*N
X = []
Y = []
Z = []
for i in range(N):
    parent[i] = i
    x, y, z = map(int, input().split())
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))
X.sort()
Y.sort()
Z.sort()
edges = []
for i in range(N-1):
    x1, i1 = X[i]
    x2, i2 = X[i+1]
    xd = abs(x1 - x2)
    edges.append((xd,i1,i2))
    y1, i1 = Y[i]
    y2, i2 = Y[i + 1]
    yd = abs(y1 - y2)
    edges.append((yd, i1, i2))
    z1, i1 = Z[i]
    z2, i2 = Z[i + 1]
    zd = abs(z1 - z2)
    edges.append((zd, i1, i2))
edges.sort()
result = 0
for edge in edges:
    d, x, y = edge
    if find_parent(x) != find_parent(y):
        union(x,y)
        result += d
print(result)