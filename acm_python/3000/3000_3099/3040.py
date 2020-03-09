L = sorted(list(int(input()) for _ in range(9)))
s = sum(L)
for i in range(8):
    for j in range(i+1,9):
        if s - L[i] - L[j] == 100:
            temp = L[j]
            L.remove(L[i])
            L.remove(temp)
            print("\n".join(map(str,L)))
            exit()
