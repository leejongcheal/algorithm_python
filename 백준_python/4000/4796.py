import sys
input = sys.stdin.read().splitlines()
idx = 0
res = []
while 1:
    L,P,V = map(int,input[idx].split())
    if L == P == V == 0:
        break
    idx += 1
    r = L*(V//P)
    rest = V % P
    if rest < L:
        r += rest
    else:
        r += L
    res.append("Case {}: {}".format(idx,r))
print("\n".join(res))
