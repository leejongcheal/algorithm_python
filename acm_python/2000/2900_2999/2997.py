L = sorted(list(int(i) for i in input().split()))
a = L[1] - L[0]
b = L[2] - L[1]
if a == b:
    print(L[2] + a)
else:
    if abs(a) > abs(b):
        print(L[0]+b)
    elif abs(a) < abs(b):
        print(L[1]+a)

