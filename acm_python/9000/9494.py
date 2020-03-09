import sys
input = sys.stdin.readline
res = []
while True:
    n = int(input())
    if n == 0:
        break
    r = 0
    for _ in range(n):
        L = input().rstrip()+" "
        if len(L)-1 <= r:
            continue
        r += L[r:].index(" ")
    res.append(str(r+1))
print("\n".join(res))

