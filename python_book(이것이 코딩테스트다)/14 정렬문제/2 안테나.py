N = int(input())
L = list(map(int, input().split()))
L.sort()
print(L[(N-1)//2])