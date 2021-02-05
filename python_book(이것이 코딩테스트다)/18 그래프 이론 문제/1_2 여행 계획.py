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
    if Y < X:
        parent[X] = Y
    else:
        parent[Y] = X


N, M = map(int, input().split())
parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i
for i in range(N):
    L = list(map(int, input().split()))
    for j in range(N):
        if L[j] == 1:
            union(i+1, j+1)
move = list(map(int, input().split()))
flag = 0
for j in range(len(move)- 1):
    x = find_parent(move[j])
    y = find_parent(move[j+1])
    if x != y:
        flag = 1
        break
if flag == 1:
    print("NO")
else:
    print("YES")
