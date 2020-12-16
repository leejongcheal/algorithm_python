import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
if b >= a:
    print(1)
else:
    print(0)