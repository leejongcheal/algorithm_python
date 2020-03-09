# 책에 있는 재귀는 시간 초과라서 그냥 dic(day,heigh)을 그날에 heigh인 확률로 해서 구하면 모든 테스트 케이스에 중복 사용 가능
# 으로 두고 노 재귀 사용하자 오우 풀림!
# 이항계수 써서 바로 풀어버리는 경우가 더 빠르긴함 -> 일부로 거름 문제 풀이방향에는 도움이 안됨
import sys


def solve():
    global dic, m, n, maxday, cache
    if maxday == 0:
        cache[1][1] = 0.25
        cache[1][2] = 0.75
        maxday = 1
    for day in range(maxday+1, m+1):
        for h in range(day,2*day+1):
            if h == day:
                cache[day][h] = cache[day-1][h-1]*0.25
            elif h == 2*day:
                cache[day][h] = cache[day-1][h-2]*0.75
            else:
                cache[day][h] = cache[day-1][h-1]*0.25 + cache[day-1][h-2]*0.75


read = sys.stdin.readline
ans = []
cache = []
maxday = 0
for i in range(1001):
    cache.append([0] * (2 * i + 1))  # [day][height]
for _ in range(int(read())):
    n, m = map(int, read().split())
    res = 0
    if m > maxday:
        solve()
        maxday = m
    for i in range(n, 2 * m + 1):
        res += cache[m][i]
    ans.append(res)
# for i in range(len(cache)):
#     if cache[i][i] != 0:
#         print(cache[i])
for a in ans:
    sys.stdout.write("%.10f\n" % (a))
