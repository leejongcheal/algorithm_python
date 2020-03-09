import sys
n = int(input())
L = [int(i) for i in sys.stdin.read().splitlines()]
v = [0]*1000001
m = 1
for r in L:
    if v[r] == 0:
        v[r] = 1
        S = L[:]
        idx = 0
        while L.count(r) > idx:
            idx += 1
            S.remove(r)
        cnt = 1
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                cnt += 1
            else:
                m = max(m,cnt)
                cnt = 1
        m = max(m,cnt)
print(m)

