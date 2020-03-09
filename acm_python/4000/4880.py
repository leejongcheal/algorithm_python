import sys
input = sys.stdin.readline
res = []
while 1:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    if a == b == c:
        res.append("GP {}".format(a))
    elif b - a == c - b:
        res.append("AP {}".format(c + b-a))
    else:
        res.append("GP {}".format(int(c*(b/a))))
print("\n".join(res))
