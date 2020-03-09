import sys
L = sys.stdin.readlines()
print(L)
S = []
for i in range(len(L)):
    S += L[i].split()
res = ""
max = 0
for i in S:
    if i == "E-N-D":
        break
    a = 0
    char = ""
    for c in i:
        if "a" <= c <= "z" or "A" <= c <= "Z" or c == "-":
            a += 1
        else:
            char += c
    if max < a:
        idx = 0
        while idx < len(char):
            i = i.replace(char[idx],"")
            idx += 1
        res = i
        max = a
print(res)
