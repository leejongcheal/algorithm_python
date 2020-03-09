import sys
input = sys.stdin.readline
res = []
while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    if a%b == 0 :
        res.append("multiple")
    elif b%a == 0:
        res.append("factor")
    else:
        res.append("neither")
print("\n".join(res))
