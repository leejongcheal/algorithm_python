import math
N = int(input())
L = list(map(int, input().split()))
res = 0

for num in L:
    for j in range(2, int(math.sqrt(num))+2):
        if num % j == 0:
            break
    if num != 1 and j == int(math.sqrt(num))+1:
        res += 1
print(res)
