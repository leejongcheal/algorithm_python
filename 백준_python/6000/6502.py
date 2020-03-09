import sys
name = sys.stdin.read().splitlines()
res =[]
for idx in range(len(name)-1):
    c,a,b = map(int,name[idx].split())
    if c**2 >= (a/2)**2 + (b/2)**2:
        res.append("Pizza {} fits on the table.".format(idx+1))
    else:
        res.append("Pizza {} does not fit on the table.".format(idx+1))
print("\n".join(res))
