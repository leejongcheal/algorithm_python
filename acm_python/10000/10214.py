import sys
T = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(0,9*T,9):
    a = 0
    b = 0
    for i in range(9):
        c,d= map(int,name[idx+i].split())
        a += c
        b += d
    if a>b:
        res.append("Yonsei")
    elif a<b:
        res.append("Korea")
    else:
        res.append("Draw")
print("\n".join(res))
