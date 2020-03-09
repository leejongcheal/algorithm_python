import sys
n,m = map(int,input().split())
L = sys.stdin.read().splitlines()
v = [int(i) for i in range(n)]
r=0
for i in range(m):
    x,y = map(int,L[i].split())
    x,y=x-1,y-1
    if v[x] != v[y]:
        temp = v[y]
        for j in range(n):
            if v[j] == temp:
                v[j] = v[x]
for i in range(n):
    if v[i] == i:
        r += 1
print(r)