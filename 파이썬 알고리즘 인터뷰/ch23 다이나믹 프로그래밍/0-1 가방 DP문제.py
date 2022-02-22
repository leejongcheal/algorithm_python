cargo = [(4, 12),(2,1),(10,4),(1,1),(2,2)]
capacity = 15
pack = [[0]*(capacity + 1) for _ in range(len(cargo) + 1)]

for i in range(len(cargo) + 1):
    for j in range(capacity + 1):
        if i == 0 or j == 0:
            pack[i][j] = 0
        elif cargo[i-1][1] <= j:
            pack[i][j] = max(
                cargo[i-1][0] + pack[i-1][j - cargo[i-1][1]],
                pack[i-1][j]
            )
        else:
            pack[i][j] = pack[i-1][j]

for p in pack:
    print(p)
print(pack[5][15])
