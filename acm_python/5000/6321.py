import sys
n = int(input())
name = sys.stdin.read().splitlines()
res =[]
for idx in range(n):
    r = ""
    for c in name[idx]:
        if c == "Z":
            r += "A"
        else:
            r += chr(ord(c)+1)
    if idx != n-1:
        res.append("String #{}\n{}\n".format(idx+1,r))
    else:
        res.append("String #{}\n{}".format(idx + 1, r))
print("\n".join(res))
