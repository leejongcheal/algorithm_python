L = [0]
for i in range(1, 5):
    x, y = map(int, input().split())
    L.append(y - x + L[i - 1])
print(max(L))
