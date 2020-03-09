import sys
tele = "zaqxswcdevfrbgtnhymjukilop"
res = []
name = sys.stdin.read().splitlines()
for idx in range(len(name)-1):
    res.append("Y")
    for c in tele:
        if name[idx].count(c) == 0:
            res[-1] = "N"
print("\n".join(res))
