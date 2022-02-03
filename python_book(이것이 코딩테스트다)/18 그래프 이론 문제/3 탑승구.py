def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global parent
    X = find(x)
    Y = find(y)
    if X < Y:
        parent[Y] = X
    else:
        parent[X] = Y


G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
L = []
for _ in range(P):
    L.append(int(input()))
cnt = 0
for l in L:
    index = find(l)
    if index == 0:
        break
    else:
        union(index, index - 1)
        cnt += 1
print(cnt)