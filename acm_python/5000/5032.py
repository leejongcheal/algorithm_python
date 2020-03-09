a, b, c = map(int,input().split())
a = a+b
res = 0
while a//c > 0:
    b = a //c
    a = a%c + b
    res += b
print(res)
