import sys
n,k= map(int,input().split())
L = sys.stdin.read().splitlines()
r = []
s = ""
for i in range(n):
    if int(L[i][0]) == k:
        s = L[i][2:]
    r.append(L[i][2:])
r.sort(reverse=True)
print(r.index(s)+1)
