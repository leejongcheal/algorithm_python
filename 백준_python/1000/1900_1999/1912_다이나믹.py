N = int(input())
L = list(map(int,input().split()))
R = []
for i in range(N):
    if i == 0:
        R.append(L[i])
    else:
        if R[-1]+L[i] > L[i]:
            R.append(L[i]+R[-1])
        else:
            R.append(L[i])
print(max(R))
