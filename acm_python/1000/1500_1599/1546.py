n = int(input())
L = list(map(int,input().split()))
max = max(L)
for i in range(len(L)):
    L[i] =round(L[i]/max*100,2)
print(sum(L)/len(L))
