import sys

input = sys.stdin.read().splitlines()
res = []
idx = 0
while True:
    try:
        a = input[idx]
        idx += 1
        N, B, M = map(float, a.split())
        n = 0
        while N < M:
            n += 1
            N = N*(1+B*0.01)
        res.append(n)
    except:
        break
print("\n".join(map(str,res)))
