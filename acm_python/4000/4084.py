import sys
def search_depth(s):
    depth = 0
    while not(s[0] == s[1] == s[2] == s[3]):
        next = [0]*4
        depth += 1
        next[0] = abs(s[0] - s[1])
        next[1] = abs(s[1] - s[2])
        next[2] = abs(s[2] - s[3])
        next[3] = abs(s[3] - s[0])
        s = next
    return depth


L = sys.stdin.read().splitlines()
res = []
for idx in range(len(L)-1):
    s = [int(i) for i in L[idx].split()]
    res.append(search_depth(s))
print("\n".join(map(str,res)))

