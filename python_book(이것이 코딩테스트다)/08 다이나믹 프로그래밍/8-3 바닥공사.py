n = int(input())
result = []
result.append(1)
result.append(3)
if n < 3:
    print(result[n-1])
else:
    for i in range(2,n):
        result.append(result[i-1] + 2 * result[i-2])
    print(result[n-1])
