n,n1 = map(int,input().split())
s = set(map(int,input().split()))
s1 = set(map(int,input().split()))
A = s - s1
B = s1 - s
print(len(A)+len(B))