import sys
n = int(input())
name = sys.stdin.read().splitlines()
idx = 0
res = []
while True:
    a = int(name[idx])
    if a == 0:
        break
    idx += 1
    if a%n == 0:
        res.append("{} is a multiple of {}.".format(a,n))
    else:
        res.append("{} is NOT a multiple of {}.".format(a,n))
print("\n".join(res))
