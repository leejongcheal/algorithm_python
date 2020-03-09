import sys
dic = {}
t = int(input())
L = list(map(int,sys.stdin.read().splitlines()))
res = []
for i in range(1,46):
    dic[i] = (i*(i+1))//2
for idx in range(t):
    for i in range(1,46):
        if dic[i] > L[idx]:
            break
    n = i
    r = 0
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                if dic[a]+dic[b]+dic[c] == L[idx]:
                    r = 1
                    break
            if r == 1:
                break
        if r == 1:
            break
    if r == 1:
        res.append("1")
    else:
        res.append("0")
print("\n".join(res))