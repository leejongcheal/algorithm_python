def search_n(X):
    i = 1
    while True:
        if 2*X <= i*(i+1):
            return i
        i += 1


X = int(input())
n = search_n(X)
s = ((n)*(n-1))//2 + 1
if n % 2 == 0:
    a = 1 + (X - s)
    b = n - (X - s)
else:
    b = 1 + (X - s)
    a = n - (X - s)
print("{}/{}".format(a,b))

