N = int(input())
n = 0
if N < 100:
    n = N
else:
    n = 99
    for i in range(100,N+1):
        a = i//100
        b = (i//10) % 10
        c = i % 10
        if a - b == b - c:
            n += 1
print(n)
