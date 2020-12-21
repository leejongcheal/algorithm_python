import sys
n = int(sys.stdin.readline().rstrip())
L = [[0]*19 for _ in range(19)]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    L[a-1][b-1] = 1
for i in L:
    print(" ".join(list(map(str, i))))