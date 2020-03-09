import sys
n = int(input())
L = [[0]*(n+1) for _ in range(n+1)]
v = [[0]*(n+1) for _ in range(n+1)]
x, y = map(int, input().split())
m = int(input())
nameList = sys.stdin.read().splitlines()
for idx in range(m):
    i, j = map(int,nameList[idx].split())
    L[i][j] = 1
    L[j][i] = 1
q = [x]
while q:
    start = q.pop(0)
    for i in range(1,n+1):
        if L[start][i] == 1 and v[start][i] == 0 and start != i:
            v[start][i] = 1
            v[i][start] = 1
            if v[i][i] == 0:
                v[i][i] = v[start][start] + 1
            q.append(i)
    if v[y][y] != 0:
        break
if x == y:
    print(0)
elif v[y][y] == 0:
    print(-1)
else:
    print(v[y][y])
