import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(t):
    L = list(name[idx].split())
    s = float(L[0])
    for i in range(1,len(L)):
        if L[i] == "@":
            s *= 3
        elif L[i] == "%":
            s += 5
        elif L[i] == "#":
            s -= 7
    res.append("%.2f"%(s))
print("\n".join(map(str,res)))
