import sys
def fi(n,k):
    if k == 0:
        return 1
    elif L[n][k] != 0:
        return L[n][k]
    else:
        a = fi(n-1, k)+fi(n, k-1)
        L[n][k] = a
        return a

    
L = [[0]*14 for i in range(15)]
for i in range(14):
    L[0][i] = i+1
t = int(input())
name = sys.stdin.read().splitlines()
ans = ""
for i in range(0, 2*t, 2):
    n = int(name[i])
    k = int(name[i+1])
    ans += str(fi(n,k-1))+"\n"
print(ans)