import sys
name = sys.stdin.read().splitlines()
idx = 0
res = []
while 1:
    s = name[idx]
    if s == "#":
        break
    idx += 1
    n = s.count("1")
    if s[-1] =="e":
        if n%2 == 0:
            res.append(s[:-1]+"0")
        else:
            res.append(s[:-1] + "1")
    else:
        if n%2 == 0:
            res.append(s[:-1] + "1")
        else:
            res.append(s[:-1] + "0")
print("\n".join(res))
