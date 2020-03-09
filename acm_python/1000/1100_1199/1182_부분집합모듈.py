import itertools

N,S = map(int,input().split())
L = list(map(int,input().split()))
result = 0
for i in range(1,N+1):
    A = itertools.combinations(L,i)
    for s in A:
        if sum(s) == S:
            result += 1
print(result)