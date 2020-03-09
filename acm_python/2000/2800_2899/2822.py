L = []
sum = 0
index = []
for _ in range(8):
    L.append(int(input()))
sor = sorted(L, reverse=True)
for i in range(5):
    index.append(L.index(sor[i])+1)
print(sor[0]+sor[1]+sor[2]+sor[3]+sor[4])
print(" ".join(map(str,sorted(index))))

