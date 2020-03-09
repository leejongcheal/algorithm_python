N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
a = L[1] - L[0]
b = L[1]//L[0]
if L[1] % L[0] == 0 and L[1] + a == L[2]:  # 등차 또는 등비임
    if L[2] % L[1] == 0:  # 등비로 확정
        print(L[N-1]*b)
    else:
        print(L[N-1]+a)
elif L[1] % L[0] == 0:
    print(L[N - 1] * b)
else:
    print(L[N - 1] + a)
