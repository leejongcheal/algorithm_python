import sys
n = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(n):
    r = 0
    a = 0
    for c in name[idx]:
        if c == "O":
            a += 1
            r += a
        else:
            a = 0
    res.append(str(r))
print("\n".join(res))