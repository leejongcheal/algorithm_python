def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


a,b = (int(c) for c in input().split())
print(gcd(max(a,b),min(a,b)))
