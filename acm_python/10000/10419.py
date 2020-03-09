import sys
t = int(input())
L = [int(i) for i in sys.stdin.read().splitlines()]
res = []
for idx in range(t):
    for i in range(L[idx]+2):
        if i+i**2>L[idx]:
            break
    res.append(str(i-1))
print("\n".join(res))
