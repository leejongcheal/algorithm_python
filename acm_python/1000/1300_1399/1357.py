def rev(n):
    res = 0
    while(n):
        res *= 10
        res += n%10
        n //= 10
    return res


a,b = map(int,input().split())
print(rev(rev(a)+rev(b)))
