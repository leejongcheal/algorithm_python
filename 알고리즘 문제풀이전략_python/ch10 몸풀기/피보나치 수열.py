def fi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fi(n-2) + fi(n-1)


a = int(input())
print(fi(a))
