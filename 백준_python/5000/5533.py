import sys
t = int(input())
name = sys.stdin.read().splitlines()
L = []
for i in range(t):
    L += name[i].split()
res = []
for i in range(0, 3 * t, 3):
    score = 0
    for j in range(3):
        c = 0
        for idx in range(j,len(L),3):
            if L[idx] == L[i+j]:
                c += 1
        if c == 1:
            score += int(L[i+j])
    res.append(score)
print(" ".join(map(str, res)))
