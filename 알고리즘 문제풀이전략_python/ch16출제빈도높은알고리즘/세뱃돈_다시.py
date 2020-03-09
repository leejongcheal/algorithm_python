T = int(input())
MIXIMUM = 100000000
for i in range(T):
    n, k = map(int,input().split())
    solution = [0]*(n+1)
    solution[0] = 1
    for i in range(1,k+1):
        for j in range(i,n+1):
            solution[j] = (solution[j] + solution[j-i])%MIXIMUM
    print(solution[n])

