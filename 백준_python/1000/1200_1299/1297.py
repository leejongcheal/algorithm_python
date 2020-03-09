import math
c,a,b = map(int,input().split())
x = math.sqrt(c*c/(a*a+b*b))
print("%d %d"%(int(a*x),int(b*x)))