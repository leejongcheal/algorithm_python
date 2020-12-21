import sys
a, r, n = map(int, sys.stdin.readline().rstrip().split())
print(a*(r**(n-1)))