def dfs(now):
    global c_list, h_list, res, visit, M
    if visit.count(1) == M:
        # 거리계산
        s_c_list = []
        for i in range(len(visit)):
            if visit[i] == 1:
                s_c_list.append(c_list[i])
        res = min(res, cal_distance(s_c_list))
        return None
    for i in range(now + 1, len(c_list)):
        visit[i] = 1
        dfs(i)
        visit[i] = 0
    return


def cal_distance(s_c_list):
    global N, h_list
    res = 0
    for hx, hy in h_list:
        h_res = int(1e10)
        for cx, cy in s_c_list:
            h_res = min(h_res, abs(cx - hx) + abs(cy - hy))
        res += h_res
    return res


N , M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
c_list = []
h_list = []
res = int(1e10)
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            h_list.append((i,j))
        elif Map[i][j] == 2:
            c_list.append((i,j))
visit = [0]*(len(c_list))
for i in range(len(c_list)):
    visit[i] = 1
    dfs(i)
    visit[i] = 0
print(res&