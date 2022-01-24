def find_parent(x):
    global parent
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    global parent
    X = find_parent(x)
    Y = find_parent(y)
    if X < Y:
        parent[Y] = X
    else:
        parent[X] = Y


N = int(input())
P = int(input())
parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i
result = 0
for i in range(P):
    g = int(input())
    G = find_parent(g)
    if G == 0:
        break
    union(g, G-1)
    result += 1
print(result)