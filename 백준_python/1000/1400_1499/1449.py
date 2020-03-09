N,L = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
result = 1
start = X[0]
for i in range(1,len(X)):
    if X[i] - start > L - 1:
        result += 1
        start = X[i]
print(result)
