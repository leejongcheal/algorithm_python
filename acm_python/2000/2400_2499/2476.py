import sys


def f(x, y, z):
    if x == y and y == z:
        return 10000 + x * 1000
    elif x == y or y == z:
        return 1000 + y * 100
    elif x == z:
        return 1000 * z * 100
    else:
        return 100 * z


r = sys.stdin.readline
N = int(r())
m = 0
for _ in range(N):
    x, y, z = sorted(map(int, r().split()))
    temp = f(x, y, z)
    m = max(m, temp)
print(m)
