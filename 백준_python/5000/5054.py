import sys

t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(0, 2 * t, 2):
    n = int(name[idx])
    L = sorted(list(map(int, name[idx + 1].split())))
    mi = L[0]
    ma = L[-1]
    if n == 1:
        res.append(0)
    else:
        a = []
        for i in range(mi,ma+1):
           a.append((i - mi)*2 + (ma - i)*2)
        res.append(min(a))
print("\n".join(map(str,res)))

