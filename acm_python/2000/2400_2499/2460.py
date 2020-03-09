L = []
a = 0
for i in range(10):
    x,y = map(int,input().split())
    a += y - x
    L.append(a)
print(max(L))
