import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
if a == 1 and b == 1:
    print(1)
else:
    print(0)