def cal_dist(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

#[[[x,y]....],[], []]꼴
def comb(L, M):
    result = []
    N = len(L)
    if N < M:
        return None
    if M == 1:
        for i in range(N):
            result.append([L[i]])
    else:
        for i in range(N - M + 1):
            for temp in comb(L[i+1:N], M-1):
                result.append([L[i]]+temp)
    return result

N, M = map(int ,input().split())
Map = []
house_list = []
chicken_list = []
for _ in range(N):
    Map.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            house_list.append([i,j])
        elif Map[i][j] == 2:
            chicken_list.append([i,j])
chiken_m_lists = comb(chicken_list, M)
res = int(1e10)
result = []
for chiken_m_list in chiken_m_lists:
    total = 0
    for house in house_list:
        x1, y1 = house[0], house[1]
        house_dist = int(1e10)
        for chiken in chiken_m_list:
            x2, y2 = chiken[0], chiken[1]
            house_dist = min(house_dist, cal_dist(x1, y1, x2, y2))
        total += house_dist
    if res > total:
        res = total
print(res)


