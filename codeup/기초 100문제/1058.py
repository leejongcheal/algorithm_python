import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
if a == b == 0:
    print(1)
else:
    print(0)