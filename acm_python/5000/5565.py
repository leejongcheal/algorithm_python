import sys
L = [int(i) for i in sys.stdin.read().splitlines()]
print(L[0] - sum(L[1:]))
