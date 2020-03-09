import sys
t = int(input())
input = sys.stdin.readline
res = []
for _ in range(t):
    l,n = map(int,input().split())
    mid = l/2
    low = 0
    high = 0
    for i in range(n):
        s = int(input())
        if s == mid:
            low = max(low,s)
            high = max(high,s)
        elif s < mid:
            low = max(low,s)
            high = max(high,l-s)
        else:
            low = max(low,l-s)
            high = max(high,s)
    res.append("{} {}".format(low,high))
print("\n".join(map(str,res)))
