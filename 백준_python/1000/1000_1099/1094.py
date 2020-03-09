n = int(input())
r = 0
for i in range(8,-1,-1):
    if n >= 2**i:
        n -= 2**i
        r += 1
    if n == 0:
        break
print(r)
