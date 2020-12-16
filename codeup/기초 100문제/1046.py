import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
sum = a + b + c
print(sum)
print("%.1f"%(sum/3))