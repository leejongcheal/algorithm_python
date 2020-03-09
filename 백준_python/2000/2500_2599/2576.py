import sys
input = sys.stdin.read().splitlines()
L = [int(i) for i in input if int(i) % 2 == 1]
if not L:
    print(-1)
else:
    print(sum(L))
    print(min(L))
