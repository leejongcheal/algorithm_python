n = int(input())
result = 0
for i in range(n+1):
    if i == 3 or i == 13 or i == 23:
        result += 3600
    else:
        result += 1575
print(result)