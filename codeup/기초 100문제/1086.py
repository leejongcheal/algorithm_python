import sys
w, h, b = map(int, sys.stdin.readline().rstrip().split())
print("%.2f MB"%((w*h*b)/2**23))