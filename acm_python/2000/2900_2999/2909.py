c,k = map(int,input().split())
c = c/(10**k)
if c >= int(c)+0.5:
    c = int(c)+1
else:
    c = int(c)
print(c*(10**k))
