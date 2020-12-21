import sys
n = int(sys.stdin.readline().rstrip())
L = list(sys.stdin.readline().rstrip().split())
print(" ".join(reversed(L)))