import sys

L = []
for _ in range(19):
    L.append(list(sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(19):
        if L[a-1][i] == "0":
            L[a-1][i] = "1"
        else:
            L[a-1][i] = "0"
        if L[i][b-1] == "0":
            L[i][b-1] = "1"
        else:
            L[i][b-1] = "0"
for i in range(19):
    print(" ".join(L[i]))