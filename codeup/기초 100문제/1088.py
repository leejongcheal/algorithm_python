import sys
a = int(sys.stdin.readline().rstrip())
L = []
for i in range(1, a+1):
    if i % 3 != 0:
        L.append(str(i))
print(" ".join(L))