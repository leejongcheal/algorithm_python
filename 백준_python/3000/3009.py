a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
if a1 == a2:
    if b3 == b1:
        print(a3,b2)
    elif b3 == b2:
        print(a3,b1)
elif a1 == a3:
    if b2 == b1:
        print(a2,b3)
    elif b2 == b3:
        print(a2,b1)
elif a2 == a3:
    if b1 == b2:
        print(a1,b3)
    elif b1 == b3:
        print(a1,b2)
