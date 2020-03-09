L = sorted(list(map(int, input().split())))
print(max(L[2]-L[1]-1, L[1]-L[0]-1))