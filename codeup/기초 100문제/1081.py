import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i, j)