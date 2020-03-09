T = int(input())
for _ in range(T):
    n = int(input())
    v = [0]
    for i in range(n):
        v.append(int(input()))
    s = [0]*(n+1)
    s[1] = v[1]
    s[2] = v[1] + v[2]
    for i in range(3,n+1):
        jump = s[i - 2] + v[i]
        nojump = s[i - 3] + v[i] + v[i-1]
        s[i] = max(jump, nojump)
    print(s[n])


