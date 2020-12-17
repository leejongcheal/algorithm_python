import sys

L = [("X" if i % 3 == 0 else str(i)) for i in range(1, int(sys.stdin.readline().rstrip()) + 1)]
print(" ".join(L))