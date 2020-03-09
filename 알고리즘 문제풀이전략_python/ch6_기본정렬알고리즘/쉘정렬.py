def shell_sort(L):
    n = len(L)
    gab = n // 2
    while gab > 0:
        for start in range(gab):
            shell_insert(L, start, gab)
        #print("After increments of size",gab,"The list is",L)
        gab //= 2


def shell_insert(L, start, gab):
    n = len(L)
    for i in range(start + gab, n, gab):
        key = L[i]
        for j in range(i - gab, -1, -gab):
            if key < L[j]:
                L[j], L[j + gab] = L[j + gab] , L[j]
            else:
                L[j + gab] = key
                break


L = [int(a) for a in input().split()]
shell_sort(L)
print(L)
