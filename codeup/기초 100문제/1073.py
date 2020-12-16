import sys

L = map(int, sys.stdin.readline().rstrip().split())
for i in L:
    if i == 0:
        break
    print(i)