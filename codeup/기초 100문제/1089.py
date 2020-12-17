import sys

s, d, n = map(int, sys.stdin.readline().rstrip().split())
print(s+d*(n-1))