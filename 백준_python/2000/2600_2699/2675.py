import sys
t = int(input())
name = sys.stdin.read().splitlines()
L = [name[idx].split() for idx in range(t)]
ans = ""
for i in range(t):
    for c in L[i][1]:
        ans += int(L[i][0])*c
    ans += "\n"
print(ans)
