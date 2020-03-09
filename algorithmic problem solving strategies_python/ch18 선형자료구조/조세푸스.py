# 배열의 번호를 증가시키는 방법으로 품
# 더 깔끔한 코딩이나 방법있긴할텐데 귀찮
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    L = []
    for i in range(2,n+1):
        L.append(i)
    i = len(L) - 1
    while len(L) != 2:
        j = 0
        while j<k:
            j += 1
            i += 1
            if i == len(L):
                i = 0
        del L[i]
        i -= 1
        if i < 0:
            i = len(L) - 1
    print(L[0], L[1])
