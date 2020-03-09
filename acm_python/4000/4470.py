import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(t):
    res.append("{}. ".format(idx+1)+name[idx])
print("\n".join(res))
