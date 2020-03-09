x, y, z = sorted(map(int, input().split()))
if x == y and y == z:
    r = 10000 + x * 1000
elif x == y or y == z:
    r = 1000 + y * 100
elif x == z:
    r = 1000 * z * 100
else:
    r = 100 * z
print(r)
