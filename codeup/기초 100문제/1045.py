import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print("%.2f"%(a / b))