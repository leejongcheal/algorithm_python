T = int(input())
for _ in range(T):
    n = int(input())
    res = 0
    s = []
    for i in range(n+1):
        s.append(input())
    for i in range(n):
        if i % 2 == 0:
            res += (s[i+1]+s[i+1]).find(s[i])
        else:
            res += (s[i]+s[i]).find(s[i+1])

    print(res)
