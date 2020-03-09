M = int(input())
s = input()
N = len(s)//M
L = []
for i in range(N):
    if i % 2 == 0:
        L.append(s[0+i*M:M+i*M])
    else:
        L.append(s[0 + i*M:M + i*M][::-1])
for i in range(M):
    for j in range(N):
        print(L[j][i],end="")
