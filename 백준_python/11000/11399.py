n = int(input())
L = sorted(list(int(i) for i in input().split()))
res=0
for i in range(n):
    res += (n-i)*L[i]
print(res)