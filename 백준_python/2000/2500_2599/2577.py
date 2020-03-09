A = int(input())
B = int(input())
C = int(input())
res = str(A*B*C)
for i in range(10):
    print(res.count(str(i)))
