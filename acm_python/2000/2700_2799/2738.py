import sys
x,y = map(int,input().split())
name = sys.stdin.read().splitlines()
a = [list(map(int,name[idx].split())) for idx in range(2*x)]
L = [[a[i][j] + a[x+i][j] for j in range(y)] for i in range(x)]
for c in L:
    print(" ".join(str(x) for x in c))
