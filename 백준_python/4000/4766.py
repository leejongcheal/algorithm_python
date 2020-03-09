import sys
input = list(map(float,sys.stdin.read().splitlines()))
idx = 1
res = []
while 1:
    if input[idx] == 999:
        break
    res.append("%.2f"%(input[idx] - input[idx-1]))
    idx += 1
print("\n".join(res))
