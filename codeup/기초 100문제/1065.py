import sys
L = [i for i in map(int, sys.stdin.readline().rstrip().split()) if i%2 == 0]
for i in L:
    print(i)