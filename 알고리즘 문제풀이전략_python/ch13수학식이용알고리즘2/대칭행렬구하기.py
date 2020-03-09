# 대칭행렬 구하기 == xor 연산 사용하기 -> 사실상 암기
T = int(input())
for _ in range(T):
    n = int(input())
    L = input().split()
    for i in range(n):
        for j in range(n):
            print("%c" % (L[i ^ j]), end=" ")
        print()
