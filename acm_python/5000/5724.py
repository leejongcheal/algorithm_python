import sys
res = []
name = sys.stdin.read().splitlines()
for idx in range(len(name)-1):
    a = 0
    for i in range(1,int(name[idx])+1):
        a += i**2
    res.append(a)
print("\n".join(map(str,res)))

