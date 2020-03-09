import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(t):
    res.append(" ".join([i[::-1] for i in name[idx].split()]))
print("\n".join(res))
