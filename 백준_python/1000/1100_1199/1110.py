r = 0
N = int(input())
n = N
while True:
    r += 1
    a = n//10 + n % 10
    n = (n % 10)*10 + a % 10
    # print(n,end=" ")
    if N == n:
        print(r)
        break
