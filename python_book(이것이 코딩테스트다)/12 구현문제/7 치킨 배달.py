def abs(n):
    if n < 0:
        n = n * -1
    return n

def dist(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


def comb(L, n):
    N = len(L)
    ret = []
    if N < n:
        return None
    if n == 1:
        for i in L:
            ret.append([i])
    else:
        for i in range(N - n + 1):
            for temp in comb(L[i+1:], n-1):
                ret.append([L[i]] + temp)
    return ret


INF = int(1e9)
chikin_list = []
home_list = []
map_list = []
N, M = map(int, input().split())
result = [INF]*(M+2)
for _ in range(N):
    map_list.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if map_list[i][j] == 1:
            home_list.append((i+1,j+1))
        if map_list[i][j] == 2:
            chikin_list.append((i+1, j+1))
for m in range(1, M+1):
    # ss
    check_chikin = comb(chikin_list, m)
    for check_list in check_chikin:
        cnt = 0
        for h in home_list:
            h_cnt = INF
            for c in check_list:
                d = dist(h, c)
                if d < h_cnt:
                    h_cnt = d
            cnt += h_cnt
        result[m] = min(result[m], cnt)
print(min(result))