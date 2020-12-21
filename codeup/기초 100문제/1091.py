import sys
a, m, d, n = map(int, sys.stdin.readline().rstrip().split())
for _ in range(n-1):
    a = a*m + d
print(a)