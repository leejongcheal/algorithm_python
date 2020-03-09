import sys
input = sys.stdin.readline
while True:
    x = input()
    if x == "":
        break
    x = int(x)*10000000
    n = int(input())
    L = (list(int(input()) for _ in range(n)))
    L.sort()
    end = n - 1
    i = 0
    se = 0
    while i < end:
        if L[i]+L[end] == x:
            print("yes {} {}".format(L[i],L[end]))
            se = 1
            break
        elif L[i] + L[end] > x:
            end -= 1
        else:
            i += 1
    if se == 0:
        print('danger')
