n = int(input())
L = list(map(int,input().split()))
res = [0]*(n+1)
for i in range(n):
    res[L[i]] = str(L[i] - (i+1))
print("\n".join(res[1:]))

