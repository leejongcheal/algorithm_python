L = sorted(list(map(int,input().split())))
d = {"A":L[0],"B":L[1],"C":L[2]}
s = input()
print(d[s[0]],d[s[1]],d[s[2]])