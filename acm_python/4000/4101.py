import sys
res = []
while 1:
    x,y = map(int,sys.stdin.readline().split())
    if x == y == 0:
        break
    if x <= y:
        res.append("No")
    else:
        res.append("Yes")
print("\n".join(res))
