N = int(input())
L = list(map(int, input().split()))
S = list(set(L))
S.sort()
cnt = 0
remain = 0
for i in S:
    c = L.count(i)
    cnt += (c + remain) // i
    remain = (c + remain) % i
print(cnt)
