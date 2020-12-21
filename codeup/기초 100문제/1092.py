import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d = d + 1
print(d)