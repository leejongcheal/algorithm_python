import sys

flag = 0
while (1):
    L = map(int, sys.stdin.readline().rstrip().split())
    for i in L:
        if i == 0:
            flag = 1
            break
        print(i)
    if flag == 1:
        break
