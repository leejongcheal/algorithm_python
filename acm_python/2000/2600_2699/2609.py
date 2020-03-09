import math
A,B = map(int,input().split())
print(math.gcd(A,B))
print((A*B)//math.gcd(A,B))
