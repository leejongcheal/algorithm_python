def power(k):
    global A
    global C
    if k == 0:  # n^0 = 1
        return 1
    temp = power(k//2)
    result = (temp*temp) % C
    if k % 2 == 1:
        result *= A
        result %= C
    return result


A,B,C = map(int,input().split())
print(power(B))

