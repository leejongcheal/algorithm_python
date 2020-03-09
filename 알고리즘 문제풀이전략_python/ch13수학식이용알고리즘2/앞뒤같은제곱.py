def convert(n, base):
    T = "0123456789ABCDEF"  # 이거를 앞에 두고 global 쓸려고 했는데 밑에 있는 T(문제 갯수)로 넘어감
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solve(base):
    cnt = 0
    for n in range(1, 301):
        s = convert(n ** 2, base)
        if s == s[::-1]:
            #print(n,s)
            cnt += 1
    print(cnt)


T = int(input())
L = []
for _ in range(T):
    L.append(int(input()))
for a in L:
    solve(a)
