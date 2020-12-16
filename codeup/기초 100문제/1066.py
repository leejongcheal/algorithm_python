import sys
L = [("odd" if i%2 == 1 else "even") for i in map(int, sys.stdin.readline().rstrip().split())]
for i in L:
    print(i)