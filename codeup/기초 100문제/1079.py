import sys

L = sys.stdin.readline().rstrip().split()
for i in L:
    print(i)
    if i == "q":
        break
