def check_n(n):
    for i in range(1,n+2):  # 1의 경우 일떄 i=2일떄 멈춤 즉 최대 n+1 까지 돌아야함
        if 2*n < (i+1)*i:
            s = (i*(i-1))//2
            return i - 1,s

N = int(input())
result = 0
while N != 0:
    i,s = check_n(N)
    # print(N,i,s)
    result += i
    N -= s
print(result)
