import math
M = int(input())
N = int(input())
L = []
if int(math.sqrt(M))**2 == M:
    L.append(M)
for i in range(int(math.sqrt(M))+1,int(math.sqrt(N))+1):
    L.append(i*i)
if len(L) == 0:
    print(-1)
else:
    print(sum(L))
    print(L[0])

