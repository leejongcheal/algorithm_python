s,m = map(int,input().split())
if s-m >= 0 and (s-m)%2 == 0:
    print((s+m)//2,(s-m)//2)
else:
    print(-1)
