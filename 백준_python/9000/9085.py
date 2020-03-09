import sys
t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(0,2*t,2):
    res.append(sum(list(map(int,name[idx+1].split()))))
print("\n".join(map(str,res)))