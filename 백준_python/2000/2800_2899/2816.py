n = int(input())
L = [0]
for i in range(n):
    L.append(input())
k1 = L.index("KBS1")
k2 = L.index("KBS2")
if k1 > k2:
    k2 += 1
ans = "1"*(k1-1)+"4"*(k1-1)+"1"*(k2-1)+"4"*(k2-2)
print(ans)

