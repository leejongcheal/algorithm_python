L = []
for i in range(10):
    L.append(int(input()))
print(sum(L)//10)
max = L[0]
for i in L:
    if L.count(i) > L.count(max):
        max = i
print(max)
