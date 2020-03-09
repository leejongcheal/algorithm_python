n=int(input())
L=sorted(list(map(int,input().split())))
R=[]
for i in range(n//2):
    if i%2 == 0:
        R.insert(0,L[-1-i])
        R.append(L[i])
    else:
        R.insert(0,L[i])
        R.append(L[-1-i])
r = 0
for i in range((n//2)*2-1):
    r+=abs(R[i]-R[i+1])
if n%2==0:
    print(r)
else:
    print(max(r+abs(L[n//2]-R[0]),r+abs(L[n//2]-R[-1])))

