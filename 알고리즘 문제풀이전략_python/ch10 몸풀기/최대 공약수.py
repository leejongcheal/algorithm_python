def gcd(a,b):
    while b:
        a, b = b, a%b
    return a


a, b = (int(c) for c in input().split())
print(gcd(a,b))
