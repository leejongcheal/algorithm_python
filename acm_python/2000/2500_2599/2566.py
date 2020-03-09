L = [list(map(int, input().split())) for _ in range(9)]
x, y = 0, 0
res = L[0][0]
for i in range(9):
    m = max(L[i])
    if res < m:
        x, y = i, L[i].index(max(L[i]))
        res = m
print(res)
print(x+1,y+1)
