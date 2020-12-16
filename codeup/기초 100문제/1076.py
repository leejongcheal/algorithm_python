import sys
a = sys.stdin.readline().rstrip()
L = []
for i in range(ord("a"), ord(a)+1):
    L.append(chr(i))
print(" ".join(L))