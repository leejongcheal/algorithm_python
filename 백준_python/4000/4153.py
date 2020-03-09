import sys
res = []
while 1:
    L = sorted(list(map(int,sys.stdin.readline().split())))
    if L[0] == L[1] == L[2] == 0:
        break
    if L[0]**2 + L[1]**2 == L[2]**2:
        res.append("right")
    else:
        res.append("wrong")
print("\n".join(res))
