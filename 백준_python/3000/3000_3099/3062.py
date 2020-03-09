import sys
def check(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return "NO"
    return "YES"


t = int(input())
L = []
name = sys.stdin.read().splitlines()
for i in range(t):
    s = int(name[i]) + int(name[i][::-1])
    L.append(check(str(s)))
print("\n".join(L))
