import sys

n = int(input())
name = sys.stdin.read().splitlines()
L = []
for idx in range(n):
    x, y = map(int, name[idx].split())
    L.append([x, y, 0])
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            L[i][2] += 1
for i in range(n):
    print(L[i][2]+1,end=" ")
