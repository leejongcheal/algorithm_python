import sys
n = int(input())
res =[]
name = sys.stdin.read().splitlines()
for idx in range(n):
    L = (list(map(int,name[idx].split())))
    S = sorted(L[1:])
    m = 0
    for i in range(len(S)-1):
        m = max(S[i+1] - S[i],m)
    res.append("Class {}".format(idx+1))
    res.append("Max {}, Min {}, Largest gap {}".format(S[-1],S[0],m))
print("\n".join(res))

