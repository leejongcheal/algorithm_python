N, M = map(int, input().split())
L = list(map(int,input().split()))
cnt = [0]*(M+1)
for i in L:
    cnt[i] += 1
mult_cnt = len(L)
res = 0
for i in range(1,M+1):
    if cnt[i] != 0:
        mult_cnt -= cnt[i]
        res += mult_cnt*cnt[i]
print(res)