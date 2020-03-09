import sys
n = int(input())
m = int(input())
L = [[0] * (n + 1) for _ in range(n + 1)]
nameList = sys.stdin.read().splitlines()
for i in range(m):
    x, y = map(int, nameList[i].split())
    L[x][y] = 1
    L[y][x] = 1
q = [1]
res = [1]
while q:
    start = q.pop(0)
    for i in range(1, n+1):
        if L[start][i] == 1 and i not in res:
            q.append(i)
            res.append(i)
print(len(res)-1)
