import sys
t = int(input())
name = sys.stdin.read().splitlines()
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = []
for i in range(t):
    res = 0
    for c in s:
        if name[i].find(c) == -1:
            res += ord(c)
    L.append(res)
print("\n".join(map(str,L)))
