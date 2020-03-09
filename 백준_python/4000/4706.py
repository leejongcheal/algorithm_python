import sys, math
name = sys.stdin.read().splitlines()
idx = 0
res = []
while True:
    a, b = map(float, name[idx].split())
    if a == b == 0:
        break
    idx += 1
    s = 1 - (b / a)**2
    res.append("%.3f" % (math.sqrt(s)))
print("\n".join(res))
