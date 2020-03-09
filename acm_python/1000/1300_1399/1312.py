A,B,N = map(int,input().split())
for i in range(N):
    A %= B
    A *= 10
    C = A/B
    # print(A,C)
print("%d" % (int(C)))
