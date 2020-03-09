import sys
L = sys.stdin.read().splitlines()
res = int(L[0])
for i in range(1,len(L),2):
    if L[i] == "=":
        print(res)
        exit()
    a = int(L[i+1])
    if L[i] == "+":
        res += a
    elif L[i] == "-":
        res -= a
    elif L[i] == "*":
        res *= a
    elif L[i] =="/":
        res //= a

