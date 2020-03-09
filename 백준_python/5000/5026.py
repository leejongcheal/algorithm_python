import sys
n = int(input())
name = sys.stdin.read().splitlines()
res = []
for i in range(n):
    L = name[i].split("+")
    if len(L) == 1:
        res.append("skipped")
    else:
        res.append(str(int(L[0])+int(L[1])))
print("\n".join(res))
