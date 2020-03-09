import sys
n = int(input())
name = sys.stdin.read().splitlines()
L = [[int(i) for i in name[idx]] for idx in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if L[i][j] == 1:
            L[i][j] = 2
            q = [(i, j)]
            a = 1
            while q:
                x, y = q.pop(0)
                if x+1 < n and L[x+1][y] == 1:
                    a += 1
                    L[x+1][y] = 2
                    q.append((x+1,y))
                if x-1 >= 0 and L[x-1][y] == 1:
                    a += 1
                    L[x-1][y] = 2
                    q.append((x-1,y))
                if y+1 < n and L[x][y+1] == 1:
                    a += 1
                    L[x][y+1] = 2
                    q.append((x,y+1))
                if y-1 >= 0 and L[x][y-1] == 1:
                    a += 1
                    L[x][y-1] = 2
                    q.append((x,y-1))
            res.append(a)
print(len(res))
res.sort()
for i in res:
    print(i)
