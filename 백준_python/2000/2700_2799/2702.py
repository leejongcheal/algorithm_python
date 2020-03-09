import math, sys

n = int(input())
name = sys.stdin.read().splitlines()
for idx in range(n):
    x, y = map(int, name[idx].split())
    print((x * y) // math.gcd(x, y), math.gcd(x, y))
