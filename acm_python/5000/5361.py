import sys
T = [350.34, 230.90, 190.55, 125.30, 180.90]
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(t):
    c = 0
    L = list(map(int,name[idx].split()))
    for i in range(5):
        c += L[i]*T[i]
    res.append("$%.2f"%c)
print("\n".join(res))
