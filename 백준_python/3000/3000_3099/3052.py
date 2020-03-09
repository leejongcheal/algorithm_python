import sys
L = sys.stdin.read().splitlines()
a = set(int(i)%42 for i in L)
print(len(a))
