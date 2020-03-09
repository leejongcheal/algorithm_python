import sys
limit = 100001
l = [0,1]+ [0]*limit
for i in range(1,limit):
    q =[]
    x = i
    m = 1
    while True:
        q +=[x]
        if x < limit and l[x] > 0:
            m = l[x]
            break
        else:
            if x%2 == 0:
                x = x//2
            else:
                x = 3*x + 1
    for i in reversed(q):
        m = max(i,m)
        if i<limit:
            l[i] = m
res = []
t = int(input())
name = sys.stdin.read().splitlines()
for idx in range(t):
    res.append(l[int(name[idx])])
print("\n".join(map(str,res)))