import sys
R = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
t = int(input())
L = []
for i in range(t):
    L.append(list(map(int,input().split())))
for l in L:
    a = l[0] % 10
    b = l[1] % len(R[a])
    if a == 0:
        print(10)
    else:
        if b == 0:
            print(R[a][-1])
        else:
            print(R[a][b-1])
