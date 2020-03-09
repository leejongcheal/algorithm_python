import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for i in range(t):
    a,b,c = map(int,name[i].split())
    if a == b - c:
        res.append("does not matter")
    elif a > b - c:
        res.append("do not advertise")
    else:
        res.append("advertise")
print("\n".join(res))
