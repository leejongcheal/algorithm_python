import sys
t = int(input())
name = sys.stdin.read().splitlines()
res =[]
for i in range(0,t*2,2):
    n = int(name[i])
    L = list(map(int,name[i+1].split()))
    a = 1
    while sum(L) <= n:
        a += 1
        next = [0]*6
        for idx in range(6):
            next[idx] = L[(idx+3)%6] + L[(idx+1)%6] + L[(idx-1)%6] + L[idx]
        L = next[:]
    res.append(a)
print("\n".join(map(str,res)))
