import sys
n = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))
rL = []
for i in range(23):
    rL.append(str(L.count(i+1)))
print(" ".join(rL))