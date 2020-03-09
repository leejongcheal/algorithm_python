import sys
t = int(input())
res = []
name = [list(i.split()) for i in sys.stdin.read().splitlines()]
for idx in range(t):
    res.append(" ".join(name[idx][2:]+name[idx][0:2]))
print("\n".join(res))
