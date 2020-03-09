import sys
t = int(input())
name = sys.stdin.read().splitlines()
L = [[int(i) for i in name[idx].split() if int(i)%2 == 0] for idx in range(t)]
ans = ""
for i in range(t):
    ans +="{} {}\n".format(sum(L[i]),min(L[i]))
print(ans)