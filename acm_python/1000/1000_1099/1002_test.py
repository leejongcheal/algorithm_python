import sys


def check(x):
    if x > 10000:
        return 10000
    if x < -10000:
        return -10000
    return x


def distance(x1, y1, x2, y2):
    return ( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())   # sys.stdin.readline() 이게 더빠름
    d = distance(x1,y1,x2,y2)
    add = (r1+r2)**2
    sub = (r1-r2)**2
    if d == add or (d == sub and d != 0):  # 외접 내접   d!=0주의 !!!
        print(1)
    elif d == 0 and r1 == r2:  # 동일한 원인 경우
        print(-1)
    elif d > add or d < sub:  #원이 서로 밖에 있는경우 or 안에 포함 하는경우
        print(0)
    else:
        print(2)