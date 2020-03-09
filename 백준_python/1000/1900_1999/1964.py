def cal(n):
    if n == 1:
        return 5
    else:
        return (3*n*(n+1))//2 + n + 1
N = int(input())
print(cal(N) % 45678)
