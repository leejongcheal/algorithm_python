import sys
name = sys.stdin.read().splitlines()
idx = 0
res = []
while True:
    x, y = map(int,name[idx].split())
    idx += 1
    if x == y == 0:
        break
    carry = 0
    c = 0
    while not (x == y == 0):
        a, b = x%10,y%10
        x, y = x//10,y//10
        if a+b+c > 9:
            carry += 1
            c = 1
        else:
            c = 0
    res.append(carry)
print("\n".join(map(str,res)))
