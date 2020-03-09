import sys
res = []
n = int(input())
name = sys.stdin.read().splitlines()
for idx in range(n):
    i = len(name[idx])//2 - 1
    if name[idx][i] == name[idx][-1-i]:
        res.append("Do-it")
    else:
        res.append("Do-it-Not")
print("\n".join(res))
