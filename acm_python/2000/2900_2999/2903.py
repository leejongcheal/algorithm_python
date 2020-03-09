n = int(input())
res = [2,3]
for i in range(2,n+1):
    res.append(res[-1]*2 - 1)
print(res[-1]**2)

