n,m = map(int,input().split())
a,b = map(int,input().split())
ans = ""
for i in range(n):
    line = ""
    for j in range(m):
        if (i+j)%2 == 0:
            line += "X"*b
        else:
            line += "."*b
    ans += (line+"\n")*a
print(ans)
