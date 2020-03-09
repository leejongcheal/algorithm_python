def check(num,i,j):
    global n
    global result
    if n == num:
        result.append([i,j])
N = int(input())
n = int(input())
L = []
for i in range(N+2):
    if i == 0 or i == N+1:
        L.append([-1]*(N+2))
    else:
        L.append([-1]+[0]*(N)+[-1])
x = N*N
i,j = 1,1
result = []
while(x != 0):
    r = 1
    if r%4 == 1:
        while L[i][j] == 0:
            check(x,i,j)
            L[i][j] = x
            x -= 1
            i += 1
        r += 1
        i -= 1
        j += 1
    if r%4 == 2:
        while L[i][j] == 0:
            check(x, i, j)
            L[i][j] = x
            x -= 1
            j += 1
        r += 1
        j -= 1
        i -= 1
    if r%4 == 3:
        while L[i][j] == 0:
            check(x, i, j)
            L[i][j] = x
            x -= 1
            i -= 1
        r += 1
        j -= 1
        i += 1
    if r % 4 == 0:
        while L[i][j] == 0:
            check(x, i, j)
            L[i][j] = x
            x -= 1
            j -= 1
        r += 1
        j += 1
        i += 1
#     #하우상좌 순서
for i in range(N+2):
    if i != 0 and i != N+1:
        for j in range(1,N+1):
            print(L[i][j],end=" ")
        print()
print(result[0][0],result[0][1])
