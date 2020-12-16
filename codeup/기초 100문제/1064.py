import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
ab = a if a < b else b
print( c if c < ab else ab)