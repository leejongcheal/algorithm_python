import sys
h, b, c, s = map(int, sys.stdin.readline().rstrip().split())
print("%.1f MB"%((h*b*c*s)/2**23))